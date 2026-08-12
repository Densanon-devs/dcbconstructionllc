/* Page Consistency
   Wires the nav interactions (mobile toggle, dropdowns, scroll effect) and
   injects the floating mobile call button.

   The header and footer are NOT built here any more. They used to be, but that
   put the site's entire internal link graph — main nav, services dropdown,
   areas dropdown, footer quick links — behind JavaScript execution. Crawlers
   that don't run JS saw 31 pages barely linked to each other, and the services
   hub, reviews, privacy and terms pages were completely orphaned. Both are now
   static HTML in every page.

   If you change a nav or footer link, edit it in every page (or re-run
   tools/staticize_nav.py against a fresh copy). Do not reintroduce runtime
   injection for anything a crawler needs to follow.

   Include in any page and call initPage() near the bottom of <body>:
     <script src="js/page-consistency.js"></script>
     <script>initPage({ depth: 0, activePage: 'home' });</script>

   depth      - retained for backward compatibility; no longer used.
   activePage - retained for backward compatibility; the active nav item is
                now marked up statically.
*/

(function () {
  const PHONE_DISPLAY = '(425) 737-0645';
  const PHONE_TEL     = 'tel:+14257370645';

  // ---- Public entry ----

  window.initPage = function initPage(config) {
    config = config || {};

    if (!config.hideFloatingCall) {
      injectFloatingCall();
    }
    syncFooterYear();
    initNavInteractions();
  };

  // ---- Footer year ----
  // The year is baked into the HTML so it renders without JS; this only
  // corrects it after a New Year until the pages are regenerated.

  function syncFooterYear() {
    const el = document.querySelector('[data-footer-year]');
    if (!el) return;
    const year = String(new Date().getFullYear());
    if (el.textContent.trim() !== year) el.textContent = year;
  }

  // ---- Floating Call Now (mobile only via CSS) ----

  function injectFloatingCall() {
    const btn = document.createElement('a');
    btn.className = 'floating-call';
    btn.href = PHONE_TEL;
    btn.setAttribute('aria-label', 'Call DCB Construction at ' + PHONE_DISPLAY);
    btn.innerHTML = '<span class="floating-call-icon" aria-hidden="true">&#9742;</span><span class="floating-call-text">Call Now</span>';
    document.body.append(btn);
  }

  // ---- Nav interactions (mobile menu, dropdowns, scroll, active link) ----

  function initNavInteractions() {
    const menuToggle = document.querySelector('.menu-toggle');
    const mainNav    = document.querySelector('.main-nav');

    if (menuToggle && mainNav) {
      menuToggle.addEventListener('click', function () {
        this.classList.toggle('active');
        mainNav.classList.toggle('open');
        const isOpen = mainNav.classList.contains('open');
        this.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        document.body.style.overflow = isOpen ? 'hidden' : '';
      });
    }

    // Mobile dropdown — tap parent link to expand
    document.querySelectorAll('.nav-dropdown').forEach(function (dropdown) {
      const link = dropdown.querySelector(':scope > a');
      if (link && window.innerWidth <= 768) {
        link.addEventListener('click', function (e) {
          e.preventDefault();
          dropdown.classList.toggle('open');
        });
      }
    });

    // Reset mobile state on resize to desktop
    window.addEventListener('resize', function () {
      if (window.innerWidth > 768) {
        document.querySelectorAll('.nav-dropdown').forEach(function (d) { d.classList.remove('open'); });
        if (mainNav)    mainNav.classList.remove('open');
        if (menuToggle) { menuToggle.classList.remove('active'); menuToggle.setAttribute('aria-expanded', 'false'); }
        document.body.style.overflow = '';
      }
    });

    // Header scroll-shrink effect
    const header = document.querySelector('.site-header');
    if (header) {
      const onScroll = function () {
        if (window.scrollY > 50) header.classList.add('scrolled');
        else header.classList.remove('scrolled');
      };
      window.addEventListener('scroll', onScroll, { passive: true });
      onScroll();
    }
  }
})();
