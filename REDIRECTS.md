# Legacy URL redirects

## Why this exists

The site went live in its current form on **2026-05-18** (commit `9ba8171`, "Cutover:
live at dcbconstructionllc.com"). It replaced a WordPress install that used a
completely different URL scheme, and **no redirects were put in place**.

Every URL Google had indexed and ranked — `/kitchen-remodel/`,
`/remodeling-post-falls-id/`, `/contact-us/`, and 18 others — began returning a
hard 404. Google keeps 404'd URLs in its index for several weeks before dropping
them, which is why the traffic collapse showed up in **July**, roughly six to ten
weeks after the May cutover, rather than immediately.

The list of retired URLs was recovered from `page-sitemap.xml` and
`posts-index.json` — the WordPress sitemap byproducts kept (gitignored) at the
repo root.

## How the redirects work today

GitHub Pages serves static files only; it cannot issue a server-side `301`. Each
retired URL therefore has a directory containing an `index.html` stub with:

- `<meta http-equiv="refresh" content="0; url=...">` — Google documents an
  **instant** meta-refresh as equivalent to a permanent redirect
- `<link rel="canonical">` pointing at the new URL, to consolidate ranking signals
- a `window.location.replace()` call so real visitors land instantly without
  adding a browser-history entry

There is deliberately **no `noindex`** on these stubs. A `noindex` on a redirect
hop risks propagating to the destination instead of consolidating into it.

## Upgrade path: real 301s via Cloudflare

Meta-refresh redirects work, but a genuine `301` is stronger and faster to be
honored. DNS for `dcbconstructionllc.com` currently points straight at GitHub
Pages (`185.199.108-111.153`) with no proxy in front.

Moving the domain onto Cloudflare (free tier) and proxying it puts a redirect
layer in front of GitHub Pages. Same move already done for `theriverag.church`.
Then load the table below as a **Bulk Redirect List** (Cloudflare dashboard →
Bulk Redirects → create list → upload CSV), with status `301`.

Keep the static stubs in place after the cutover — they cost nothing and cover
the window while DNS propagates.

### Redirect table

| Old WordPress URL | New URL |
| --- | --- |
| `/about-us/` | `/about.html` |
| `/bathroom-remodel/` | `/services/bathroom-remodeling.html` |
| `/contact-us/` | `/contact.html` |
| `/curbless-entry-shower-installation/` | `/services/walk-in-showers.html` |
| `/fireplace-tile-installation/` | `/services/tile-installation.html` |
| `/floor-tile-installation/` | `/services/tile-installation.html` |
| `/in-floor-heating-installation/` | `/services/in-floor-heating.html` |
| `/kitchen-backsplash-installation/` | `/services/tile-installation.html` |
| `/kitchen-remodel/` | `/services/kitchen-remodeling.html` |
| `/kitchen-remodeling-guide-complete-homeowner-blueprint/` | `/services/kitchen-remodeling.html` |
| `/kitchen-remodeling-in-coeur-dalene-id/` | `/services/kitchen-remodeling-coeur-d-alene.html` |
| `/lvt-luxury-vinyl-tile-plank-installation/` | `/services/flooring.html` |
| `/remodeling-athol-id/` | `/areas/hayden.html` |
| `/remodeling-coeur-dalene-id/` | `/areas/coeur-d-alene.html` |
| `/remodeling-hayden-id/` | `/areas/hayden.html` |
| `/remodeling-post-falls-id/` | `/areas/post-falls.html` |
| `/remodeling-sandpoint-id/` | `/areas/coeur-d-alene.html` |
| `/reviews/` | `/reviews.html` |
| `/small-kitchen-remodeling-ideas/` | `/services/kitchen-remodeling.html` |
| `/trim-casing-installation/` | `/services/trim-finishing.html` |
| `/walk-in-shower-installation/` | `/services/walk-in-showers.html` |

`/` and `/services/` carried over unchanged and need no redirect.

## Known compromises

Two retired URLs have **no true equivalent** and currently point at the nearest
real geography:

- `/remodeling-athol-id/` → Hayden (Athol is ~15 minutes north)
- `/remodeling-sandpoint-id/` → Coeur d'Alene

Both were live, indexed area pages under WordPress. Redirecting them to a
different city is a stopgap: it recovers the link signal but not the keyword.
Building genuine `areas/athol.html` and `areas/sandpoint.html` pages and
repointing these redirects would recover the local rankings properly. Note that
`areaServed` in the homepage `GeneralContractor` schema already claims Bonner
County, which is Sandpoint's county.

## Regenerating

The stubs were generated from a map held in the generator script. If more
retired URLs surface (check Search Console → Pages → "Not found (404)"), add them
to the table above and to the generator, then re-run it.
