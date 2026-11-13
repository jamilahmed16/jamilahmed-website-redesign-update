# jamilahmed.com: deep audit (13 Nov 2026)

This audit was read-only, with one exception: a launch regression that I fixed immediately, explained under "Fixed during the audit".

How the data was collected:
- **Inventory:** every post, page, menu, Themer template and SEO setting, read through Novamira.
- **Crawl:** all 59 public URLs from the Yoast sitemaps, as a logged-out visitor.
- **Links and images:** 291 unique links (external ones checked from the WP Engine server) and 55 unique image files.
- **Speed:** Lighthouse 13.6, mobile, simulated slow 4G, on 5 representative pages.

Raw data is in `audit/`: `inventory.json`, `crawl.json`, `linkcheck.json` and the Lighthouse JSON files.

---

## Fixed during the audit

- **The homepage canonical pointed to `/home-2026/`, which 301-redirects to `/`.** That told Google the homepage was a
  redirect. It was caused by Yoast caching the new page's slug at launch. I set an explicit canonical
  (`https://jamilahmed.com/`), rebuilt the Yoast data for the page and purged the cache. `canonical` and `og:url` are
  now correct.

---

## 1. Pages: must-have, legal, cleanup

**Live pages today:** Home, About, Consulting, Newsletter, Podcast, Contact, Blog, plus the old Beaver page "Home" at `/home/` (ID 820).

| Issue | Evidence | Fix |
|---|---|---|
| **Privacy Policy, Terms & Conditions and Affiliate Disclosure return 404** | Linked from the footer on **57 of 59 pages**. WordPress's privacy-page setting points to page ID 3, which no longer exists. The site earns affiliate commission (Semrush, Moosend, Leonardo and others) with no disclosure page, which is an FTC and Google risk. | Create all three in the new design. Set the privacy page in Settings → Privacy, and the legal pages in Yoast's llms.txt settings. |
| **Old `/home/` page (820) is a duplicate homepage** | Status 200, no meta description, and it loads a Beaver demo image from `lite.demos.wpbeaverbuilder.com`. Yoast's `llms.txt` still lists it as *the* Home page. | 301 to `/`, then trash it. |
| **Missing must-haves for an authority site** | No Services detail pages, no case studies or results page, no media/press or speaking page, no FAQ page in the new design (`/seo-faqs/` is an old post). | Decide which you want. Recommended: **Speaking & Media** (Times Square, Onalytica, HackerNoon, podcast), **Case Studies** (from Reinforce Lab clients you can name) and **AI Search glossary/FAQ hub** (rebuilt from `/seo-glossary/` and `/seo-faqs/`). |
| **The author page reads "Best SEO Consultant"** | `/author/jamilahmed/` has no H1 and a 600-character description. It's the page AI engines use to resolve "who wrote this". | Rebuild it as a proper author/entity page with Person schema, credentials and sameAs links. |
| **Category archives are thin** | All 10 categories are indexed, with no H1, no description and no intro. Topics like "Make Money" and "Email Marketing" don't fit the new positioning. | Reduce to 4 or 5 topical hubs (SEO, AI Search, AI Automation, Personal Branding, Tools & Reviews), each with an intro and an H1. Redirect the rest. |

## 2. Broken links and image issues

**Broken internal links (real 404s)**

| Broken URL | Linked from | Cause |
|---|---|---|
| `/privacy-policy/`, `/terms-conditions/`, `/affiliate-disclosure/` | 57 pages each | Pages deleted |
| `/best-personal-branding-course/`, `/personal-branding-consulting-services/`, `/what-is-social-media-marketing/` | 51 pages each (old footer, "Guides for Beginners") | Pages never existed or were deleted |
| `/increase-website traffic/` | 51 pages (old footer) | **Malformed URL**: contains a space |
| `/best-seo-services/` | 4 posts | Page deleted |
| `/how-to-make-money-with-chatgpt/` | 5 posts | Post deleted |
| `wp-login.php?...post=573&action=edit` | `/seo-glossary/` | An **admin edit link** was pasted into the article |

**Broken affiliate links (lost revenue)**
- `semrush.sjv.io/3evoav` and `semrush.sjv.io/rQmOoB` return **404**. These are Semrush affiliate links, so you're losing commission.
- `trymoo.moosend.com/z2j16j8bjojk` returns **404**, which is the Moosend affiliate link.
- `app.leonardo.ai/?via=jaaff1988` answered 429 (rate-limited during the check). Re-check it by hand.

**Old footer links that technically work but point to thin pages:** "Affiliate Marketing" (14 words), "Content Marketing"
(19 words), "Make Money Blogging" (20 words). See section 3.

**Social links:** LinkedIn (999), Instagram (429), Medium (403) and Quora (403) only failed because those platforms block
automated checks. They are fine for people. The LinkedIn "share" buttons on every post use the deprecated
`shareArticle` URL. They should use `linkedin.com/sharing/share-offsite/?url=`.

**Images**
- **123 images have no width/height attributes.** Missing dimensions make the layout jump as images load.
- **The post-grid thumbnails on the Blog page and on 12 posts have no alt text:** What is SEO, Small Business SEO,
  Personal Blog, SEO Glossary, SEO Basics, SEO FAQs and others.
- **Gravatar avatars show on 36 posts without alt text**, and they're an extra third-party request.
- **The Blog hero loads a 116 KB PNG ("Building Your Personal Brand" book).** That's off-message for the new positioning, and it's the page's LCP element.
- **Featured images:**
  - 7 published posts have none: affiliate-marketing, content-marketing, make-money-blogging, black-friday-deals,
    semrush-pricing, best-local-seo-tools, best-ai-tools-for-writing.
  - Two posts have featured images with no alt text: how-to-build-a-personal-brand and ai-tool-to-convert-text-to-video.
- **The illustration style (purple, orange and teal flat art) clashes with the new palette**, so every post thumbnail needs replacing in the redesign.
- **Several image attachments carry the old positioning in their alt text.** For example, the hero photo's alt reads "Best Personal
  Branding Strategist Jamil Ahmed...". Rewrite these.

## 3. Content: all 38 published posts and 68 drafts

**Published posts (38).** Published Dec 2024 to Jan 2025 and barely touched since. **15 titles carry a year (2024 or 2025)**, so they look stale in 2026 search results.

| Group | Posts | Recommendation |
|---|---|---|
| **Thin placeholders, published** | affiliate-marketing (14 words), what-is-content-marketing (19), how-to-make-money-blogging (20), best-black-friday-deals (18) | These hurt site quality. **Unpublish and 301**, or rewrite properly. They are linked sitewide from the old footer. |
| **Core SEO pillars, keep and rewrite for AI search** | what-is-seo, seo-basics, small-business-seo, seo-for-ceos, seo-glossary, seo-faqs, best-seo-tools-for-saas-companies, best-seo-reporting-tools-for-agencies, best-local-seo-tools | Rewrite around SEO plus AI Search (AEO/GEO), add an answer-first summary, FAQ and author box, then refresh the dates. |
| **Semrush cluster, keep (you're a Semrush Ambassador)** | semrush-pricing, semrush-vs-ahrefs, semrush-vs-surfer-seo, semrush-vs-brightlocal, brightedge-vs-semrush, diib-vs-semrush, semrush-app-center, semrush-agency-growth-kit-review | Update to 2026 data and fix the dead affiliate links. A big opportunity if your SEMrush keyword research supports it. |
| **Personal branding, merge** | what-is-personal-branding, how-to-build-a-personal-brand, personal-branding-strategy, personal-branding-seo | Four posts compete for the same intent. Merge into one or two strong guides and redirect the rest. |
| **AI writing tools, off-core and dated** | copy-ai-reviews, copy-ai-vs-chatgpt, copy-ai-vs-rytr, copy-ai-vs-writesonic, jasper-ai-vs-copy-ai, best-ai-tools-for-writing-seo-rich-blog-content | Six posts about one tool category. Merge into one "AI writing tools for SEO" comparison and redirect the rest, unless Search Console shows real traffic. |
| **Off-positioning** | best-ai-gift-ideas-tools, best-software-for-hosting-webinars, ai-tool-to-convert-text-to-video, decktopus-review, moosend-review, best-ai-tools-for-product-managers, how-to-start-a-blog | Decide one by one with Search Console clicks: keep what earns traffic and affiliate revenue; redirect the rest to the closest topic. |

**Drafts (68).** 2 are near-complete (Local SEO for Rehab Centers, 4,635 words; Cloudways review, 9,503 words), about 8
have real text, and **about 55 are empty titles**, mostly the Semrush how-to series. Those titles map well onto a daily
publishing plan.

**I need two things before rewriting:** your SEMrush keyword research (you said you'll share it), and ideally a
**Google Search Console export of clicks and impressions per page for the last 12 months**. Then each post's decision
(keep, merge, redirect or delete) is based on data, not guesswork.

## 4. Footer (as in your screenshot)

Your reference footer has these blocks:
- social icons (LinkedIn, X, Facebook, Instagram, YouTube, Medium, Quora);
- logo plus bio;
- **Guides for Beginners** (10 links);
- **Latest Posts** (6, automatic);
- **Quick Links** (10).

The new footer currently has only Pages, Connect and Newsletter. Problems in that reference footer that must not be carried over:
- 4 of its 10 Guides links are **404**, and 3 more go to thin posts.
- "SEO Course" and "SEO FAQs" both point to `/seo-faqs/`.
- The bio uses the old positioning ("SEO Consultant and personal branding strategist").

**Plan:** rebuild the footer with every block from your screenshot, in the new design:
- social icons as clean SVGs instead of icon-font PNG boxes;
- the Guides links pointing only to live, rewritten guides;
- Latest Posts automatic;
- Quick Links fixed;
- the bio updated to the new positioning.

Then apply it **sitewide**, replacing the old Themer footer (277).

## 5. Menus: three different navigations

| Where | What shows today |
|---|---|
| New pages (Home, About and others) | New Themer header with the "JA 2026 Main" menu |
| **Every blog post, category, author and `/blog/` page** | **Old Beaver Theme header**: the "Header Menu" is assigned but **has 0 items**, so posts show a logo and **no navigation at all** |
| Footer | Old Themer footer (hard-coded links) on posts; new footer on the new pages |
| Unused | "Footer Menu 01" (empty) |

**Plan:** one header and one footer sitewide. Assign "JA 2026 Main" to the theme's Header location as a fallback, and
delete the empty menus.

## 6. Layout and template issues

- **The old blog templates are still live:**
  - Themer "Blog" archive (393), Themer "Single Blog Post" (232) and "Breadcrumbs" (327).
  - The old Customizer theme: Oswald headings, Roboto Slab buttons and nav, Merriweather Sans logo font, black header.
  - The `/blog/` hero still says **"Get the 5-minute newsletter keeping 2M+ innovators in the loop"**, which conflicts with the 7,600+ figure on the new pages.
- **Single posts:**
  - **Two H1s** on best-ai-tools-for-writing-seo-rich-blog-content.
  - The Lighthouse **heading-order** check fails on Home, About and the glossary.
  - Comment forms are on every post, with 0 comments ever.
  - A Gravatar author box.
  - A LinkedIn share link using the deprecated URL.
- **Accessibility:**
  - Links are distinguished from body text by colour only (`link-in-text-block`).
  - Low contrast on posts.
  - Small tap targets in the post footer and icons.
  - Icon links with no name (the social icons).
- **Background tone:** you want the light backgrounds about 10% darker. The current stone is `#F4F3F1`. Proposal:
  `#E9E7E3` as the main band and `#DFDCD7` for alternating bands, with `#FFFFFF` kept only for form fields. I'll show it
  on one page before applying everywhere, because a full 10% (`#DCDBD9`) starts to read as grey.

## 7. Mobile speed (Lighthouse, mobile, slow 4G)

| Page | Perf | LCP | FCP | TBT | CLS | Weight | Requests |
|---|---|---|---|---|---|---|---|
| Home (new) | 82 | 4.0 s | 2.8 s | 10 ms | 0 | 407 KB | 34 |
| About (new) | 93 | 2.6 s | 2.6 s | 0 | 0 | 313 KB | 30 |
| What is SEO (old post) | 87 | 3.5 s | 2.6 s | 0 | 0 | 579 KB | 42 |
| SEO Glossary (old post) | 85 | 3.7 s | 2.7 s | 10 ms | 0 | 587 KB | 42 |
| **Blog (old archive)** | **75** | **5.8 s** | 2.6 s | 0 | 0 | 876 KB | 49 |

Target: **95+ on mobile and LCP under 2.0 s on every page.** What's slowing pages down, in order of impact:

1. **Fonts: about 360 KB on every post, from 7 families plus 3 icon fonts.**
   - Text fonts: IBM Plex Sans, Oswald, Roboto Slab, Merriweather Sans, Merriweather and Roboto, from the old Customizer
     and Beaver settings. The new pages load Oswald and IBM Plex a second time through their own font request.
   - Icon fonts: Ultimate Icons (91 KB TTF), Font Awesome **Pro** loaded from `pro.fontawesome.com`, and Dashicons (35 KB CSS) on the front end.
   - Fix: **self-host only Oswald 500 and IBM Plex Sans 400/600** (subset WOFF2, about 60 KB in total) with `font-display: swap` and preload.
     Remove Roboto Slab, Merriweather and Roboto. Drop Font Awesome Pro, Ultimate Icons and Dashicons for inline SVG.
2. **Render-blocking CSS: 11 stylesheets plus about 30 KB of inline CSS per page.**
   - Bootstrap 4 (24 KB), Easy TOC (2 files), Magnific Popup, the theme skin, Dashicons, Font Awesome Pro and Ultimate Icons.
   - FCP is stuck at 2.6 to 2.8 s on every page because of this.
3. **jQuery plus jquery-migrate and 13 more scripts on posts.**
   - Easy TOC alone loads 5 files.
   - Fitvids, throttle-debounce and Magnific Popup load even when nothing uses them.
4. **Images.**
   - The Blog hero PNG (116 KB) is the LCP element there.
   - The Home LCP is the hero photo served at 768 px. It should be a ~60 KB AVIF/WebP with `fetchpriority="high"`.
   - 123 images lack dimensions.
5. **Third parties.** Google Tag Manager/gtag (Site Kit), the Cloudflare email-decode script, and Gravatar.
6. **Caching is in place.** WP Engine page cache answered with HIT, and Cloudflare sits in front. Good.

**The constraint:** WP Engine blocks PHP from writing PHP files, so Novamira cannot install a caching or optimisation
plugin, or change PHP. Two ways to get the rest of the gains:
- **(a)** You deploy the child theme once through WP Engine Git push or SFTP. That unlocks dequeuing unused CSS and JS,
  self-hosted fonts and preload. **Recommended.**
- **(b)** Configure WP Engine's built-in tools and settings only. That route is safe, but its gains are smaller.

## 8. SEO, AEO, GEO and LLM visibility

**Entity and schema (biggest gap for AI search)**
- **No `Person` schema anywhere**, and **no `BlogPosting` schema on posts**. The page graph only contains WebSite,
  BreadcrumbList and ImageObject.
- Yoast is set to "Person = user 3", but the Person node isn't printed, and Schema Pro is installed with **0 schemas**.
  So LLMs and Google can't tie "Jamil Ahmed" to his credentials, Reinforce Lab, LinkedIn, Crunchbase or Semrush.
- Fix:
  - One clean `Person` entity with `sameAs` links (LinkedIn, Crunchbase, X, YouTube, Medium, Quora, about.me, Reinforce
    Lab), `jobTitle`, `worksFor` Reinforce Lab, `alumniOf`, `award` and `knowsAbout`.
  - `BlogPosting` with author, `dateModified` and `reviewedBy` on every post.
  - `ProfilePage` on About.
  - `FAQPage` where there are real Q&As.
  - `Service` on Consulting.
  - Turn off Schema Pro or Yoast schema, whichever we don't use, to avoid duplicate graphs.

**llms.txt is stale and misleading.**
- It lists the old `/home/` as Home and only 1 post.
- Fix: switch Yoast's llms.txt to manual selection: About, Consulting, Contact, the legal pages and the rewritten pillar posts.
  Better still, a hand-written `llms.txt` that summarises who Jamil is, his services and his best answers.

**robots.txt.** No rules block AI crawlers (GPTBot, ClaudeBot and PerplexityBot are allowed by default), which is what you want.
Two improvements:
- Add explicit `Allow` lines for OAI-SearchBot, ChatGPT-User, PerplexityBot and ClaudeBot, plus a line pointing to `/llms.txt`.
- Remove the irrelevant `Disallow` lines (`/junk/`, `/old-site/`).

**On-page**
- **16 indexed URLs have no meta description:** the 10 categories, Blog, old Home and 4 posts.
- **13 titles run over 60 characters**, and **15 titles carry 2024 or 2025**.
- The homepage SEO title and the site tagline ("SEO & AI Search Consultant") are both correct.
- **Internal linking is weak.** 6 posts have 3 or fewer internal links pointing to them (seo-for-ceos, semrush-app-center,
  personal-branding-seo and others). No post links to the Consulting page or to Reinforce Lab.

**AEO/GEO content format (for the rewrites)**
- An answer-first 40 to 60 word summary under each H1.
- A "Key takeaways" list.
- Question-shaped H2s that match real queries.
- Tables for comparisons.
- Cited sources with dates.
- An author box with credentials and a "reviewed/updated" date.
- An FAQ block.
- `dateModified` kept current.

These are what AI Overviews, ChatGPT and Perplexity quote.

**Other**
- Comments are open on all posts (0 comments ever). Disable them to cut spam risk and page weight.
- The Gravatar author box exposes a hashed email and adds a third-party request. Replace it with a local author photo.

## Proposed order of work

1. **Today (no content decisions needed):**
   - Legal pages.
   - Fix all broken internal links, the malformed footer URL and the admin link.
   - 301 `/home/` to `/`.
   - Header menu fallback.
   - Person and BlogPosting schema.
   - llms.txt and robots.txt.
   - Meta descriptions for categories and Blog.
   - Image alt text.
   - Disable comments.
2. **Design rollout:**
   - The darker stone tone, shown on one page first.
   - The new sitewide header and full footer (your screenshot's blocks).
   - The new blog archive, category and single-post templates in the Black & Brass system, with an author box, TOC
     styling and FAQ block.
3. **Speed:** font consolidation, removing unused CSS and JS, image conversion, and the hero preload. Needs either the
   one-time child-theme deploy or route (b) from section 7.
4. **Content:** keep, merge or redirect each post using your SEMrush keyword research and Search Console data, then
   rewrite in the AEO/GEO format, then start daily publishing from the keyword plan.

## Decisions I need from you

1. **Legal pages.** Should I draft Privacy Policy, Terms and Affiliate Disclosure from standard templates for a
   Bangladesh-based consultant with US/EU visitors? You would need to approve the text.
2. **Speed path.** (a) a one-time child-theme deploy through WP Engine Git or SFTP (I prepare the files), or (b) settings only.
3. **The thin posts and off-topic posts.** Can I unpublish and redirect the 4 thin placeholders now? The rest waits for your data.
4. **Search Console.** Can you share a 12-month Pages export, or give access?
5. **Affiliate links.** Do you have current Semrush (Impact) and Moosend affiliate links to replace the dead ones?
