"""Bake the shared header + footer into every page as static HTML.

They were previously built at runtime by js/page-consistency.js, which meant the
site's entire internal link graph -- nav, service dropdown, area dropdown, footer
quick links -- existed only after JavaScript executed. Crawlers that do not run
JS saw a set of 31 pages with almost no links between them, and the services hub,
reviews, privacy and terms pages were fully orphaned.

This emits byte-identical markup to what the JS produced, so the existing CSS and
the interaction handlers keep working untouched.
"""
import io
import os
import re
import sys

ROOT = r"D:\LLCWork\dcbconstructionllc"

SERVICES = [
    ("kitchen-remodeling.html",  "Kitchen Remodeling"),
    ("bathroom-remodeling.html", "Bathroom Remodeling"),
    ("walk-in-showers.html",     "Walk-In Showers"),
    ("tile-installation.html",   "Tile Installation"),
    ("flooring.html",            "Flooring"),
    ("in-floor-heating.html",    "In-Floor Heating"),
    ("trim-finishing.html",      "Trim &amp; Finishing"),
]

AREAS = [
    ("coeur-d-alene.html", "Coeur d'Alene"),
    ("post-falls.html",    "Post Falls"),
    ("hayden.html",        "Hayden"),
]

PHONE_DISPLAY = "(425) 737-0645"
PHONE_TEL = "tel:+14257370645"
EMAIL = "Dcbconstructionllccda@gmail.com"
FACEBOOK_URL = "https://www.facebook.com/p/DCB-Construction-LLC-100063575410269/"
GOOGLE_PROFILE_URL = "https://share.google/CpDnAjdtCnlxxiWwL"
YEAR = "2026"


def header_html(root, active):
    def cls(name):
        return ' class="active"' if name == active else ""

    services_items = "\n              ".join(
        '<li><a href="%sservices/%s">%s</a></li>' % (root, slug, label)
        for slug, label in SERVICES
    )
    areas_items = "\n              ".join(
        '<li><a href="%sareas/%s">%s</a></li>' % (root, slug, label)
        for slug, label in AREAS
    )
    services_active = ' class="active"' if active == "services" else ""
    areas_active = ' class="active"' if active == "areas" else ""

    return """<header class="site-header">
    <div class="header-inner">
      <a href="%(root)sindex.html" class="logo">DCB Construction <span>LLC</span></a>

      <nav class="main-nav">
        <ul>
          <li><a href="%(root)sindex.html"%(home)s>Home</a></li>
          <li><a href="%(root)sabout.html"%(about)s>About</a></li>
          <li class="nav-dropdown%(sa_cls)s">
            <a href="%(root)sservices/index.html"%(services_active)s>Services</a>
            <ul class="dropdown-menu">
              %(services_items)s
            </ul>
          </li>
          <li class="nav-dropdown%(aa_cls)s">
            <a href="%(root)sareas/coeur-d-alene.html"%(areas_active)s>Areas</a>
            <ul class="dropdown-menu">
              %(areas_items)s
            </ul>
          </li>
          <li><a href="%(root)sreviews.html"%(reviews)s>Reviews</a></li>
          <li><a href="%(root)sgallery.html"%(gallery)s>Gallery</a></li>
          <li><a href="%(root)scontact.html"%(contact)s>Contact</a></li>
        </ul>
      </nav>

      <a href="%(tel)s" class="header-cta header-cta-desktop">&#9742; %(phone)s</a>

      <button class="menu-toggle" aria-label="Toggle navigation menu" aria-expanded="false">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </header>""" % {
        "root": root,
        "home": cls("home"),
        "about": cls("about"),
        "reviews": cls("reviews"),
        "gallery": cls("gallery"),
        "contact": cls("contact"),
        "sa_cls": " active" if active == "services" else "",
        "aa_cls": " active" if active == "areas" else "",
        "services_active": services_active,
        "areas_active": areas_active,
        "services_items": services_items,
        "areas_items": areas_items,
        "tel": PHONE_TEL,
        "phone": PHONE_DISPLAY,
    }


def footer_html(root):
    services_list = "\n            ".join(
        '<li><a href="%sservices/%s">%s</a></li>' % (root, slug, label)
        for slug, label in SERVICES
    )
    areas_list = "\n            ".join(
        '<li><a href="%sareas/%s">%s</a></li>' % (root, slug, label)
        for slug, label in AREAS
    )

    return """<footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col footer-about">
          <h4>DCB Construction <span style="color: var(--color-accent);">LLC</span></h4>
          <p>Quality craftsmanship in Northern Idaho. We specialize in kitchen and bathroom remodeling, tile installation, flooring, and custom finishing work for homeowners across the Coeur d'Alene region.</p>
          <div class="footer-social">
            <a href="%(fb)s" aria-label="Facebook" target="_blank" rel="noopener noreferrer">FB</a>
            <a href="%(gbp)s" aria-label="Google Business Profile" target="_blank" rel="noopener noreferrer">G</a>
          </div>
        </div>

        <div class="footer-col">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="%(root)sindex.html">Home</a></li>
            <li><a href="%(root)sabout.html">About</a></li>
            <li><a href="%(root)sservices/index.html">Services</a></li>
            <li><a href="%(root)sgallery.html">Gallery</a></li>
            <li><a href="%(root)sreviews.html">Reviews</a></li>
            <li><a href="%(root)scontact.html">Contact</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Our Services</h4>
          <ul>
            %(services_list)s
          </ul>
        </div>

        <div class="footer-col">
          <h4>Service Areas</h4>
          <ul>
            %(areas_list)s
          </ul>
          <p style="margin-top: 1.25rem;"><a href="%(tel)s" style="color: var(--color-accent);">%(phone)s</a></p>
          <p><a href="mailto:%(email)s" style="color: rgba(255,255,255,0.6);">%(email)s</a></p>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; <span data-footer-year>%(year)s</span> DCB Construction LLC. All rights reserved. Idaho License RCE-52572.</p>
        <p><a href="%(root)sprivacy-policy.html">Privacy Policy</a> &nbsp;|&nbsp; <a href="%(root)sterms.html">Terms of Use</a></p>
      </div>
    </div>
  </footer>""" % {
        "root": root,
        "fb": FACEBOOK_URL,
        "gbp": GOOGLE_PROFILE_URL,
        "services_list": services_list,
        "areas_list": areas_list,
        "tel": PHONE_TEL,
        "phone": PHONE_DISPLAY,
        "email": EMAIL,
        "year": YEAR,
    }


INIT_RE = re.compile(r"<script>\s*initPage\(\s*\{(?P<args>[^}]*)\}\s*\)\s*;?\s*</script>")


def main():
    targets = []
    for pattern_dir in ("", "services", "areas"):
        d = os.path.join(ROOT, pattern_dir) if pattern_dir else ROOT
        for name in sorted(os.listdir(d)):
            if name.endswith(".html") and os.path.isfile(os.path.join(d, name)):
                targets.append(os.path.join(d, name))

    changed = 0
    for path in targets:
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        src = io.open(path, encoding="utf-8").read()

        m = INIT_RE.search(src)
        if not m:
            print("SKIP (no initPage): %s" % rel)
            continue
        if "<header" in src or "<footer" in src:
            print("SKIP (already static): %s" % rel)
            continue

        args = m.group("args")
        depth = int(re.search(r"depth:\s*(\d+)", args).group(1))
        am = re.search(r"activePage:\s*'([^']*)'", args)
        active = am.group(1) if am else ""
        root = "../" * depth

        # --- insert header immediately after <body> ---
        bm = re.search(r"<body[^>]*>", src)
        if not bm:
            print("SKIP (no <body>): %s" % rel)
            continue
        src = src[: bm.end()] + "\n\n  " + header_html(root, active) + "\n" + src[bm.end():]

        # --- insert footer immediately before the page-consistency script ---
        sm = re.search(r"[ \t]*<script src=\"[^\"]*page-consistency\.js\"></script>", src)
        if not sm:
            print("SKIP (no page-consistency script): %s" % rel)
            continue
        src = src[: sm.start()] + "\n  " + footer_html(root) + "\n\n" + src[sm.start():]

        io.open(path, "w", encoding="utf-8", newline="\n").write(src)
        changed += 1
        print("baked  depth=%d active=%-9s %s" % (depth, active or "-", rel))

    print("\n%d/%d pages updated." % (changed, len(targets)))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
