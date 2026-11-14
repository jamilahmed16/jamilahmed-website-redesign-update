"""SEO & AI Search Audit service page (/seo-ai-search-audit/, post 872).
Targets: seo audit service (3,600, KD 26), ai search audit (480, KD 16)."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bb import Page, payload
POST_ID = int(os.environ.get("POST_ID", "872"))
p = Page()

# 1. Hero
hero = p.row(bg="ink", cls="ja26-root ja-dark", pad=(120, 112), pad_mobile=(64, 64))
(h,) = hero.cols(100)
h.heading("SEO &amp; AI Search <em>Audit</em>", tag="h1", mb=28, cls="ja-measure")
h.text("<p>A senior SEO audit service that also checks how your company shows up inside ChatGPT, Perplexity, Gemini "
       "and Google's AI Overviews. Delivered in 24 to 72 hours, with a walkthrough of every finding and a prioritised "
       "90-day plan your team can act on.</p>", cls="ja-lead", mb=40)
h.button("Book your audit", "/contact/", inline=True)
h.button("See all consulting", "/consulting/", ghost=True, inline=True)

# 2. Quick facts strip
facts = p.row(bg="stone", cls="ja-recognition", pad=(56, 56), pad_mobile=(40, 24))
for col, (t, s) in zip(facts.cols(25, 25, 25, 25, gap=40, cls="ja-hair"), [
    ("24 to 72 hours", "Delivery, longer for large sites"),
    ("Google + AI search", "Both audited together"),
    ("Walkthrough included", "Every finding explained"),
    ("90-day plan", "Prioritised by impact"),
]):
    col.heading(t, tag="h3", mb=8)
    col.text(f"<p>{s}</p>", cls="ja-caption")

# 3. Why a combined audit
why = p.row(bg="stone", pad=(56, 112), pad_mobile=(40, 64))
a, b = why.cols(50, 50, gap=64)
a.heading("Why audit Google and AI search together", tag="h2", mb=24)
a.text("<p>A classic SEO audit tells you why you don't rank. It doesn't tell you why ChatGPT recommends your competitor, "
       "or why Google's AI Overview answers your buyer's question without mentioning you.</p>"
       "<p>Both depend on the same foundations: a site search engines can crawl, content that answers real questions with "
       "evidence, and clear signals about who you are. So I audit them as one system and give you one plan.</p>")
b.heading("Who it's for", tag="h3", mb=16)
b.text("<ul>"
       "<li>B2B, SaaS, pharmaceutical, healthcare and professional services companies</li>"
       "<li>Founders and marketing leaders who need a clear, senior view before they spend more</li>"
       "<li>Teams whose traffic is flat or falling as AI answers take the clicks</li>"
       "<li>Companies planning a redesign, migration or new content programme</li>"
       "</ul>", cls="ja-list")

# 4. What the audit covers
cov = p.row(bg="graphite", cls="ja-dark", pad=(112, 112), pad_mobile=(64, 64))
(ch,) = cov.cols(100)
ch.heading("What the audit covers", tag="h2", mb=48)
for title, items in [
    ("Technical SEO", ["Crawling, indexing and canonical issues", "Site architecture and internal linking",
                       "Core Web Vitals and mobile speed", "Structured data and schema"]),
    ("AI search visibility", ["Where you are cited in AI answers, and where competitors are",
                              "The questions buyers ask AI tools in your market", "Entity clarity: how AI understands your brand",
                              "Sources AI engines trust in your niche"]),
    ("Content and authority", ["Pages that rank, decline or cannibalise each other", "Evidence, expertise and trust gaps",
                               "Topic and keyword gaps against competitors", "Backlink profile and toxic link risk"]),
    ("Competitors and demand", ["Who wins your keywords on Google and in AI answers", "Search demand and where it is moving",
                                "Quick wins already close to page one", "Opportunities ranked by revenue potential"]),
]:
    l, r = cov.cols(45, 55, gap=64, cls=["ja-hair", "ja-hair"])
    l.heading(title, tag="h3", mb=40)
    r.text("<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>", cls="ja-list", mb=40)

# 5. Deliverables
dv = p.row(bg="stone", pad=(112, 64), pad_mobile=(64, 40))
(dh,) = dv.cols(100)
dh.heading("What you get", tag="h2", mb=48)
for col, (t, body) in zip(dv.cols(33, 34, 33, gap=48, cls="ja-rule"), [
    ("The audit report", "Every issue and opportunity, with evidence, severity and the fix, written for decision makers and the people who implement."),
    ("A walkthrough of the findings", "I take you through the audit step by step, explain what matters most and answer your team's questions."),
    ("A prioritised 90-day plan", "What to fix first, what to build next and what each step should return, ordered by impact and effort."),
]):
    col.heading(t, tag="h3", mb=12)
    col.text(f"<p>{body}</p>")

# 6. How it works
hw = p.row(bg="stone", pad=(64, 112), pad_mobile=(40, 64))
(hh,) = hw.cols(100)
hh.heading("How it works", tag="h2", mb=48)
for col, (step, title, body) in zip(hw.cols(25, 25, 25, 25, gap=40, cls="ja-rule"), [
    ("Step 1", "Short call", "We agree goals, markets and competitors. You get a fixed quote before any work starts."),
    ("Step 2", "Access", "You share read access to Google Search Console and Google Analytics. Nothing else is required."),
    ("Step 3", "Audit", "Delivered in 24 to 72 hours. Large or multi-market sites can take longer, and I'll tell you upfront."),
    ("Step 4", "Walkthrough and plan", "We go through the findings together and agree the 90-day plan."),
]):
    col.heading(step, tag="h4", cls="ja-step", mb=10)
    col.heading(title, tag="h3", mb=10)
    col.text(f"<p>{body}</p>")

# 7. Pricing: what sets the price (left) and a card of what every audit includes (right)
pr = p.row(bg="ink", cls="ja-dark ja-pricing", pad=(112, 112), pad_mobile=(64, 64))
pl, pc = pr.cols(50, 50, align="center", gap=80, cls=["", "ja-price-card"])
pl.heading("Pricing", tag="h2", mb=20)
pl.text("<p>You pay for the depth your business needs, not a one-size package. Every audit gets a fixed price "
        "after a short call, before any work starts.</p>", cls="ja-lead", mb=36)
pl.heading("What sets the price", tag="h3", mb=16)
pl.text("<ul>"
        "<li>Size of the site: pages, templates and subdomains</li>"
        "<li>Number of markets and languages</li>"
        "<li>How many competitors we benchmark</li>"
        "<li>How deep the AI search analysis goes</li>"
        "</ul>", cls="ja-list")
pc.heading("Every audit includes", tag="h3", mb=20)
pc.text("<ul>"
        "<li>Google and AI search audited together</li>"
        "<li>Written report with evidence and fixes</li>"
        "<li>Walkthrough of every finding</li>"
        "<li>Prioritised 90-day plan</li>"
        "<li>Delivery in 24 to 72 hours</li>"
        "<li>Fixed price, no retainer</li>"
        "</ul>", cls="ja-list ja-checks", mb=32)
pc.button("Get your fixed quote", "/contact/")

# 8. FAQ
FAQ = [
    ("What is an SEO audit service?",
     "An SEO audit service is a structured review of your website's technical health, content and authority that explains why it does or doesn't rank, and what to fix first. Mine also covers AI search."),
    ("What is an AI search audit?",
     "An AI search audit checks how AI assistants such as ChatGPT, Perplexity, Gemini and Google's AI Overviews describe and cite your company and your competitors, and what content and signals would get you cited more often."),
    ("How long does the audit take?",
     "Usually 24 to 72 hours after I receive access. Large or multi-market sites can take longer, and you'll know the timeline before we start."),
    ("What access do you need?",
     "Read access to Google Search Console and Google Analytics. Access to your CMS isn't needed for the audit."),
    ("How much does an SEO and AI search audit cost?",
     "It depends on site size, markets and goals. You get a fixed quote after a short call, before any work begins."),
    ("Can you implement the fixes?",
     "Yes. Your team can run the plan, I can advise them, or my company Reinforce Lab can implement it end to end."),
]
qa = p.row(bg="stone", cls="ja-faq", pad=(112, 112), pad_mobile=(64, 64))
(qh,) = qa.cols(100)
qh.heading("Frequently Asked Questions (FAQs)", tag="h2", cls="ja-faq-title", mb=48)
for q, ans in FAQ:
    (qc,) = qa.cols(100, cls="ja-qa")
    qc.heading(q, tag="h3", mb=10)
    qc.text(f"<p>{ans}</p>", mb=32)
schema = {"@context": "https://schema.org", "@graph": [
    {"@type": "Service", "name": "SEO & AI Search Audit", "serviceType": "SEO audit",
     "description": "A senior SEO audit service covering Google and AI search (ChatGPT, Perplexity, Gemini, Google AI Overviews), delivered in 24 to 72 hours with a walkthrough and a prioritised 90-day plan.",
     "provider": {"@type": "Person", "name": "Jamil Ahmed", "url": "https://jamilahmed.com/"},
     "areaServed": "Worldwide", "url": "https://jamilahmed.com/seo-ai-search-audit/"},
    {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]},
]}
qc.text('<script type="application/ld+json">' + json.dumps(schema) + '</script>', mb=0)

# 9. Closing CTA: graphite band with brass rule (separates it from the ink footer), headline left, next steps right
cta = p.row(bg="graphite", cls="ja-dark ja-closing", pad=(112, 112), pad_mobile=(64, 64))
cl, cr = cta.cols(55, 45, align="center", gap=80)
cl.heading("Find out what's holding you back on Google <em>and</em> in AI answers", tag="h2", mb=24)
cl.text("<p>Tell me about your company. You'll get a fixed quote and a delivery date, and if an audit isn't the right "
        "first step, I'll tell you.</p>", cls="ja-lead", mb=40)
cl.button("Book your audit", "/contact/", inline=True)
cl.button("See all consulting", "/consulting/", ghost=True, inline=True)
cr.heading("What happens next", tag="h3", mb=20)
cr.text("<ol class=\"ja-next\">"
        "<li><strong>Send a short brief</strong><span>Your site, markets and goals. It takes two minutes.</span></li>"
        "<li><strong>Short call and fixed quote</strong><span>We agree scope, competitors and timeline.</span></li>"
        "<li><strong>Audit and walkthrough</strong><span>Delivered in 24 to 72 hours, then we go through it together.</span></li>"
        "</ol>", cls="ja-next-wrap")

if __name__ == "__main__":
    print(payload(POST_ID, p))
