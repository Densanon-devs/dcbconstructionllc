"""Generate static redirect stubs for the old WordPress URLs.

GitHub Pages cannot issue server-side 301s, so each retired WordPress URL gets a
directory + index.html containing an instant meta-refresh plus a canonical tag
pointing at the new location. Google documents the instant meta-refresh as
equivalent to a permanent redirect, so ranking signals consolidate onto the new
URL.

Deliberately NO `noindex` on the stubs: noindex on a redirect hop can propagate
to the target instead of consolidating into it.
"""
import os
import sys

ROOT = r"D:\LLCWork\dcbconstructionllc"
BASE = "https://dcbconstructionllc.com"

# old WordPress path -> new site path (site-root-relative)
REDIRECTS = {
    # --- service pages -------------------------------------------------
    "kitchen-remodel":                        "/services/kitchen-remodeling.html",
    "bathroom-remodel":                       "/services/bathroom-remodeling.html",
    "walk-in-shower-installation":            "/services/walk-in-showers.html",
    "curbless-entry-shower-installation":     "/services/walk-in-showers.html",
    "floor-tile-installation":                "/services/tile-installation.html",
    "kitchen-backsplash-installation":        "/services/tile-installation.html",
    "fireplace-tile-installation":            "/services/tile-installation.html",
    "lvt-luxury-vinyl-tile-plank-installation": "/services/flooring.html",
    "in-floor-heating-installation":          "/services/in-floor-heating.html",
    "trim-casing-installation":               "/services/trim-finishing.html",

    # --- service + city ------------------------------------------------
    "kitchen-remodeling-in-coeur-dalene-id":  "/services/kitchen-remodeling-coeur-d-alene.html",

    # --- area pages ----------------------------------------------------
    "remodeling-coeur-dalene-id":             "/areas/coeur-d-alene.html",
    "remodeling-post-falls-id":               "/areas/post-falls.html",
    "remodeling-hayden-id":                   "/areas/hayden.html",
    # Athol and Sandpoint had no replacement page. Nearest real geography:
    # Athol sits ~15 min north of Hayden; Sandpoint is the Bonner County seat.
    # These should become dedicated area pages -- see REDIRECTS.md.
    "remodeling-athol-id":                    "/areas/hayden.html",
    "remodeling-sandpoint-id":                "/areas/coeur-d-alene.html",

    # --- core pages ----------------------------------------------------
    "contact-us":                             "/contact.html",
    "about-us":                               "/about.html",
    "reviews":                                "/reviews.html",

    # --- retired blog posts --------------------------------------------
    "kitchen-remodeling-guide-complete-homeowner-blueprint": "/services/kitchen-remodeling.html",
    "small-kitchen-remodeling-ideas":                        "/services/kitchen-remodeling.html",
}

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Page Moved | DCB Construction LLC</title>
<link rel="canonical" href="{target_abs}">
<meta http-equiv="refresh" content="0; url={target_abs}">
<meta name="description" content="This page has moved. DCB Construction LLC \u2014 kitchen and bathroom remodeling in Coeur d'Alene, Post Falls, and Hayden, Idaho.">
<script>window.location.replace("{target_abs}");</script>
</head>
<body>
<p>This page has moved to <a href="{target_abs}">{target_abs}</a>.</p>
</body>
</html>
"""


def main():
    written = []
    for old, new in sorted(REDIRECTS.items()):
        target_abs = BASE + new

        # sanity: the redirect target must exist on disk
        target_file = os.path.join(ROOT, new.lstrip("/").replace("/", os.sep))
        if new.endswith("/"):
            target_file = os.path.join(target_file, "index.html")
        if not os.path.isfile(target_file):
            print("MISSING TARGET: %s -> %s" % (old, new))
            sys.exit(1)

        out_dir = os.path.join(ROOT, old)
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "index.html")
        with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(TEMPLATE.format(target_abs=target_abs))
        written.append("/%s/  ->  %s" % (old, new))

    print("Wrote %d redirect stubs:" % len(written))
    for line in written:
        print("  " + line)


if __name__ == "__main__":
    main()
