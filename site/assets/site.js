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
