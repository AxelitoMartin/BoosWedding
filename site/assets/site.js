// Where RSVP submissions are sent. Leave empty to keep the prototype offline:
// answers are then saved in this browser's localStorage only.
// Set to a form backend URL (Formspree, Basin, your own API...) that accepts a JSON POST.
const RSVP_ENDPOINT = "";

const WEDDING_DATE = new Date("2027-09-04T12:00:00+08:00");

// Countdown
(function countdown() {
  const box = document.querySelector("[data-countdown]");
  if (!box) return;
  const out = {
    days: box.querySelector("[data-days]"),
    hours: box.querySelector("[data-hours]"),
    minutes: box.querySelector("[data-minutes]"),
  };
  function tick() {
    const diff = Math.max(0, WEDDING_DATE - new Date());
    out.days.textContent = Math.floor(diff / 86400000);
    out.hours.textContent = Math.floor((diff / 3600000) % 24);
    out.minutes.textContent = Math.floor((diff / 60000) % 60);
  }
  tick();
  setInterval(tick, 30000);
})();

// RSVP form
(function rsvp() {
  const form = document.querySelector("form.rsvp");
  if (!form) return;
  const success = document.querySelector("[data-success]");
  const error = document.querySelector("[data-error]");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const entry = {
      firstName: data.get("firstName"),
      lastName: data.get("lastName"),
      email: data.get("email"),
      address: data.get("address"),
      attending: data.get("attending"),
      guests: data.get("attending") === "yes" ? Number(data.get("guests") || 1) : 0,
      dietary: data.get("dietary") || "",
      dietaryOther: data.get("dietaryOther") || "",
      needsLodgingHelp: data.get("attending") === "yes" && data.get("lodging") === "yes",
      message: data.get("message") || "",
      language: document.documentElement.lang,
      submittedAt: new Date().toISOString(),
    };

    const button = form.querySelector('button[type="submit"]');
    button.disabled = true;
    error.hidden = true;
    try {
      if (RSVP_ENDPOINT) {
        const res = await fetch(RSVP_ENDPOINT, {
          method: "POST",
          headers: { "Content-Type": "application/json", Accept: "application/json" },
          body: JSON.stringify(entry),
        });
        if (!res.ok) throw new Error(res.status);
      } else {
        const saved = JSON.parse(localStorage.getItem("rsvps") || "[]");
        saved.push(entry);
        localStorage.setItem("rsvps", JSON.stringify(saved));
        console.log("RSVP saved locally (prototype mode):", entry);
      }
      form.hidden = true;
      success.hidden = false;
      success.scrollIntoView({ behavior: "smooth", block: "center" });
    } catch (err) {
      console.error(err);
      error.hidden = false;
    } finally {
      button.disabled = false;
    }
  });
})();

// Contact buttons without a web link (WeChat ID): copy the value to the clipboard.
document.querySelectorAll("[data-copy]").forEach((btn) => {
  btn.addEventListener("click", async () => {
    const value = btn.querySelector(".contact-value");
    try {
      await navigator.clipboard.writeText(btn.dataset.copy);
    } catch (err) {
      return;
    }
    value.textContent = "✓ " + (btn.dataset.copied || btn.dataset.copy);
    setTimeout(() => (value.textContent = btn.dataset.copy), 2000);
  });
});
