"""B2B & SaaS SEO Consultant service page (/b2b-saas-seo-consultant/, post 874).
Targets: b2b seo consultant (1,600, KD 8), saas seo consultant (1,600, KD 9),
fractional seo consultant (210, KD 7), seo consultant for startups (50)."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bb import Page, payload
POST_ID = int(os.environ.get("POST_ID", "874"))
p = Page()

# 1. Hero
hero = p.row(bg="ink", cls="ja26-root ja-dark", pad=(120, 112), pad_mobile=(64, 64))
(h,) = hero.cols(100)
h.heading("B2B &amp; SaaS SEO <em>Consultant</em>", tag="h1", mb=28, cls="ja-measure")
h.text("<p>Your buyers research for weeks, compare vendors in ChatGPT and read three reviews before they book a demo. "
       "I help B2B and SaaS companies show up at every step of that journey, on Google and in AI answers, and turn it "
       "into pipeline.</p>", cls="ja-lead", mb=40)
h.button("Book a consultation", "/contact/", inline=True)
h.button("Start with an audit", "/seo-ai-search-audit/", ghost=True, inline=True)

# 2. Facts strip
facts = p.row(bg="stone", cls="ja-recognition", pad=(56, 56), pad_mobile=(40, 24))
for col, (t, s) in zip(facts.cols(25, 25, 25, 25, gap=40, cls="ja-hair"), [
    ("Pipeline, not traffic", "Measured in demos and deals"),
    ("Google + AI search", "Where buyers shortlist vendors"),
    ("Fractional or project", "Senior help without a full hire"),
    ("Founder-friendly", "Clear priorities, no jargon"),
]):
    col.heading(t, tag="h3", mb=8)
    col.text(f"<p>{s}</p>", cls="ja-caption")

# 3. Why B2B/SaaS SEO is different
why = p.row(bg="stone", pad=(56, 112), pad_mobile=(40, 64))
a, b = why.cols(50, 50, gap=64)
a.heading("B2B search is won before the demo request", tag="h2", mb=24)
a.text("<p>Most B2B and SaaS buyers never search your brand name first. They search the problem, compare categories, "
       "read alternatives pages and ask AI assistants for a shortlist. If you only rank for your own name, you meet buyers "
       "after the decision is half made.</p>"
       "<p>I build search around the buying committee: the questions each role asks, the comparisons they make and the "
       "proof they need, so your pages and your brand are there at each step.</p>")
b.heading("Signs you need a B2B SEO consultant", tag="h3", mb=16)
b.text("<ul>"
       "<li>Traffic grows but demo requests and trials don't</li>"
       "<li>Competitors own the \"best\", \"alternatives\" and \"vs\" searches in your category</li>"
       "<li>ChatGPT and Perplexity recommend other vendors when buyers ask</li>"
       "<li>Content is published every week, with no link to pipeline</li>"
       "<li>You need senior SEO leadership but not a full-time hire yet</li>"
       "</ul>", cls="ja-list")

# 4. What I help with
cov = p.row(bg="graphite", cls="ja-dark", pad=(112, 112), pad_mobile=(64, 64))
(ch,) = cov.cols(100)
ch.heading("What I help B2B and SaaS teams with", tag="h2", mb=48)
for title, items in [
    ("Search strategy tied to pipeline", ["Keywords mapped to buyer stage and role, not volume alone",
                                          "Priorities ranked by likely pipeline value",
                                          "Reporting that connects organic and AI traffic to demos, trials and deals"]),
    ("Bottom-of-funnel pages", ["Comparison, \"vs\" and alternatives pages", "Use case, industry and integration pages",
                                "Pricing and product pages that rank and convert"]),
    ("AI search visibility", ["How ChatGPT, Perplexity, Gemini and AI Overviews shortlist vendors in your category",
                              "Getting cited in the sources AI engines trust, such as reviews, comparisons and data",
                              "Clear entity and product information AI can repeat accurately"]),
    ("Content that earns authority", ["Thought leadership built on your own data and expertise",
                                      "Topic clusters that support your product pages",
                                      "Fewer, better pieces instead of volume"]),
    ("Technical SEO for SaaS sites", ["JavaScript rendering, app and marketing site structure",
                                      "Docs, help centre and subdomain strategy",
                                      "Site speed, indexing and internal linking"]),
]:
    l, r = cov.cols(40, 60, gap=64, cls=["ja-hair", "ja-hair"])
    l.heading(title, tag="h3", mb=40)
    r.text("<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>", cls="ja-list", mb=40)

# 5. Ways to work
ww = p.row(bg="stone", pad=(112, 64), pad_mobile=(64, 40))
(wh,) = ww.cols(100)
wh.heading("Ways to work together", tag="h2", mb=48)
for col, (t, body, link) in zip(ww.cols(33, 34, 33, gap=48, cls="ja-rule"), [
    ("SEO &amp; AI Search Audit", "A senior diagnostic of your site and category, delivered in 24 to 72 hours with a walkthrough and a prioritised 90-day plan.",
     '<a href="/seo-ai-search-audit/">See what the audit includes</a>'),
    ("Fractional SEO lead", "Senior SEO leadership for startups and scale-ups that aren't ready for a full-time hire: strategy, priorities, and direction for your writers, developers and agencies.", ""),
    ("Full build with Reinforce Lab", "When you need execution too, my company Reinforce Lab delivers the plan: SEO, AI search, content systems and automation.", ""),
]):
    col.heading(t, tag="h3", mb=12)
    col.text(f"<p>{body}</p>" + (f"<p>{link}</p>" if link else ""))

# 6. Why me
wm = p.row(bg="stone", pad=(64, 112), pad_mobile=(40, 64))
ml, mr = wm.cols(40, 60, gap=80)
ml.heading("Why work with me", tag="h2", mb=24)
mr.text("<ul>"
        "<li><strong>A founder who sells B2B.</strong> As Founder &amp; CEO of Reinforce Lab since 2018, I live with the same pipeline targets you do.</li>"
        "<li><strong>Product marketing background.</strong> Product Manager at Janssen (Johnson &amp; Johnson) and international marketing roles, so positioning and buyer journeys come first.</li>"
        "<li><strong>Semrush Ambassador</strong>, and named a Top 3 Business Intelligence Marketing Influencer by Onalytica.</li>"
        "<li><strong>Google and AI search together</strong>, so your team follows one plan.</li>"
        "</ul>", cls="ja-list")

# 7. Pricing
pr = p.row(bg="ink", cls="ja-dark ja-pricing", pad=(112, 112), pad_mobile=(64, 64))
pl, pc = pr.cols(50, 50, align="center", gap=80, cls=["", "ja-price-card"])
pl.heading("Pricing", tag="h2", mb=20)
pl.text("<p>Every engagement is scoped to your stage, market and goals. You get a fixed proposal after a short call, "
        "before any work starts.</p>", cls="ja-lead", mb=36)
pl.heading("What shapes the scope", tag="h3", mb=16)
pl.text("<ul>"
        "<li>Your stage: startup, scale-up or established</li>"
        "<li>Number of products, markets and segments</li>"
        "<li>One-off audit, fractional lead or ongoing advisory</li>"
        "<li>Advice only, or implementation with Reinforce Lab</li>"
        "</ul>", cls="ja-list")
pc.heading("Every engagement includes", tag="h3", mb=20)
pc.text("<ul>"
        "<li>Direct access to me, not a junior team</li>"
        "<li>Google and AI search in one strategy</li>"
        "<li>Priorities ranked by pipeline value</li>"
        "<li>Plans your team can ship</li>"
        "<li>Reporting tied to demos and deals</li>"
        "<li>Fixed scope before work starts</li>"
        "</ul>", cls="ja-list ja-checks", mb=32)
pc.button("Request a proposal", "/contact/")

# 8. FAQ
FAQ = [
    ("What does a B2B SEO consultant do?",
     "A B2B SEO consultant builds search strategy around how business buyers research: problem searches, category comparisons, alternatives and AI shortlists. The goal is qualified pipeline, not just traffic."),
    ("What does a SaaS SEO consultant do differently?",
     "SaaS SEO focuses on comparison, alternatives, integration and use case pages, product-led content, and technical issues common to SaaS sites such as JavaScript rendering and docs subdomains."),
    ("What is a fractional SEO consultant?",
     "A fractional SEO consultant gives you senior SEO leadership part-time: strategy, priorities and direction for your team and agencies, without the cost of a full-time hire."),
    ("Do you work with startups?",
     "Yes. Early-stage companies usually start with the audit or a fractional engagement, so the first content and pages target the searches most likely to produce customers."),
    ("Do you cover AI search as well as Google?",
     "Yes. B2B buyers increasingly ask ChatGPT, Perplexity and Gemini for vendor shortlists, so every engagement covers AI visibility alongside classic SEO."),
    ("How do we start?",
     "Book a consultation. Most B2B and SaaS clients start with the SEO &amp; AI Search Audit, which gives you a prioritised 90-day plan."),
]
qa = p.row(bg="stone", cls="ja-faq", pad=(112, 112), pad_mobile=(64, 64))
(qh,) = qa.cols(100)
qh.heading("Frequently Asked Questions (FAQs)", tag="h2", cls="ja-faq-title", mb=48)
for q, ans in FAQ:
    (qc,) = qa.cols(100, cls="ja-qa")
    qc.heading(q, tag="h3", mb=10)
    qc.text(f"<p>{ans}</p>", mb=32)
schema = {"@context": "https://schema.org", "@graph": [
    {"@type": "Service", "name": "B2B and SaaS SEO consulting", "serviceType": "B2B SEO consulting",
     "description": "SEO and AI search consulting for B2B and SaaS companies, focused on pipeline: buyer-journey keyword strategy, comparison and alternatives pages, AI visibility and fractional SEO leadership.",
     "provider": {"@type": "Person", "name": "Jamil Ahmed", "url": "https://jamilahmed.com/"},
     "areaServed": "Worldwide", "url": "https://jamilahmed.com/b2b-saas-seo-consultant/"},
    {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a.replace("&amp;", "&")}} for q, a in FAQ]},
]}
qc.text('<script type="application/ld+json">' + json.dumps(schema) + '</script>', mb=0)

# 9. Closing CTA
cta = p.row(bg="graphite", cls="ja-dark ja-closing", pad=(112, 112), pad_mobile=(64, 64))
cl, cr = cta.cols(55, 45, align="center", gap=80)
cl.heading("Be on the shortlist <em>before</em> the demo request", tag="h2", mb=24)
cl.text("<p>Tell me about your product, market and pipeline goals. You'll get a clear recommendation and a fixed "
        "proposal, and if I'm not the right fit, I'll say so.</p>", cls="ja-lead", mb=40)
cl.button("Book a consultation", "/contact/", inline=True)
cl.button("Start with an audit", "/seo-ai-search-audit/", ghost=True, inline=True)
cr.heading("What happens next", tag="h3", mb=20)
cr.text("<ol class=\"ja-next\">"
        "<li><strong>Send a short brief</strong><span>Your product, buyers and what you need from search.</span></li>"
        "<li><strong>Call and proposal</strong><span>We agree scope, priorities and timeline.</span></li>"
        "<li><strong>Audit or kickoff</strong><span>Usually the audit first, then a 90-day plan tied to pipeline.</span></li>"
        "</ol>", cls="ja-next-wrap")

if __name__ == "__main__":
    print(payload(POST_ID, p))
