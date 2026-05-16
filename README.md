# DCB Construction LLC — Website

## Project Overview

**Client:** DCB Construction LLC
**Owner:** David C. Busse
**Scope:** Recover digital presence from prior vendor (Quality Resource LLC) and migrate to a Densanon-built static site under David's control.
**Date Started:** 2026-03-24
**Active Build Window:** 2026-05-04 → 2026-05-08
**Status:** Static site rebuilt and ready to ship pending domain transfer.

## About the Client

DCB Construction LLC is a remodeling contractor serving Northern Idaho (Coeur d'Alene, Post Falls, Hayden, plus Kootenai/Bonner/Boundary/Benewah/Shoshone counties). Specialties: kitchen and bathroom remodeling, walk-in and curbless showers, custom tile work, flooring, in-floor heating, and trim/finishing carpentry. Idaho License RCE-52572. BBB Accredited since 2018.

## Site Map

| Section | Files |
|---|---|
| Top level | `index.html`, `about.html`, `contact.html`, `gallery.html`, `reviews.html` |
| Services (7) | `services/{index, kitchen-remodeling, bathroom-remodeling, walk-in-showers, tile-installation, flooring, in-floor-heating, trim-finishing}.html` |
| Service × City combos (6) | `services/{kitchen,bathroom}-remodeling-{coeur-d-alene,post-falls,hayden}.html` |
| Areas (3) | `areas/{coeur-d-alene, post-falls, hayden}.html` |
| Photos | `assets/img/projects/` — 30 customer-only photos |

Blog removed (was net-negative SEO with fake teaser cards).

## Document Navigation

| Document | Purpose |
|---|---|
| [Executive Summary](00-executive-summary.md) | Real findings from the WP site audit, current state of the rebuild, top strengths/gaps |
| [Scoring Checklist](01-scoring-checklist.md) | Feature-by-feature audit (template; not yet filled) |
| [Recommendations Roadmap](02-recommendations-roadmap.md) | Phased action plan — what shipped, what's next |

## Pending

- **Domain transfer** — Quality Resource committed to send EPP/auth code by Friday 2026-05-08. Domain currently at Cloudflare Registrar in their account (registered 2026-03-05, ICANN 60-day transfer lock expired 2026-05-04). Escalation path if missed: registrar-abuse@cloudflare.com → ICANN Transfer Dispute Resolution
- **Google Business Profile** — David needs to file "Request Access" at business.google.com (7-day auto-transfer if QR doesn't respond)
- **DNS cutover** — once domain is in David's account, change `CNAME` from `testsite.densanon.com` to `dcbconstructionllc.com` and configure GitHub Pages custom domain
- **Citations** — verify NAP consistency on Yelp, Houzz, Angi, Thumbtack
- **In-floor heating + trim-finishing** service pages have no project photos; left without galleries pending more from David

## Local Files (gitignored)

- `credentials.local.md` — wp-admin login (rotated 2026-05-04)
- `backup/` — WP content backup (105 MB), photo triage, content extracts, helper PowerShell scripts

## Contact (on-site)

- (425) 737-0645
- Dcbconstructionllccda@gmail.com
- 5550 N Anne St, Coeur d'Alene, ID 83815
