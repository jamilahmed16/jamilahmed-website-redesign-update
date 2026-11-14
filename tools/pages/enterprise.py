"""Enterprise SEO Consultant service page (/enterprise-seo-consultant/, post 873).
Target: enterprise seo consultant (2,400, KD 18, CPC $49.27)."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bb import Page, payload
POST_ID = int(os.environ.get("POST_ID", "873"))
p = Page()

# 1. Hero
hero = p.row(bg="ink", cls="ja26-root ja-dark", pad=(120, 112), pad_mobile=(64, 64))
(h,) = hero.cols(100)
h.heading("Enterprise SEO <em>Consultant</em>", tag="h1", mb=28, cls="ja-measure")
h.text("<p>Senior enterprise SEO consulting for large, complex and regulated websites. I help leadership and in-house "
       "teams decide what to own on Google and in AI answers, fix what holds the site back at scale, and tie search to "
       "pipeline and revenue.</p>", cls="ja-lead", mb=40)
h.button("Book a consultation", "/contact/", inline=True)
h.button("Start with an audit", "/seo-ai-search-audit/", ghost=True, inline=True)

# 2. Facts strip
facts = p.row(bg="stone", cls="ja-recognition", pad=(56, 56), pad_mobile=(40, 24))
for col, (t, s) in zip(facts.cols(25, 25, 25, 25, gap=40, cls="ja-hair"), [
    ("Senior, hands-on", "You work with me directly"),
    ("Google + AI search", "One strategy for both"),
    ("Regulated markets", "Pharma and healthcare background"),
    ("Works with your teams", "In-house, agencies and IT"),
]):
    col.heading(t, tag="h3", mb=8)
    col.text(f"<p>{s}</p>", cls="ja-caption")

# 3. Why enterprise SEO is different
why = p.row(bg="stone", pad=(56, 112), pad_mobile=(40, 64))
a, b = why.cols(50, 50, gap=64)
a.heading("Enterprise SEO is a coordination problem", tag="h2", mb=24)
a.text("<p>On a large site, the hard part is rarely knowing what to fix. It's getting product, engineering, content, "
       "legal and regional teams to fix the right things in the right order, without breaking what already ranks.</p>"
       "<p>An enterprise SEO consultant brings a senior outside view, sets priorities leadership can sign off, and gives "
       "your teams a plan they can ship through normal release cycles.</p>")
b.heading("Signs you need one", tag="h3", mb=16)
b.text("<ul>"
       "<li>Organic traffic is flat or falling while AI Overviews answer your buyers' questions</li>"
       "<li>Competitors are named in ChatGPT and Perplexity, and your brand isn't</li>"
       "<li>A migration, replatform or redesign is on the roadmap</li>"
       "<li>Several markets, languages or business units compete for the same keywords</li>"
       "<li>SEO reports talk about rankings, and leadership asks about revenue</li>"
       "</ul>", cls="ja-list")

# 4. What I help with
cov = p.row(bg="graphite", cls="ja-dark", pad=(112, 112), pad_mobile=(64, 64))
(ch,) = cov.cols(100)
ch.heading("What I help enterprise teams with", tag="h2", mb=48)
for title, items in [
    ("Strategy and governance", ["What to own in search, by product, market and audience",
                                  "Priorities leadership can approve and fund",
                                  "SEO requirements built into product and release processes"]),
    ("Technical SEO at scale", ["Crawl budget, indexing and duplicate content across millions of URLs",
                                "Templates, internal linking and site architecture",
                                "Core Web Vitals and JavaScript rendering"]),
    ("International SEO", ["Market and language structure, hreflang and localisation",
                           "Avoiding cannibalisation between regions and business units",
                           "Local demand and competitors in each market"]),
    ("AI search visibility", ["How ChatGPT, Perplexity, Gemini and AI Overviews describe your brand",
                              "Entity clarity, structured data and evidence AI engines trust",
                              "Content that gets cited, not just ranked"]),
    ("Migrations and redesigns", ["Redirect and URL mapping plans", "Pre-launch checks and post-launch monitoring",
                                  "Protecting rankings and revenue through the change"]),
    ("Regulated content", ["Evidence-led content for pharma, healthcare and other regulated industries",
                           "Workflows that pass medical, legal and compliance review",
                           "Expertise and trust signals that matter to both Google and AI"]),
]:
    l, r = cov.cols(40, 60, gap=64, cls=["ja-hair", "ja-hair"])
    l.heading(title, tag="h3", mb=40)
    r.text("<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>", cls="ja-list", mb=40)

# 5. Ways to work
ww = p.row(bg="stone", pad=(112, 64), pad_mobile=(64, 40))
(wh,) = ww.cols(100)
wh.heading("Ways to work together", tag="h2", mb=48)
for col, (t, body, link) in zip(ww.cols(33, 34, 33, gap=48, cls="ja-rule"), [
    ("SEO &amp; AI Search Audit", "A senior diagnostic of the whole site, delivered in 24 to 72 hours (longer for very large sites) with a walkthrough and a prioritised 90-day plan.",
     '<a href="/seo-ai-search-audit/">See what the audit includes</a>'),
    ("Executive advisory", "Ongoing strategy for leadership and in-house teams: monthly sessions, priorities, reviews of agency and team work, and reporting tied to pipeline.", ""),
    ("Full build with Reinforce Lab", "When the plan needs more hands, my company Reinforce Lab implements it: SEO, AI search, content systems and automation.", ""),
]):
    col.heading(t, tag="h3", mb=12)
    col.text(f"<p>{body}</p>" + (f"<p>{link}</p>" if link else ""))

# 6. Why me
wm = p.row(bg="stone", pad=(64, 112), pad_mobile=(40, 64))
ml, mr = wm.cols(40, 60, gap=80)
ml.heading("Why work with me", tag="h2", mb=24)
mr.text("<ul>"
        "<li><strong>Enterprise experience from the inside.</strong> Product Manager, Immunology at Janssen (Johnson &amp; Johnson), and international business roles in pharmaceuticals before that.</li>"
        "<li><strong>Founder &amp; CEO of Reinforce Lab</strong>, an AI growth company working across SEO, AI search, content and automation since 2018.</li>"
        "<li><strong>Semrush Ambassador</strong>, and named a Top 3 Business Intelligence Marketing Influencer by Onalytica.</li>"
        "<li><strong>Google and AI search together</strong>, so your teams follow one plan instead of two.</li>"
        "</ul>", cls="ja-list")

# 7. Pricing
pr = p.row(bg="ink", cls="ja-dark ja-pricing", pad=(112, 112), pad_mobile=(64, 64))
pl, pc = pr.cols(50, 50, align="center", gap=80, cls=["", "ja-price-card"])
pl.heading("Pricing", tag="h2", mb=20)
pl.text("<p>Enterprise engagements are scoped to your site, markets and goals. You get a fixed proposal after a short "
        "call, before any work starts.</p>", cls="ja-lead", mb=36)
pl.heading("What shapes the scope", tag="h3", mb=16)
pl.text("<ul>"
        "<li>Number of sites, markets and languages</li>"
        "<li>Size and complexity of the platform</li>"
        "<li>One-off project or ongoing advisory</li>"
        "<li>Advice only, or implementation with Reinforce Lab</li>"
        "</ul>", cls="ja-list")
pc.heading("Every engagement includes", tag="h3", mb=20)
pc.text("<ul>"
        "<li>Direct access to me, not a junior team</li>"
        "<li>Google and AI search in one strategy</li>"
        "<li>Priorities ranked by revenue impact</li>"
        "<li>Plans your teams can ship</li>"
        "<li>Reporting tied to pipeline</li>"
        "<li>Fixed scope before work starts</li>"
        "</ul>", cls="ja-list ja-checks", mb=32)
pc.button("Request a proposal", "/contact/")

# 8. FAQ
FAQ = [
    ("What does an enterprise SEO consultant do?",
     "An enterprise SEO consultant sets search strategy for large or complex websites, finds the technical, content and authority issues that limit growth at scale, and helps in-house teams, agencies and engineering prioritise and ship fixes."),
    ("How is enterprise SEO different from regular SEO?",
     "Scale and coordination. Enterprise sites have more pages, markets, stakeholders and release processes, so the work is as much about governance and prioritisation as about individual fixes."),
    ("Do you replace our SEO agency or in-house team?",
     "No. I usually work alongside them, setting direction and reviewing work. If you need more capacity, my company Reinforce Lab can implement."),
    ("Do you cover AI search as well as Google?",
     "Yes. Every engagement covers visibility in ChatGPT, Perplexity, Gemini and Google's AI Overviews alongside classic SEO."),
    ("Do you work with regulated industries?",
     "Yes. My background is in pharmaceuticals, including Janssen (Johnson &amp; Johnson), so evidence-led content and compliance review are familiar ground."),
    ("How do we start?",
     "Book a consultation. Most enterprise engagements start with the SEO &amp; AI Search Audit, which gives you a prioritised 90-day plan."),
]
qa = p.row(bg="stone", cls="ja-faq", pad=(112, 112), pad_mobile=(64, 64))
(qh,) = qa.cols(100)
qh.heading("Frequently Asked Questions (FAQs)", tag="h2", cls="ja-faq-title", mb=48)
for q, ans in FAQ:
    (qc,) = qa.cols(100, cls="ja-qa")
    qc.heading(q, tag="h3", mb=10)
    qc.text(f"<p>{ans}</p>", mb=32)
schema = {"@context": "https://schema.org", "@graph": [
    {"@type": "Service", "name": "Enterprise SEO consulting", "serviceType": "Enterprise SEO consulting",
     "description": "Senior enterprise SEO consulting for large, complex and regulated websites, covering Google and AI search.",
     "provider": {"@type": "Person", "name": "Jamil Ahmed", "url": "https://jamilahmed.com/"},
     "areaServed": "Worldwide", "url": "https://jamilahmed.com/enterprise-seo-consultant/"},
    {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a.replace("&amp;", "&")}} for q, a in FAQ]},
]}
qc.text('<script type="application/ld+json">' + json.dumps(schema) + '</script>', mb=0)

# 9. Closing CTA
cta = p.row(bg="graphite", cls="ja-dark ja-closing", pad=(112, 112), pad_mobile=(64, 64))
cl, cr = cta.cols(55, 45, align="center", gap=80)
cl.heading("Make search a revenue channel your board <em>understands</em>", tag="h2", mb=24)
cl.text("<p>Tell me about your sites, markets and goals. You'll get a clear recommendation and a fixed proposal, and if "
        "I'm not the right fit, I'll say so.</p>", cls="ja-lead", mb=40)
cl.button("Book a consultation", "/contact/", inline=True)
cl.button("Start with an audit", "/seo-ai-search-audit/", ghost=True, inline=True)
cr.heading("What happens next", tag="h3", mb=20)
cr.text("<ol class=\"ja-next\">"
        "<li><strong>Send a short brief</strong><span>Your sites, markets and what you need from search.</span></li>"
        "<li><strong>Call and proposal</strong><span>We agree scope, stakeholders and timeline.</span></li>"
        "<li><strong>Audit or kickoff</strong><span>Usually the audit first, then a 90-day plan your teams can ship.</span></li>"
        "</ol>", cls="ja-next-wrap")

if __name__ == "__main__":
    print(payload(POST_ID, p))
