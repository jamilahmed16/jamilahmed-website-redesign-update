"""Consulting page (/consulting/)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _cta import closing_cta
from bb import Page, SITE, payload
UP = f"{SITE}/wp-content/uploads"
POST_ID = int(os.environ.get("POST_ID", "0"))
p = Page()

hero = p.row(bg="ink", cls="ja26-root ja-dark", pad=(120, 112), pad_mobile=(64, 64))
(h,) = hero.cols(100)
h.heading("SEO consulting for Google <em>and</em> AI search", tag="h1", mb=28, cls="ja-measure")
h.text("<p>Senior, hands-on SEO consulting services for founders, C-suite leaders, B2B and pharmaceutical companies that want to be found, "
       "cited and chosen. You work with me directly.</p>", cls="ja-lead", mb=40)
h.button("Book a consultation", "/contact/")

fit = p.row(bg="stone", pad=(112, 64), pad_mobile=(64, 40))
a, b = fit.cols(50, 50, gap=64)
a.heading("Who I work with", tag="h2", mb=24)
a.text("<p>Companies where a single new client is worth a lot, and where buyers do serious research before they talk to "
       "sales: pharmaceutical and life sciences, healthcare, B2B SaaS, manufacturing, technology, professional services and "
       "e-commerce brands.</p><p>Usually the founder or a C-suite leader is in the room, because search strategy now touches "
       "brand, content, product and revenue at once.</p>")
b.text("<ul>"
       "<li>Your organic traffic is flat, or falling as AI Overviews take the clicks</li>"
       "<li>Competitors are named in ChatGPT and Perplexity answers, and you are not</li>"
       "<li>You publish a lot of content but cannot tie it to pipeline</li>"
       "<li>A redesign or migration is coming and you cannot afford to lose rankings</li>"
       "<li>Your team runs reporting and research by hand every week</li>"
       "</ul>", cls="ja-list", mt=8)

eng = p.row(bg="graphite", cls="ja-dark", pad=(112, 112), pad_mobile=(64, 64))
(eh,) = eng.cols(100)
eh.heading("Engagements", tag="h2", mb=20)
eh.text('<p>Specialist services: <a href="/enterprise-seo-consultant/">Enterprise SEO consulting</a> , <a href="/b2b-saas-seo-consultant/">B2B &amp; SaaS SEO consulting</a> and <a href="/pharma-healthcare-seo/">Pharma &amp; healthcare SEO</a>.</p>', cls="ja-specialist", mb=48)
for title, desc, items in [
    ("SEO &amp; AI Search Audit",
     "A senior diagnostic of your visibility on Google and inside AI answers, delivered in 24 to 72 hours with a walkthrough and a prioritised 90-day plan. <a href=\"/seo-ai-search-audit/\">See what the audit includes</a>.",
     ["Technical SEO and site architecture review", "AI search visibility: where you are cited, and where competitors are",
      "Content authority and evidence gaps", "Competitor and demand analysis", "A 90-day action plan your team can run"]),
    ("Executive advisory",
     "Ongoing strategy for founders and leadership teams, month by month.",
     ["Monthly strategy sessions", "Priorities for SEO, AI search and content", "Automation opportunities with clear ROI",
      "Reporting tied to pipeline and revenue", "Review of agency and in-house work"]),
    ("Full build with Reinforce Lab",
     "When the plan needs a team, my company Reinforce Lab implements the complete AI Growth System.",
     ["SEO and AI search optimisation", "Evidence-verified content systems", "AI workflow and marketing automation",
      "Lead generation systems", "Executive dashboards"]),
]:
    l, r = eng.cols(45, 55, gap=64, cls=["ja-hair", "ja-hair"])
    l.heading(title, tag="h3", mb=12)
    l.text(f"<p>{desc}</p>", mb=40)
    r.text("<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>", cls="ja-list", mb=40)

hw = p.row(bg="stone", pad=(112, 112), pad_mobile=(64, 64))
(hh,) = hw.cols(100)
hh.heading("How it works", tag="h2", mb=48)
for col, (step, title, body) in zip(hw.cols(25, 25, 25, 25, gap=40, cls="ja-rule"), [
    ("Step 1", "Conversation", "A focused call about your goals, market and current results. If I am not the right fit, I will say so."),
    ("Step 2", "Diagnose", "I map your visibility on Google and in AI answers, your content and your competitors."),
    ("Step 3", "Plan", "You get a prioritised plan: what to fix, what to build, and what it should return."),
    ("Step 4", "Execute and measure", "Your team, or Reinforce Lab, executes. We track outcomes in pipeline, not rankings alone."),
]):
    col.heading(step, tag="h4", cls="ja-step", mb=10)
    col.heading(title, tag="h3", mb=10)
    col.text(f"<p>{body}</p>")

qa = p.row(bg="stone", cls="ja-faq", pad=(0, 112), pad_mobile=(0, 64))
(qh,) = qa.cols(100)
qh.heading("Frequently Asked Questions (FAQs)", tag="h2", cls="ja-faq-title", mb=48)
for q, ans in [
    ("What is AI Search Optimization?",
     "It is the work of making your company the source AI assistants such as ChatGPT, Perplexity, Gemini and Google's AI Overviews rely on and cite. It builds on SEO, and adds evidence, structure, entity clarity and authority signals that language models use."),
    ("Do you replace my SEO agency?",
     "Not necessarily. Many clients keep their agency or in-house team and use me for strategy, direction and review. Where a full team is needed, Reinforce Lab can deliver it."),
    ("Which industries do you know best?",
     "Pharmaceutical and life sciences, healthcare, B2B SaaS, manufacturing, technology, professional services and e-commerce. My background in pharma makes regulated, evidence-heavy markets a particular strength."),
    ("How do we start?",
     "Book a consultation. We talk through your goals and current results, and I recommend the right starting point, usually the <a href=\"/seo-ai-search-audit/\">SEO &amp; AI Search Audit</a>."),
]:
    (qc,) = qa.cols(100, cls="ja-qa")
    qc.heading(q, tag="h3", mb=10)
    qc.text(f"<p>{ans}</p>", mb=32)

# Closing call to action (shared style)
closing_cta(p, "Start with a <em>conversation</em>",
            "Tell me about your company and what you want search to do for it. If I'm not the right fit, I'll say so.",
            [("Book a consultation", "/contact/", False), ("Start with an audit", "/seo-ai-search-audit/", True)],
            "What happens next", [('Send a short brief', 'Your company, markets and goals.'), ('Short call', 'We agree what to fix first, scope and timeline.'), ('Audit or kickoff', 'Usually the audit first, then a 90-day plan your team can ship.')])

if __name__ == "__main__":
    print(payload(POST_ID, p))

