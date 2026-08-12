"""Tighten titles and meta descriptions for SERP display.

Titles were running up to 79 characters and descriptions up to 215, both well
past where Google truncates. Several titles also led with the brand instead of
the service + city a local search actually matches on -- the homepage most
importantly, which carried no service keyword at all.

Every page repeats its title in <title>/og:title/twitter:title and its
description in meta description/og:description/twitter:description, so each
replacement is applied to all three.
"""
import io
import os
import re
import sys

ROOT = r"D:\LLCWork\dcbconstructionllc"

# file -> (new title or None, new description or None)
CHANGES = {
    "index.html": (
        "Kitchen & Bath Remodeling, Coeur d'Alene | DCB Construction",
        None,
    ),
    "about.html": (
        None,
        "Meet DCB Construction LLC, a licensed remodeling contractor serving Coeur d'Alene, Post Falls, and Hayden since 2015. Idaho license RCE-52572.",
    ),
    "contact.html": (
        "Contact DCB Construction LLC | Coeur d'Alene, ID",
        "Get a free remodeling estimate from DCB Construction LLC. Serving Coeur d'Alene, Post Falls, and Hayden. Call (425) 737-0645.",
    ),
    "gallery.html": (
        "Remodeling Project Gallery | Coeur d'Alene, ID",
        "Real photos of completed kitchen, bathroom, walk-in shower, fireplace, and tile projects by DCB Construction LLC across Coeur d'Alene and Northern Idaho.",
    ),
    "reviews.html": (
        "Customer Reviews | Coeur d'Alene Remodeling Contractor",
        "Read real reviews from Coeur d'Alene, Post Falls, and Hayden homeowners about DCB Construction LLC. BBB A+ rated with zero complaints.",
    ),
    "services/index.html": (
        "Remodeling Services in Coeur d'Alene, ID | DCB Construction",
        "Kitchen and bathroom remodeling, walk-in showers, tile, flooring, in-floor heating, and trim work from DCB Construction LLC in Coeur d'Alene, Idaho.",
    ),
    "services/kitchen-remodeling.html": (
        "Kitchen Remodeling in Coeur d'Alene, ID | DCB Construction",
        "Custom kitchen remodeling from DCB Construction LLC. Cabinetry, countertops, and layout redesigns for homeowners across Coeur d'Alene and Northern Idaho.",
    ),
    "services/bathroom-remodeling.html": (
        "Bathroom Remodeling in Coeur d'Alene, ID | DCB Construction",
        "Full bathroom renovations, shower replacements, tile work, and accessibility upgrades from DCB Construction LLC in Coeur d'Alene and Northern Idaho.",
    ),
    "services/walk-in-showers.html": (
        "Walk-In & Curbless Showers | Coeur d'Alene, ID",
        "Custom walk-in and curbless shower installation by DCB Construction LLC. Accessible designs with custom tile and frameless glass in Northern Idaho.",
    ),
    "services/tile-installation.html": (
        "Tile Installation in Coeur d'Alene, ID | DCB Construction",
        "Ceramic, porcelain, natural stone, and mosaic tile for bathrooms, kitchens, fireplaces, and floors. DCB Construction LLC, Coeur d'Alene, Idaho.",
    ),
    "services/flooring.html": (
        "Flooring Installation, Coeur d'Alene ID | DCB Construction",
        "Hardwood, laminate, luxury vinyl plank, tile, and natural stone flooring installed by DCB Construction LLC across the Coeur d'Alene region.",
    ),
    "services/in-floor-heating.html": (
        "In-Floor Radiant Heating | Coeur d'Alene, ID",
        "Electric and hydronic radiant floor heating for bathrooms, kitchens, and basements, installed by DCB Construction LLC in Northern Idaho.",
    ),
    "services/trim-finishing.html": (
        "Trim, Casing & Finish Carpentry | Coeur d'Alene, ID",
        "Crown molding, baseboards, door and window casing, wainscoting, and decorative millwork from DCB Construction LLC in Northern Idaho.",
    ),
    # --- service + city combos ---
    "services/kitchen-remodeling-coeur-d-alene.html": (
        "Kitchen Remodeling in Coeur d'Alene, ID | DCB Construction",
        "Custom kitchen remodeling in Coeur d'Alene, Idaho. Full renovations, custom cabinetry, layout redesigns, and tile work from DCB Construction LLC.",
    ),
    "services/bathroom-remodeling-coeur-d-alene.html": (
        "Bathroom Remodeling in Coeur d'Alene, ID | DCB Construction",
        None,
    ),
    "services/kitchen-remodeling-hayden.html": (
        None,
        "Custom kitchen remodeling in Hayden, Idaho. DCB Construction LLC redesigns kitchens for Hayden and Hayden Lake homeowners. Free estimates.",
    ),
    "services/kitchen-remodeling-post-falls.html": (
        None,
        "Kitchen remodeling in Post Falls, Idaho. DCB Construction LLC opens up dated layouts and installs new cabinetry across Post Falls and Kootenai County.",
    ),
    "services/bathroom-remodeling-hayden.html": (
        None,
        "Bathroom remodeling in Hayden, Idaho. Full renovations, walk-in showers, custom tile, and accessibility upgrades for Hayden and Hayden Lake homes.",
    ),
    "services/tile-installation-coeur-d-alene.html": (
        "Tile Installation in Coeur d'Alene, ID | DCB Construction",
        "Expert tile installation in Coeur d'Alene, Idaho. Floors, showers, backsplashes, and fireplaces from DCB Construction LLC. Free estimates.",
    ),
    "services/tile-installation-hayden.html": (
        None,
        "Expert tile installation in Hayden, Idaho. Floors, showers, backsplashes, and fireplaces from DCB Construction LLC. Free estimates.",
    ),
    "services/tile-installation-post-falls.html": (
        None,
        "Expert tile installation in Post Falls, Idaho. Floors, showers, backsplashes, and fireplaces from DCB Construction LLC. Free estimates.",
    ),
    "services/walk-in-showers-coeur-d-alene.html": (
        "Walk-In Showers in Coeur d'Alene, ID | DCB Construction",
        "Custom walk-in and curbless shower installation in Coeur d'Alene, Idaho. Tile, frameless glass, and accessible designs from DCB Construction LLC.",
    ),
    "services/walk-in-showers-hayden.html": (
        "Walk-In Showers in Hayden, ID | DCB Construction LLC",
        "Custom walk-in and curbless shower installation in Hayden, Idaho. Tile, frameless glass, and accessible designs from DCB Construction LLC.",
    ),
    "services/walk-in-showers-post-falls.html": (
        "Walk-In Showers in Post Falls, ID | DCB Construction",
        "Custom walk-in and curbless shower installation in Post Falls, Idaho. Tile, frameless glass, and accessible designs from DCB Construction LLC.",
    ),
    # --- areas ---
    "areas/coeur-d-alene.html": (
        "Home Remodeling in Coeur d'Alene, ID | DCB Construction",
        "Kitchen remodeling, bathroom renovation, tile, and flooring for Coeur d'Alene homeowners. DCB Construction LLC, licensed Idaho contractor. Free estimates.",
    ),
    "areas/hayden.html": (
        None,
        "Kitchen remodeling, bathroom renovation, tile, and flooring for Hayden homeowners. DCB Construction LLC, licensed Idaho contractor. Free estimates.",
    ),
    "areas/post-falls.html": (
        None,
        "Kitchen remodeling, bathroom renovation, tile, and flooring for Post Falls homeowners. DCB Construction LLC, licensed Idaho contractor. Free estimates.",
    ),
}


def esc(text):
    """Escape for use inside an HTML attribute / element text."""
    return text.replace("&", "&amp;")


def main():
    problems = []
    for rel, (new_title, new_desc) in sorted(CHANGES.items()):
        path = os.path.join(ROOT, rel.replace("/", os.sep))
        src = io.open(path, encoding="utf-8").read()
        before = src

        if new_title:
            if len(new_title) > 60:
                problems.append("TITLE >60 (%d): %s" % (len(new_title), rel))
            t = esc(new_title)
            src, n1 = re.subn(r"<title>.*?</title>", "<title>%s</title>" % t, src, flags=re.S)
            src, n2 = re.subn(
                r'(<meta property="og:title" content=")[^"]*(">)', r"\g<1>%s\g<2>" % t, src
            )
            src, n3 = re.subn(
                r'(<meta name="twitter:title" content=")[^"]*(">)', r"\g<1>%s\g<2>" % t, src
            )
            if (n1, n2, n3) != (1, 1, 1):
                problems.append("TITLE replace counts %s: %s" % ((n1, n2, n3), rel))

        if new_desc:
            if len(new_desc) > 160:
                problems.append("DESC >160 (%d): %s" % (len(new_desc), rel))
            d = esc(new_desc)
            src, n1 = re.subn(
                r'(<meta name="description" content=")[^"]*(">)', r"\g<1>%s\g<2>" % d, src
            )
            src, n2 = re.subn(
                r'(<meta property="og:description" content=")[^"]*(">)', r"\g<1>%s\g<2>" % d, src
            )
            src, n3 = re.subn(
                r'(<meta name="twitter:description" content=")[^"]*(">)', r"\g<1>%s\g<2>" % d, src
            )
            if (n1, n2, n3) != (1, 1, 1):
                problems.append("DESC replace counts %s: %s" % ((n1, n2, n3), rel))

        if src != before:
            io.open(path, "w", encoding="utf-8", newline="\n").write(src)
            print("updated  %s" % rel)

    print("")
    if problems:
        print("PROBLEMS:")
        for p in problems:
            print("  " + p)
        sys.exit(1)
    print("All %d pages updated cleanly." % len(CHANGES))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
