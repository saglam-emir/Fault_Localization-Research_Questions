// nav.js - shared across every page: mobile menu toggle + GitHub link
// (populated from metadata.json so it's never hard-coded per page).
document.addEventListener('DOMContentLoaded', () => {
  const nav = document.querySelector('.site-nav');
  const toggle = document.querySelector('.nav-toggle');
  if (nav && toggle) {
    toggle.addEventListener('click', () => {
      const isOpen = nav.classList.toggle('menu-open');
      toggle.setAttribute('aria-expanded', String(isOpen));
    });
  }

  const ghLinks = document.querySelectorAll('.js-gh-link');
  if (ghLinks.length) {
    fetch('data/metadata.json')
      .then(r => r.json())
      .then(meta => { if (meta.github_url) ghLinks.forEach(a => a.href = meta.github_url); })
      .catch(() => {});
  }
});
