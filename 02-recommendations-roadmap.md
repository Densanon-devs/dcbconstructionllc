# DCB Construction LLC — Recommendations Roadmap

**Status as of 2026-09-12.** Phases 1–4 are complete. What remains is measurement,
content depth, and citation work.

> This file was frozen at 2026-05-08 for four months and had gone badly stale —
> it still described the domain transfer as "in flight" long after it landed.
> Every item below was re-verified against the live site on 2026-09-12 rather
> than carried forward on trust.

---

## Open work, in priority order

### P0 — Measurement (blocks everything else)

| # | Item | Status | Notes |
|---|---|---|---|
| 0.1 | **Google Analytics 4** | ❌ Not started | No `gtag`, GTM, or any analytics on any page. Verified 2026-09-12. Blocked on David creating the GA4 property and handing over the `G-XXXXXXXXXX`. |
| 0.2 | **Search Console verification + sitemap submission** | ❌ Not started | No verification meta tag on the site. Jordan can claim a fresh property with his own token — Quality Resource's old `google-site-verification` TXT is still in the Cloudflare zone but is not ours. |

**Why this is P0:** the redirect repair shipped 2026-08-11 to fix the ~80% organic
collapse, and **there is still no way to tell whether it worked.** No 404 report,
no query data, no recovery curve, and no baseline for any metric in the table at
the bottom of this file. Roughly 20 minutes of work unblocks all of it.

### P1 — Content depth

| # | Item | Status | Notes |
|---|---|---|---|
| 1.1 | Trim & finish carpentry photos | ⏳ Requested from David 2026-09-09 | Zero project photos exist. Page currently borrows a shower photo. |
| 1.2 | More in-floor heating photos | 🟡 Partly solved | Four genuine radiant-heat photos were already on the site miscategorised under flooring; they now form a real gallery on the service page. Still no finished-floor-with-thermostat shot. |
| 1.3 | Kitchen photos | ⏳ Requested from David 2026-09-09 | Only 2 kitchen photos for a headline service. |
| 1.4 | Athol + Sandpoint area pages | 🔴 Deliberately deferred | Their old URLs cross-redirect to Hayden/CDA. **Do not build these until there is real, town-specific material** — two more thin area pages would recreate the doorway problem that was just fixed. |

### P2 — Citations and reputation

| # | Item | Status |
|---|---|---|
| 2.1 | NAP consistency audit — Yelp, Houzz, Angi, Thumbtack | ⏳ Not started |
| 2.2 | Review acquisition campaign, target 10+ new Google reviews | ⏳ Not started |
| 2.3 | Before/after sliders | ⏳ Blocked — needs matched before/after pairs |

---

## Completed

### 2026-09-12 — SEO repair pass

- **Doorway content fixed.** The six service+city pages were 91% word-identical
  at worst. Rewritten with genuinely city-specific bodies and FAQ sets:

  | Group | Before (worst pair) | After |
  |---|---|---|
  | walk-in-showers × 3 cities | 91% | **45%** |
  | tile-installation × 3 cities | 91% | **42%** |

  Both now sit below the kitchen/bathroom combo pages (36–40%) that were the
  model to copy. Differentiation is by housing stock and what it actually means
  for the job — older Coeur d'Alene stock and cast-iron waste lines, Post Falls
  production builds and flatness tolerance, larger Hayden master baths, linear
  drains and heated floor.

- **Fabricated project claims removed.** The "differentiating" paragraph on each
  of those pages asserted work in specifically named neighbourhoods
  ("the Honeysuckle area", "Q'emiln Park", "Sanders Beach", "Fernan Lake
  Village"). Those were invented at build time. Three more instances were found
  on pages outside the original six and removed too. Housing-stock description
  is factual and was kept; claims of completed projects in named neighbourhoods
  are gone. See the real-content rule — this is the same failure class as the
  stock photos.

- **Fireplace tile page built** at `services/fireplace-tile-installation.html`.
  `/fireplace-tile-installation/` was its own ranking URL under WordPress and had
  been redirecting to the generic tile page while **23 real fireplace photos**
  — the largest photo set on the site — went unused. The page carries all 23,
  six fireplace-specific FAQs with schema, and content on clearances and hearth
  requirements. The redirect stub now points at it, it is linked from the
  services hub and the tile page, and it is in the sitemap.

- **Contact form added** — see the caveat below. There was no `<form>` element
  anywhere on the site; the contact page offered only `tel:` and `mailto:`.

- **In-floor heating gallery** — four genuine radiant-heat photos promoted onto
  the service page.

- **WebP backlog item closed as a non-issue.** The "10 JPGs still lack WebP
  siblings" item was wrong. All ten re-encode *larger* as WebP because they are
  already-compressed small JPEGs; the only wins are at q60–68, which would
  visibly degrade an already-artefacted source. Correctly left alone.

### 2026-09-09 — Photo provenance

Five stock photos from Quality Resource's March 2026 filler batch removed
(`bathroom-04/05/06/07`, `walkin-shower-01`) and replaced with 12 photos David
sent, all carrying genuine capture EXIF. Gallery showers 4 → 10.

### 2026-08-11 — Traffic collapse repair

21 WordPress redirect stubs, nav and footer baked static, titles and meta
descriptions brought into range, JSON-LD repaired. All verified still live.

### 2026-05 — Recovery, rebuild, takeover, cutover

Content extracted from the vendor WordPress install, static site rebuilt, domain
transferred to Porkbun, DNS moved to Cloudflare, GitHub Pages cutover, Google
Business Profile claimed, HTTPS enforced, sitemap and robots.txt live.

Verified live 2026-09-12: HTTPS enforced (301 http→https), www → apex 301,
`sitemap.xml` 200 with 31 URLs, `robots.txt` 200, WordPress redirect stubs
resolving.

---

## ⚠️ Contact form needs one manual step

The form posts to **FormSubmit.co**, which requires no account but **must be
activated once before it will deliver anything**:

1. Submit the form once from the live site.
2. FormSubmit emails `Dcbconstructionllccda@gmail.com` an activation link.
3. David clicks it. From then on submissions arrive in his inbox.

**Until that happens, submissions are not delivered** and the visitor sees a
FormSubmit confirmation-required page. Do the test submission promptly.

To switch providers instead, change the single `action` attribute in
`contact.html`. The form fields, honeypot, `_next` redirect to `thank-you.html`
and styling are provider-agnostic.

---

## Skipped, and why — do not re-add

- **Review / AggregateRating markup.** Google does not honour self-serving review
  markup for LocalBusiness or Organization. Local stars come from the Google
  Business Profile, not from on-site JSON-LD. An audit pass suggested this; it
  was rejected deliberately.
- **Blog.** Removed 2026-05-08. It was six fake teaser cards and two
  AI-generated articles. Net-negative for a contractor with no time to write.
- **WordPress migration.** The old install ran pirated Elementor Pro on the
  vendor's host. Abandoned entirely.
- **Live chat, chatbot, online quote builder.** Overkill at this volume; the
  in-person consult is the offered process.

---

## Success metrics

Baselines cannot be established until 0.1 and 0.2 land. Target snapshot one year
from the original engagement:

| Metric | Baseline | 12-month target |
|---|---|---|
| Domain controlled by David | ✅ Yes | Yes |
| Google Business Profile owned | ✅ Yes | Yes |
| Google reviews | unknown | 30+ |
| Monthly organic traffic | **unmeasurable — no analytics** | 500+/mo |
| Lead form submissions | **0 — no form existed until 2026-09-12** | 12+/mo |
