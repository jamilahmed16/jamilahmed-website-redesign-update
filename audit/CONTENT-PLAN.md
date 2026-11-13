# Content plan: rewrite all posts (13 Nov 2026)

Source: the SEMrush Organic Positions export (US, 12 Nov 2026), in `data/`, plus the SEMrush Domain Overview and the site audit.

## What the data says

- **101 US rankings, 0 estimated visits.**
  - The best position is 43. 87% of rankings sit between 61 and 100; nothing is on page 1 to 4.
  - No page holds US traffic that a rewrite or a redirect could lose.
- **The brand query "jamil ahmed" ranks #73.** Google doesn't connect your name to your own site. This is the first thing
  the Person entity work (schema, About page, sameAs links) has to fix.
- **AI search: visibility 14, 1 mention (AI Mode), 0 cited pages.** Nothing on the site is written in a format that AI answers quote.
- **Authority Score 5, 2.1K referring domains.** The top anchors include
  "high quality dofollow backlinks da 50 pa 40 premium pbn network…" (78 domains) and "using paid blog posts…" (19 domains),
  from directories such as allwebsitesdirectory.com and bestwebstats.com.
  - That's a low-quality or spam link profile. Google mostly ignores links like these, but they add nothing.
  - **Action:** export SEMrush Backlink Audit → toxic domains. Only submit a disavow file if Search Console shows a manual
    action, or if those were paid links you bought.
- **27 of the 34 published posts have no US ranking at all.** That includes what-is-seo, seo-basics, the personal branding set,
  all the Copy.ai posts and most of the Semrush posts.

US data only. Search Console (worldwide clicks and impressions) can still change individual calls, marked ⚑ below.

## Backlinks (SEMrush export, 2,200 links, 13 Nov 2026)

- **2,194 of 2,200 links point to the homepage. 2,091 (95%) are spam**, from 2,032 domains:
  - "Boost Your Rankings with High Authority Backlinks from jamilahmed.com" (1,782 links)
  - "Tiered Link Building" (97)
  - "DA 50 PA 40 Premium PBN" (91)
  - "paid blog posts" (19)
- **The spam is recent and accelerating:** 136 new links in September, **1,563 in October** and 270 in the first 12 days of
  November. It looks like an automated spam or negative-SEO campaign, not links anyone earned.
- **Real links are very few:**
  - reinforcelab.com/management/ (2 followed links: "SEO consultant", "Jamil Ahmed")
  - domestika.org/en/jadirectives (nofollow)
  - The rest of the 109 "non-spam" rows are domain-stats and scraper sites.
- **Post-level links:** only 4 posts have any, all from scraper or aggregator sites:
  - semrush-agency-growth-kit-review (whatarethebest.com)
  - diib-vs-semrush and copy-ai-reviews (affsignal.com)
  - best-seo-tools-for-saas-companies (vuink.com)
- **Every post marked "Retire" has zero backlinks**, so deleting them loses nothing. copy-ai-reviews still gets its planned
  301 into the AI writing tools page.
- **Disavow:** `data/disavow-candidates.txt` lists the 2,032 spam-only domains in Google's format. Two steps:
  1. Check Search Console → Security & Manual actions.
  2. Given the October spike, upload the file at https://search.google.com/search-console/disavow-links. Not one of these
     domains carries value, so disavowing them is low-risk.

  Google says it ignores most spam links on its own. The file is there so you don't have to rely on that.

## Decision for every post

**Rewrite.** Keep the URL, rewrite in the AI-search format, update the title (no year in the slug).

| Post | Why | New angle and target query |
|---|---|---|
| best-seo-reporting-tools-for-agencies | **Biggest cluster: 38 keywords, 13.5K volume, KD 5 to 40**, ranks 62 to 99 | "Best SEO reporting tools for agencies (tested)". Head terms: best seo reporting tools 1.6K, seo reporting software 1.3K, best seo reporting software 1K. Semrush affiliate placement. |
| small-business-seo | "small business seo" 5.4K, KD 29, #83 | Reframe for owner-led B2B: "Small business SEO in the AI search era" |
| seo-glossary | "glossary seo" 1.3K, #93 | **"SEO & AI Search Glossary"**: 200+ terms plus AEO, GEO, LLM, AI Overviews terms. Strong AI-citation asset. Absorbs seo-faqs. |
| brightedge-vs-semrush | KD 6 to 21, #55, 10 keywords | Easiest page-1 win. "BrightEdge vs Semrush" plus a "BrightEdge alternatives" section (320 searches). |
| best-seo-tools-for-saas-companies | KD 0 to 27, 8 keywords | Fits the B2B SaaS industry focus. "Best SEO tools for SaaS". |
| what-is-seo | Pillar, no ranking | "What is SEO? (and how AI search changed it)". Absorbs seo-basics. |
| seo-for-ceos | No ranking, but **exact audience fit** (C-suite) | "SEO & AI Search for CEOs: what to own, what to measure". Links to Consulting. |
| personal-branding-seo | No ranking, strong fit | "Personal brand SEO: how to get your name found and cited by AI". The entity/LLM angle, and proof via your own name. |
| how-to-build-a-personal-brand | Pillar | "How to build a personal brand (for founders and executives)". Absorbs what-is-personal-branding and personal-branding-strategy. |
| semrush-pricing | Ambassador and affiliate | 2026 pricing, plans, the AI toolkit. Fix the dead affiliate link. |
| semrush-vs-ahrefs | Ambassador and affiliate, classic comparison | 2026 update |
| diib-vs-semrush | #43, KD 14: the closest page to page 1 | Update and tighten |
| semrush-vs-surfer-seo, semrush-vs-brightlocal, semrush-app-center, semrush-agency-growth-kit-review, best-local-seo-tools | Semrush/tool cluster with affiliate value | Update to 2026, one internal-link hub (see below) |
| best-ai-tools-for-writing-seo-rich-blog-content | 15 keywords | **"Best AI writing tools for SEO"**: absorbs the five Copy.ai/Jasper posts |
| moosend-review | Email and marketing automation | **Keep only if your Moosend affiliate link is active**; otherwise retire |

**Merge (301 to the stronger page).**

| From | Into |
|---|---|
| seo-basics | what-is-seo |
| seo-faqs | seo-glossary (FAQ section) |
| what-is-personal-branding, personal-branding-strategy | how-to-build-a-personal-brand |
| copy-ai-reviews, copy-ai-vs-chatgpt, copy-ai-vs-rytr, copy-ai-vs-writesonic, jasper-ai-vs-copy-ai | best-ai-tools-for-writing-seo-rich-blog-content |

**Retire (delete; none of these has a single backlink).** Off-positioning, with no meaningful rankings.

| Post | Note |
|---|---|
| best-ai-gift-ideas-tools | 9 keywords, all position 54 or lower, consumer gifts: off-brand |
| best-software-for-hosting-webinars | 2 keywords at #89 and #97 |
| ai-tool-to-convert-text-to-video | no ranking |
| decktopus-review | no ranking |
| best-ai-tools-for-product-managers | 850 searches, but #91 and off-audience. ⚑ Could become part of a future "AI tools for business leaders" piece. |
| how-to-start-a-blog | no ranking, consumer audience. Also remove it from the footer Guides. |

**Rebuild:** best-black-friday-deals, as the evergreen "Black Friday & Cyber Monday deals for SEO, AI and marketing tools", using your affiliate links.

**Result:** 34 posts become about **20 stronger posts**, each tied to your positioning, plus the deals page.

## How every rewrite is written (AEO/GEO format)

1. An answer-first summary of 40 to 60 words right under the H1. This is what AI Overviews and ChatGPT quote.
2. A "Key takeaways" list of 3 to 5 bullets.
3. Question-shaped H2s from the People-also-ask and keyword data.
4. Comparison tables for every "vs" and "best" post, with a "who it's for" row.
5. Original input: your own tests, screenshots, Semrush data and client patterns. This is the E-E-A-T and citation magnet.
6. Sources cited with dates, plus a visible "Updated" date.
7. An FAQ block marked up with FAQPage schema.
8. The author box with credentials, plus BlogPosting and Person schema.
9. Internal links: every post links to its pillar and to Consulting.
10. Affiliate links marked `rel="sponsored"`, with a disclosure line at the top.
11. New featured images in the Black & Brass style, as WebP under 60 KB.

## Topic hubs (categories after the rewrite)

1. **SEO** (what-is-seo, small business, CEOs, glossary)
2. **AI Search** (new: AEO, GEO, LLM visibility, AI Overviews)
3. **SEO Tools** (Semrush cluster, reporting, SaaS, local, AI writing)
4. **Personal Branding** (personal brand, personal brand SEO)
5. **AI Automation** (new: workflows, growth systems)

The old categories (Make Money, Email Marketing, List Posts, Comparison, Review, Software, Blogging) get merged into these and redirected.

## Daily publishing: what I still need

The export above shows where you *already* rank. To plan new daily posts I need **keyword research for topics you want
to own**. In SEMrush Keyword Magic Tool (US plus Worldwide), export these seeds:

- `ai search optimization`, `generative engine optimization`, `llm seo`, `ai overviews seo`, `answer engine optimization`
- `seo for pharmaceutical companies`, `pharma seo`, `healthcare seo`
- `b2b saas seo`, `seo for saas`
- `semrush ai`, `ai seo tools`, `seo reporting`
- `personal branding for executives`, `founder personal brand`

From those I'll build a 90-day calendar: one post a day, grouped by hub, ordered by difficulty and business value.
