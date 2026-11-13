"""Home page (draft, post 853): jamilahmed.com redesign."""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bb import Page, SITE, payload

UP = f"{SITE}/wp-content/uploads"
p = Page()

# 1. Hero: dark band, copy left, editorial photo bleeding to the band's bottom edge.
hero = p.row(bg="ink", cls="ja26-root ja-dark ja-hero", pad=(96, 0), pad_mobile=(56, 0))
left, right = hero.cols(54, 46, align="center", gap=64)
left.heading("SEO &amp; AI Search <em>Consultant</em>", tag="h1", mb=28)
left.text(
    "<p>I'm Jamil Ahmed. I help founders, B2B and pharmaceutical companies get found on Google "
    "and cited in ChatGPT, Perplexity and AI Overviews, then turn that visibility into revenue.</p>",
    cls="ja-lead", mb=40,
)
left.button("Book a consultation", "/contact/", inline=True)
left.button("Get the newsletter", "/newsletter/", ghost=True, inline=True)
right.photo(182, f"{UP}/2023/02/Jamil-Ahmed-Hero-Image-2.jpg",
            alt="Jamil Ahmed, SEO and AI Search Consultant", cls="ja-hero-photo")

# 2. Recognition strip: four real credentials, hairline separated.
rec = p.row(bg="stone", cls="ja-recognition", pad=(56, 56), pad_mobile=(40, 24))
for col, (title, source) in zip(rec.cols(25, 25, 25, 25, gap=40, cls="ja-hair"), [
    ("Semrush Ambassador", "Semrush"),
    ("Top 3 BI Marketing Influencer", "Onalytica, 2018"),
    ("Top 50 eCommerce Influencers", "SaleHoo"),
    ("Featured in Times Square", "New York"),
]):
    col.heading(title, tag="h3", mb=8)
    col.text(f"<p>{source}</p>", cls="ja-caption")

# 3. Point of view: headline over two columns (argument + what that means in practice).
pov = p.row(bg="stone", cls="ja-pov", pad=(56, 112), pad_mobile=(40, 64))
(head,) = pov.cols(100)
head.heading("Your buyers now ask AI <em>before</em> they ask Google.", tag="h2", mb=48, cls="ja-measure")
a, b = pov.cols(50, 50, gap=64)
a.text(
    "<p>Ranking on page one used to be the whole job. Today a CFO compares vendors in ChatGPT, a "
    "procurement lead asks Perplexity for a shortlist, and Google answers before anyone clicks. If your "
    "company is not the source those answers are built on, you are invisible at the moment the decision forms.</p>"
    "<p>I build search strategies for that reality: classic SEO that still drives demand, plus the evidence, "
    "structure and authority that make AI engines cite you by name.</p>",
)
b.text(
    "<ul>"
    "<li><strong>SEO strategy</strong> for enterprise, technical and international sites</li>"
    "<li><strong>AI Search Optimization</strong>: AEO, GEO and LLM visibility</li>"
    "<li><strong>Content systems</strong> built on verified evidence, not volume</li>"
    "<li><strong>AI automation</strong> for research, reporting and lead follow-up</li>"
    "<li><strong>Executive dashboards</strong> that tie search to pipeline</li>"
    "</ul>",
    cls="ja-list",
)

# 4. Ways to work together: one primary offer, two secondary, asymmetric.
work = p.row(bg="graphite", cls="ja-dark ja-work", pad=(112, 112), pad_mobile=(64, 64))
(wh,) = work.cols(100)
wh.heading("Ways to work with me", tag="h2", mb=56)
main, side = work.cols(50, 50, gap=80, cls=["", "ja-side"])
main.heading("SEO &amp; AI Search Audit", tag="h3", mb=16)
main.text(
    "<p>A senior review of how your company shows up on Google and inside AI answers: technical health, "
    "content authority, competitors, and the questions your buyers ask. You get a prioritised 90-day plan "
    "your team can act on.</p>",
    cls="ja-lead", mb=32,
)
main.button("Book a consultation", "/contact/", inline=True)
main.button("What the audit includes", "/seo-ai-search-audit/", ghost=True, inline=True)
side.heading("Executive advisory", tag="h3", mb=12)
side.text(
    "<p>Ongoing strategy for founders and C-suite leaders: what to own in search, what to automate, "
    "and how to measure it in revenue, not rankings.</p>", mb=40,
)
side.heading("Built for you by Reinforce Lab", tag="h3", mb=12)
side.text(
    "<p>When the plan needs a team, my company <a href=\"https://reinforcelab.com/\">Reinforce Lab</a> "
    "builds the full AI Growth System: SEO, AI search, content and automation as one engine.</p>",
)

# 5. Background: portrait with brass frame, story and career rows.
bg = p.row(bg="stone", cls="ja-story", pad=(112, 112), pad_mobile=(64, 64))
ph, story = bg.cols(40, 60, align="top", gap=96)
ph.photo(791, f"{UP}/2025/09/Jamil-Ahmed-Personal-Avatar.jpg", alt="Portrait of Jamil Ahmed", cls="ja-portrait")
story.heading("A pharmacist who learned search from the inside", tag="h2", mb=28)
story.text(
    "<p>I trained as a pharmacist and spent my early career in regulated, export-driven markets, where every "
    "claim needs evidence and every market has its own rules. That discipline is how I approach search.</p>",
    mb=32,
)
story.text(
    "<ul>"
    "<li><strong>2018 to now</strong> &nbsp;Founder &amp; CEO, Reinforce Lab Ltd (Dhaka and Katy, Texas)</li>"
    "<li><strong>2017</strong> &nbsp;Product Manager, Immunology, Janssen (Johnson &amp; Johnson)</li>"
    "<li><strong>2016 to 2017</strong> &nbsp;International Marketing, Square Group</li>"
    "<li><strong>2013 to 2016</strong> &nbsp;International Business, Beacon Pharmaceuticals</li>"
    "</ul>",
    cls="ja-list ja-timeline", mb=32,
)
story.button("Read my story", "/about-me/", ghost=True)

# 6. Industries: one line scrolling left to right (pauses on hover, static for reduced motion).
IND = ["Pharmaceutical &amp; Life Sciences", "Healthcare", "B2B SaaS", "Manufacturing", "Technology",
       "Professional Services", "E-commerce"]
strip = "".join(f"<span>{x}</span><i aria-hidden=\"true\">/</i>" for x in IND)
ind = p.row(bg="ink", cls="ja-dark ja-industries", pad=(88, 88), pad_mobile=(56, 56))
(ic,) = ind.cols(100)
ic.heading("Industries I work with", tag="h2", cls="ja-industries-label", mb=28)
ic.text(f'<div class="ja-marquee"><div class="ja-marquee-track">'
        f'<p class="ja-marquee-set">{strip}</p><p class="ja-marquee-set" aria-hidden="true">{strip}</p>'
        f'</div></div>', cls="ja-marquee-wrap")

# 7. Writing: latest articles from the blog.
wr = p.row(bg="stone", cls="ja-writing", pad=(112, 96), pad_mobile=(64, 56))
(wc,) = wr.cols(100)
wc.heading("Latest writing", tag="h2", mb=48)
wc.posts(3, cls="ja-posts")
wc.button("All articles", "/blog/", ghost=True, mt=48)

# 8. Newsletter and show.
ns = p.row(bg="stone", cls="ja-duo", pad=(0, 112), pad_mobile=(0, 64))
nl, show = ns.cols(50, 50, gap=64, cls=["ja-rule", "ja-rule"])
nl.heading("AI Growth Systems for C-Suite", tag="h3", mb=12)
nl.text(
    "<p>My newsletter for business leaders: practical AI solutions, automation workflows, search strategy "
    "and real case studies. Read by 7,600+ subscribers.</p>", mb=28,
)
nl.button("Subscribe", "/newsletter/")
show.heading("The Jamil Ahmed Show", tag="h3", mb=12)
show.text(
    "<p>Conversations with industry experts, CEOs and founders about search, AI and building a business "
    "that people can find.</p>", mb=28,
)
show.button("Listen to the show", "/podcast/", ghost=True)

# 9. Closing call to action.
cta = p.row(bg="ink", cls="ja-dark ja-cta", pad=(112, 112), pad_mobile=(64, 64))
(cc,) = cta.cols(100)
cc.heading("Want a clear plan for Google <em>and</em> AI search?", tag="h2", mb=24, cls="ja-measure")
cc.text(
    "<p>Tell me where you are today. I'll tell you honestly what to fix first, and whether I'm the right person to help.</p>",
    cls="ja-lead", mb=40,
)
cc.button("Book a consultation", "/contact/")

if __name__ == "__main__":
    print(payload(853, p))
