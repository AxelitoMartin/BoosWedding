// Password gate. Each page's content and photos are encrypted at build time
// (AES-256-GCM, key derived from the password with PBKDF2-SHA256), so nothing
// is readable without the password, not even from the page source.

(function () {
  const enc = JSON.parse(document.getElementById("enc").textContent);
  const gate = document.getElementById("gate");
  const form = gate.querySelector("form");
  const input = gate.querySelector("input");
  const error = gate.querySelector("[data-gate-error]");
  const app = document.getElementById("app");
  const STORE = "site-key";

  const b64 = (s) => Uint8Array.from(atob(s), (c) => c.charCodeAt(0));
  const toB64 = (buf) => btoa(String.fromCharCode(...new Uint8Array(buf)));

  async function deriveKey(password) {
    const base = await crypto.subtle.importKey("raw", new TextEncoder().encode(password), "PBKDF2", false, ["deriveKey"]);
    return crypto.subtle.deriveKey(
      { name: "PBKDF2", salt: b64(enc.salt), iterations: enc.iterations, hash: "SHA-256" },
      base,
      { name: "AES-GCM", length: 256 },
      true,
      ["decrypt"]
    );
  }

  // Encrypted blobs are laid out as: 12-byte IV, then ciphertext + GCM tag.
  async function decrypt(key, bytes) {
    return crypto.subtle.decrypt({ name: "AES-GCM", iv: bytes.slice(0, 12) }, key, bytes.slice(12));
  }

  async function decryptImage(key, url) {
    const res = await fetch(url);
    const plain = await decrypt(key, new Uint8Array(await res.arrayBuffer()));
    return URL.createObjectURL(new Blob([plain], { type: "image/jpeg" }));
  }

  async function unlock(key) {
    const html = new TextDecoder().decode(await decrypt(key, b64(enc.page)));
    app.innerHTML = html;
    gate.hidden = true;
    app.hidden = false;
    if (enc.title) document.title = enc.title;

    // Photos
    decryptImage(key, enc.hero).then((url) => document.documentElement.style.setProperty("--hero", `url("${url}")`));
    app.querySelectorAll("img[data-enc-src]").forEach((img) => {
      decryptImage(key, img.dataset.encSrc).then((url) => (img.src = url));
    });

    // Page behaviour (countdown, RSVP form) runs once the content is in place.
    if (enc.script) {
      const s = document.createElement("script");
      s.src = enc.script;
      document.body.appendChild(s);
    }
    if (location.hash) document.getElementById(location.hash.slice(1))?.scrollIntoView();
  }

  async function tryStoredKey() {
    let saved;
    try {
      saved = JSON.parse(localStorage.getItem(STORE) || "null");
    } catch (e) {
      return false;
    }
    if (!saved || saved.salt !== enc.salt) return false;
    try {
      const key = await crypto.subtle.importKey("raw", b64(saved.key), "AES-GCM", true, ["decrypt"]);
      await unlock(key);
      return true;
    } catch (e) {
      return false; // password changed since it was saved
    }
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    error.hidden = true;
    const button = form.querySelector("button");
    button.disabled = true;
    try {
      const key = await deriveKey(input.value);
      await unlock(key);
      try {
        const raw = await crypto.subtle.exportKey("raw", key);
        localStorage.setItem(STORE, JSON.stringify({ salt: enc.salt, key: toB64(raw) }));
      } catch (err) {
        // Private browsing: the guest will simply be asked again next time.
      }
    } catch (err) {
      error.hidden = false;
      input.select();
    } finally {
      button.disabled = false;
    }
  });

  tryStoredKey().then((ok) => {
    if (!ok) {
      gate.hidden = false;
      input.focus();
    }
  });
})();
