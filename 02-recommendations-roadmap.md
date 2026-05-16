# DCB Construction LLC — Recommendations Roadmap

Status as of 2026-05-08. Phase 1 + Phase 2 are done; Phase 3 + Phase 4 are pending.

---

## Phase 1: Recovery (DONE 2026-05-04 → 2026-05-05)

| # | Item | Status |
|---|---|---|
| 1.1 | Secure wp-admin access from prior vendor | ✅ Logged in, password rotated, stored in `credentials.local.md` |
| 1.2 | Full content backup before vendor shutdown | ✅ WP XML export + REST API extracts (22 pages, 2 posts) + 147 media files (105 MB) in `backup/` |
| 1.3 | Identify domain registrar and lock state | ✅ Cloudflare Registrar (in Quality Resource's account); registered 2026-03-05; `clientTransferProhibited` (standard lock); ICANN 60-day lock expired 2026-05-04 |
| 1.4 | Triage media — separate real customer photos from stock/stolen | ✅ 30 customer-only retained, 117 stock/duplicates rejected |

---

## Phase 2: Static Site Rebuild (DONE 2026-05-04 → 2026-05-08)

| # | Item | Status |
|---|---|---|
| 2.1 | Replace placeholder image divs with real photos across all pages | ✅ index, about, gallery, services/index, all 3 area pages |
| 2.2 | Rebuild gallery.html with 30 real photos in 5 categories | ✅ Kitchens (2), Bathrooms (12), Showers (4), Tile (6), Flooring (3); fabricated city/description copy removed |
| 2.3 | Add "Recent Projects" gallery sections to service pages | ✅ Kitchen, Bathroom, Walk-in Showers, Tile, Flooring (5/7). In-floor heating + trim-finishing skipped — no photos available |
| 2.4 | Hero image on index.html | ✅ `walkin-shower-02.jpg` background with dark overlay |
| 2.5 | Remove blog (6 fake teaser cards + 2 AI-generated articles) | ✅ Deleted `blog.html`, stripped 18 nav references across 16 files |
| 2.6 | LocalBusiness/GeneralContractor JSON-LD on index.html | ✅ NAP, hours, license RCE-52572, service area (5 counties + 3 cities), services catalog, BBB + Facebook sameAs |
| 2.7 | FAQPage JSON-LD on all 7 service pages | ✅ 32 Q/A pairs auto-extracted and injected |
| 2.8 | 6 service+city combo pages | ✅ kitchen×{CDA, PF, Hayden} + bathroom×{CDA, PF, Hayden} — each with unique intro, area context, photo gallery, 4 city-specific FAQs, Service+FAQPage schema |
| 2.9 | Cross-link combo pages from service hubs and area pages | ✅ Both directions wired |

---

## Phase 3: Takeover (IN FLIGHT, 2026-05-06 → ?)

| # | Item | Status / Blocker |
|---|---|---|
| 3.1 | Get EPP / auth code from Quality Resource | 🟡 Committed to Friday 2026-05-08 (today). Escalation path: registrar-abuse@cloudflare.com → ICANN Transfer Dispute Resolution Process |
| 3.2 | Initiate domain transfer to David's own registrar account | ⏳ Blocked on 3.1 |
| 3.3 | File Google Business Profile "Request Access" | ⏳ Not yet done. Most-leverage outstanding move. 7-day auto-transfer at business.google.com |
| 3.4 | Pre-pick backup domain (don't register yet) | ⏳ E.g. `dcbconstructioncda.com`. Register only if QR misses Friday deadline (registering early signals to QR you're walking) |
| 3.5 | Confirm all final invoices with QR are settled | ⏳ Document in writing |

---

## Phase 4: Cutover + Polish (BLOCKED on Phase 3)

| # | Item | Notes |
|---|---|---|
| 4.1 | Update `CNAME` from `testsite.densanon.com` to `dcbconstructionllc.com` | After domain transfer completes (typically 5–7 days post-EPP) |
| 4.2 | Configure GitHub Pages custom domain + HTTPS | Settings → Pages → Custom domain |
| 4.3 | Verify Google Search Console for `dcbconstructionllc.com` | Submit sitemap (need to generate `sitemap.xml`) |
| 4.4 | Set up Google Analytics 4 | Add GA4 tag to all pages via shared snippet or `<head>` injection |
| 4.5 | Test contact form delivery in production | Currently MetForm-style form on contact page; may need to wire to Formspree, Netlify Forms, or similar (since we're static) |

---

## Phase 5: Growth Work (LATER)

| # | Item | Notes |
|---|---|---|
| 5.1 | Citation cleanup — NAP consistency | Verify name/address/phone match on BBB ✓, Yelp, Houzz, Angi, Thumbtack |
| 5.2 | Get more real photos for in-floor heating + trim-finishing | Ask David; add to those 2 service pages once received |
| 5.3 | Review acquisition campaign | Email past customers asking for Google reviews; target 10+ to lift the GBP listing |
| 5.4 | Add `sitemap.xml` and `robots.txt` | Trivial, do once domain is live |
| 5.5 | Service+city combo pages for additional services | Walk-in showers, tile installation are the next-most-searched. 3 cities × 2 services = 6 more potential pages |
| 5.6 | Before/after sliders on gallery | Once we have before/after pairs from real projects |

---

## Skipped (intentionally)

- **Blog** — net-negative SEO for a small contractor without time to write real posts. Removed 2026-05-08
- **WP install migration** — running pirated PRO Elements, on Quality Resource's host. Abandoning entirely once cutover happens
- **Live chat / chatbot** — overkill for a one-person contractor
- **Online quote builder** — too generic to be useful at this volume; in-person consult is already the offered process

---

## Budget Considerations

| Phase | Cost so far | Notes |
|---|---|---|
| Phase 1 | $0 | Pure labor — content extraction and triage |
| Phase 2 | $0 | Pure labor — static site build |
| Phase 3 | ~$0 (or ~$10 backup domain) | Domain transfer at Cloudflare = $0 markup, just renews at registry rate (~$10/yr). Backup domain only if needed |
| Phase 4 | $0 | GitHub Pages is free; GA4 + Search Console free |
| Phase 5 | Variable | Depends on whether citations need paid services or manual cleanup |

Compared to Quality Resource's monthly retainer (which David was paying for years), the new arrangement runs at ~$10/yr for the domain plus David's time on content updates. No recurring vendor cost.

---

## Success Metrics (target snapshot for 2027-05-08, 1 year out)

| Metric | Baseline (now) | 6-month target | 12-month target |
|---|---|---|---|
| Domain controlled by David | No (QR's Cloudflare account) | Yes | Yes |
| Google Business Profile owned by David | No | Yes | Yes |
| Google reviews | (unknown current count) | 15+ | 30+ |
| Monthly organic search traffic | (no analytics yet) | 200+/mo | 500+/mo |
| Lead form submissions / month | (no tracking yet) | 5+ | 12+ |
| Phone call volume / month | (unknown) | track via GA4 + call tracking | track |
