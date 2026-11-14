"""Pharma & Healthcare SEO Consultant service page (/pharma-healthcare-seo/, post 875).
Targets: healthcare seo consultant (1,600, KD 17), pharma seo (390, KD 24), pharmaceutical seo (320, KD 17)."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bb import Page, payload
POST_ID = int(os.environ.get("POST_ID", "875"))
p = Page()

# 1. Hero
hero = p.row(bg="ink", cls="ja26-root ja-dark", pad=(120, 112), pad_mobile=(64, 64))
(h,) = hero.cols(100)
h.heading("Pharma &amp; Healthcare SEO <em>Consultant</em>", tag="h1", mb=28, cls="ja-measure")
h.text("<p>Pharmaceutical SEO and healthcare SEO from someone who worked inside the industry. I help pharma, life "
       "sciences and healthcare companies become the trusted source on Google and in AI answers, with content that "
       "passes medical, legal and regulatory review.</p>", cls="ja-lead", mb=40)
h.button("Book a consultation", "/contact/", inline=True)
h.button("Start with an audit", "/seo-ai-search-audit/", ghost=True, inline=True)

# 2. Facts strip
facts = p.row(bg="stone", cls="ja-recognition", pad=(56, 56), pad_mobile=(40, 24))
for col, (t, s) in zip(facts.cols(25, 25, 25, 25, gap=40, cls="ja-hair"), [
    ("Pharma insider", "Janssen and international pharma"),
    ("Evidence first", "Every claim needs a source"),
    ("Review-ready", "Built for MLR and compliance"),
    ("Google + AI search", "Where patients and HCPs ask"),
]):
    col.heading(t, tag="h3", mb=8)
    col.text(f"<p>{s}</p>", cls="ja-caption")

# 3. Why pharma/healthcare SEO is different
why = p.row(bg="stone", pad=(56, 112), pad_mobile=(40, 64))
a, b = why.cols(50, 50, gap=64)
a.heading("Health search holds you to a higher standard", tag="h2", mb=24)
a.text("<p>Google treats health as \"Your Money or Your Life\" content: pages that can affect someone's health are held "
       "to the highest bar for expertise, accuracy and trust. AI assistants are just as cautious about which health "
       "sources they cite.</p>"
       "<p>At the same time, every word on a pharma or healthcare site may need medical, legal and regulatory sign-off. "
       "Generic SEO advice breaks on both counts. The work has to be evidence-led from the start and planned around "
       "your review process, not against it.</p>")
b.heading("Who I work with", tag="h3", mb=16)
b.text("<ul>"
       "<li>Pharmaceutical and biotech companies, including export-driven and multi-market brands</li>"
       "<li>Life sciences, medical device and diagnostics companies</li>"
       "<li>Healthcare providers, clinics and digital health platforms</li>"
       "<li>Health information publishers and B2B healthcare SaaS</li>"
       "</ul>", cls="ja-list")

# 4. What I help with
cov = p.row(bg="graphite", cls="ja-dark", pad=(112, 112), pad_mobile=(64, 64))
(ch,) = cov.cols(100)
ch.heading("What I help pharma and healthcare teams with", tag="h2", mb=48)
for title, items in [
    ("Expertise and trust (E-E-A-T)", ["Author, reviewer and organisation signals Google and AI engines look for",
                                       "Medical reviewer bylines, references and update dates",
                                       "Clear entity information about your company, products and people"]),
    ("Evidence-led content", ["Topics planned around real patient, caregiver and HCP questions",
                              "Every claim referenced to a credible source",
                              "Separate journeys for patients and healthcare professionals"]),
    ("Review-ready workflows", ["Briefs and drafts structured for medical, legal and regulatory (MLR) review",
                                "Fewer review rounds, because sources come with the draft",
                                "Update plans for content that goes out of date"]),
    ("AI search visibility", ["How ChatGPT, Perplexity, Gemini and AI Overviews answer questions about your condition areas",
                              "Being cited as the trusted source, not paraphrased without credit",
                              "Correcting outdated or wrong information AI repeats about your brand"]),
    ("Technical and international SEO", ["Product, condition and HCP site structure",
                                         "Multi-market and multi-language sites",
                                         "Gated HCP areas, PDFs and scientific content that search engines can't read"]),
    ("Local healthcare SEO", ["Google Business Profiles and location pages for clinics and providers",
                              "Reviews and reputation", "Service pages patients actually search for"]),
]:
    l, r = cov.cols(40, 60, gap=64, cls=["ja-hair", "ja-hair"])
    l.heading(title, tag="h3", mb=40)
    r.text("<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>", cls="ja-list", mb=40)

# 5. Ways to work
ww = p.row(bg="stone", pad=(112, 64), pad_mobile=(64, 40))
(wh,) = ww.cols(100)
wh.heading("Ways to work together", tag="h2", mb=48)
for col, (t, body, link) in zip(ww.cols(33, 34, 33, gap=48, cls="ja-rule"), [
    ("SEO &amp; AI Search Audit", "A senior diagnostic of your site, condition areas and competitors, delivered in 24 to 72 hours with a walkthrough and a prioritised 90-day plan.",
     '<a href="/seo-ai-search-audit/">See what the audit includes</a>'),
    ("Fractional SEO lead", "Part-time senior SEO leadership that works with your medical, regulatory and brand teams, without a full-time hire.", ""),
    ("Full build with Reinforce Lab", "When you need execution, my company Reinforce Lab delivers the plan: SEO, AI search, evidence-verified content and automation.", ""),
]):
    col.heading(t, tag="h3", mb=12)
    col.text(f"<p>{body}</p>" + (f"<p>{link}</p>" if link else ""))

# 6. Why me
wm = p.row(bg="stone", pad=(64, 112), pad_mobile=(40, 64))
ml, mr = wm.cols(40, 60, gap=80)
ml.heading("Why work with me", tag="h2", mb=24)
mr.text("<ul>"
        "<li><strong>A pharmacist who worked inside the industry.</strong> Product Manager, Immunology at Janssen (Johnson &amp; Johnson), International Marketing at Square Group and International Business at Beacon Pharmaceuticals.</li>"
        "<li><strong>Regulated, export-driven markets.</strong> I've worked where every claim needs evidence and every market has its own rules.</li>"
        "<li><strong>Founder &amp; CEO of Reinforce Lab</strong>, an AI growth company since 2018, and a Semrush Ambassador.</li>"
        "<li><strong>Google and AI search together</strong>, so your teams follow one plan.</li>"
        "</ul>", cls="ja-list")

# 7. Pricing
pr = p.row(bg="ink", cls="ja-dark ja-pricing", pad=(112, 112), pad_mobile=(64, 64))
pl, pc = pr.cols(50, 50, align="center", gap=80, cls=["", "ja-price-card"])
pl.heading("Pricing", tag="h2", mb=20)
pl.text("<p>Every engagement is scoped to your products, markets and review process. You get a fixed proposal after a "
        "short call, before any work starts.</p>", cls="ja-lead", mb=36)
pl.heading("What shapes the scope", tag="h3", mb=16)
pl.text("<ul>"
        "<li>Number of brands, condition areas and markets</li>"
        "<li>Patient, HCP or B2B audiences</li>"
        "<li>One-off audit, fractional lead or ongoing advisory</li>"
        "<li>Advice only, or implementation with Reinforce Lab</li>"
        "</ul>", cls="ja-list")
pc.heading("Every engagement includes", tag="h3", mb=20)
pc.text("<ul>"
        "<li>Direct access to me, not a junior team</li>"
        "<li>Google and AI search in one strategy</li>"
        "<li>Evidence-led, review-ready recommendations</li>"
        "<li>Priorities ranked by business impact</li>"
        "<li>Plans your teams can ship</li>"
        "<li>Fixed scope before work starts</li>"
        "</ul>", cls="ja-list ja-checks", mb=32)
pc.button("Request a proposal", "/contact/")

# 8. FAQ
FAQ = [
    ("What is pharma SEO?",
     "Pharma SEO is search engine optimization for pharmaceutical and life sciences companies. It works within regulatory and compliance limits and focuses on evidence, expertise and trust, because Google holds health content to its highest quality standards."),
    ("What does a healthcare SEO consultant do?",
     "A healthcare SEO consultant helps providers, health platforms and health brands rank for the questions patients and professionals search, with accurate, well-sourced content and strong expertise and trust signals."),
    ("Can SEO work within MLR and compliance review?",
     "Yes. I plan topics, briefs and drafts so sources travel with the content, which makes medical, legal and regulatory review faster. I don't replace your reviewers; I make their job easier."),
    ("Do you cover AI search for health topics?",
     "Yes. I check how ChatGPT, Perplexity, Gemini and Google's AI Overviews answer questions in your condition areas, which sources they cite, and what it takes for your content to become one of them."),
    ("Do you work with healthcare providers and clinics?",
     "Yes, including local SEO: Google Business Profiles, location and service pages, and reviews."),
    ("How do we start?",
     "Book a consultation. Most pharma and healthcare clients start with the SEO &amp; AI Search Audit, which gives you a prioritised 90-day plan."),
]
qa = p.row(bg="stone", cls="ja-faq", pad=(112, 112), pad_mobile=(64, 64))
(qh,) = qa.cols(100)
qh.heading("Frequently Asked Questions (FAQs)", tag="h2", cls="ja-faq-title", mb=48)
for q, ans in FAQ:
    (qc,) = qa.cols(100, cls="ja-qa")
    qc.heading(q, tag="h3", mb=10)
    qc.text(f"<p>{ans}</p>", mb=32)
schema = {"@context": "https://schema.org", "@graph": [
    {"@type": "Service", "name": "Pharma and healthcare SEO consulting", "serviceType": "Healthcare SEO consulting",
     "description": "SEO and AI search consulting for pharmaceutical, life sciences and healthcare companies: E-E-A-T, evidence-led and review-ready content, AI visibility and local healthcare SEO.",
     "provider": {"@type": "Person", "name": "Jamil Ahmed", "url": "https://jamilahmed.com/"},
     "areaServed": "Worldwide", "url": "https://jamilahmed.com/pharma-healthcare-seo/"},
    {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a.replace("&amp;", "&")}} for q, a in FAQ]},
]}
qc.text('<script type="application/ld+json">' + json.dumps(schema) + '</script>', mb=0)

# 9. Closing CTA
cta = p.row(bg="graphite", cls="ja-dark ja-closing", pad=(112, 112), pad_mobile=(64, 64))
cl, cr = cta.cols(55, 45, align="center", gap=80)
cl.heading("Become the source patients and doctors <em>trust</em>", tag="h2", mb=24)
cl.text("<p>Tell me about your products, markets and review process. You'll get a clear recommendation and a fixed "
        "proposal, and if I'm not the right fit, I'll say so.</p>", cls="ja-lead", mb=40)
cl.button("Book a consultation", "/contact/", inline=True)
cl.button("Start with an audit", "/seo-ai-search-audit/", ghost=True, inline=True)
cr.heading("What happens next", tag="h3", mb=20)
cr.text("<ol class=\"ja-next\">"
        "<li><strong>Send a short brief</strong><span>Your products, audiences and markets.</span></li>"
        "<li><strong>Call and proposal</strong><span>We agree scope, review process and timeline.</span></li>"
        "<li><strong>Audit or kickoff</strong><span>Usually the audit first, then a 90-day plan your teams can ship.</span></li>"
        "</ol>", cls="ja-next-wrap")

if __name__ == "__main__":
    print(payload(POST_ID, p))
