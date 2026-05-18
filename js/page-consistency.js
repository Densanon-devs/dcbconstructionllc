/* Page Consistency
   Injects shared header + footer across every page on the DCB site, and
   wires the nav interactions (mobile toggle, dropdowns, scroll effect,
   active link highlight). Mirrors the pattern used by densanon-toolkit.

   Include in any page and call initPage() near the bottom of <body>:
     <script src="js/page-consistency.js"></script>
     <script>initPage({ depth: 0, activePage: 'home' });</script>

   depth      - 0 for root pages, 1 for /services/ and /areas/ pages.
                Used to compute relative path back to root.
   activePage - 'home' | 'about' | 'services' | 'areas' | 'reviews'
                | 'gallery' | 'contact' | null. Highlights the matching
                nav item.
*/

(function () {
  // ---- Tables of nav + footer content (single source of truth) ----

  const SERVICES = [
    { slug: 'kitchen-remodeling.html',   label: 'Kitchen Remodeling' },
    { slug: 'bathroom-remodeling.html',  label: 'Bathroom Remodeling' },
    { slug: 'walk-in-showers.html',      label: 'Walk-In Showers' },
    { slug: 'tile-installation.html',    label: 'Tile Installation' },
    { slug: 'flooring.html',             label: 'Flooring' },
    { slug: 'in-floor-heating.html',     label: 'In-Floor Heating' },
    { slug: 'trim-finishing.html',       label: 'Trim &amp; Finishing' }
  ];

  const AREAS = [
    { slug: 'coeur-d-alene.html', label: "Coeur d'Alene" },
    { slug: 'post-falls.html',    label: 'Post Falls' },
    { slug: 'hayden.html',        label: 'Hayden' }
  ];

  const PHONE_DISPLAY = '(425) 737-0645';
  const PHONE_TEL     = 'tel:+14257370645';
  const EMAIL         = 'Dcbconstructionllccda@gmail.com';
  const FACEBOOK_URL  = 'https://www.facebook.com/p/DCB-Construction-LLC-100063575410269/';

  // ---- Public entry ----

  window.initPage = function initPage(config) {
    config = config || {};
    const depth = config.depth || 0;
    const root  = depth === 0 ? '' : '../'.repeat(depth);
    const active = config.activePage || '';

    injectHeader(root, active);
    injectFooter(root);
    if (!config.hideFloatingCall) {
      injectFloatingCall();
    }
    initNavInteractions();
  };

  // ---- Header ----

  function injectHeader(root, active) {
    const isActive = name => name === active ? ' class="active"' : '';

    const servicesItems = SERVICES.map(s =>
      `<li><a href="${root}services/${s.slug}">${s.label}</a></li>`
    ).join('\n              ');

    const areasItems = AREAS.map(a =>
      `<li><a href="${root}areas/${a.slug}">${a.label}</a></li>`
    ).join('\n              ');

    const servicesActive = active === 'services' ? ' class="active"' : '';
    const areasActive    = active === 'areas'    ? ' class="active"' : '';

    const header = document.createElement('header');
    header.className = 'site-header';
    header.innerHTML = `
    <div class="header-inner">
      <a href="${root}index.html" class="logo">DCB Construction <span>LLC</span></a>

      <nav class="main-nav">
        <ul>
          <li><a href="${root}index.html"${isActive('home')}>Home</a></li>
          <li><a href="${root}about.html"${isActive('about')}>About</a></li>
          <li class="nav-dropdown${servicesActive ? ' active' : ''}">
            <a href="${root}services/index.html"${servicesActive}>Services</a>
            <ul class="dropdown-menu">
              ${servicesItems}
            </ul>
          </li>
          <li class="nav-dropdown${areasActive ? ' active' : ''}">
            <a href="${root}areas/coeur-d-alene.html"${areasActive}>Areas</a>
            <ul class="dropdown-menu">
              ${areasItems}
            </ul>
          </li>
          <li><a href="${root}reviews.html"${isActive('reviews')}>Reviews</a></li>
          <li><a href="${root}gallery.html"${isActive('gallery')}>Gallery</a></li>
          <li><a href="${root}contact.html"${isActive('contact')}>Contact</a></li>
        </ul>
      </nav>

      <a href="${PHONE_TEL}" class="header-cta header-cta-desktop">&#9742; ${PHONE_DISPLAY}</a>

      <button class="menu-toggle" aria-label="Toggle navigation menu">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>`;

    document.body.prepend(header);
  }

  // ---- Footer ----

  function injectFooter(root) {
    const servicesList = SERVICES.map(s =>
      `<li><a href="${root}services/${s.slug}">${s.label}</a></li>`
    ).join('\n            ');

    const areasList = AREAS.map(a =>
      `<li><a href="${root}areas/${a.slug}">${a.label}</a></li>`
    ).join('\n            ');

    const year = new Date().getFullYear();

    const footer = document.createElement('footer');
    footer.className = 'site-footer';
    footer.innerHTML = `
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col footer-about">
          <h4>DCB Construction <span style="color: var(--color-accent);">LLC</span></h4>
          <p>Quality craftsmanship in Northern Idaho. We specialize in kitchen and bathroom remodeling, tile installation, flooring, and custom finishing work for homeowners across the Coeur d'Alene region.</p>
          <div class="footer-social">
            <a href="${FACEBOOK_URL}" aria-label="Facebook" target="_blank" rel="noopener noreferrer">FB</a>
          </div>
        </div>

        <div class="footer-col">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="${root}index.html">Home</a></li>
            <li><a href="${root}about.html">About</a></li>
            <li><a href="${root}services/index.html">Services</a></li>
            <li><a href="${root}gallery.html">Gallery</a></li>
            <li><a href="${root}reviews.html">Reviews</a></li>
            <li><a href="${root}contact.html">Contact</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Our Services</h4>
          <ul>
            ${servicesList}
          </ul>
        </div>

        <div class="footer-col">
          <h4>Service Areas</h4>
          <ul>
            ${areasList}
          </ul>
          <p style="margin-top: 1.25rem;"><a href="${PHONE_TEL}" style="color: var(--color-accent);">${PHONE_DISPLAY}</a></p>
          <p><a href="mailto:${EMAIL}" style="color: rgba(255,255,255,0.6);">${EMAIL}</a></p>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; ${year} DCB Construction LLC. All rights reserved. Idaho License RCE-52572.</p>
        <p><a href="${root}privacy-policy.html">Privacy Policy</a> &nbsp;|&nbsp; <a href="${root}terms.html">Terms of Use</a></p>
      </div>
    </div>`;

    document.body.append(footer);
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
        document.body.style.overflow = mainNav.classList.contains('open') ? 'hidden' : '';
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
        if (menuToggle) menuToggle.classList.remove('active');
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
