"""SEO & AI Search Audit service page (/seo-ai-search-audit/, post 872).
Targets: seo audit service (3,600, KD 26), ai search audit (480, KD 16)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import payload
from _service import build

POST_ID = int(os.environ.get("POST_ID", "872"))

ART = ('<div class="ja-art ja-art-doc" aria-hidden="true">'
       '<p class="ja-art-k">SEO &amp; AI Search Audit</p><p class="ja-art-t">Your company</p>'
       '<ol class="ja-art-toc"><li>Summary and priorities</li><li>Technical SEO</li><li>AI search visibility</li>'
       '<li>Content and authority</li><li>Competitors and demand</li><li>90-day plan</li></ol></div>')


def unique(p):
    """How each finding is written: the format, with one example."""
    r = p.row(bg="stone", cls="ja-finding-row", pad=(112, 56), pad_mobile=(64, 40))
    l, c = r.cols(45, 55, align="center", gap=72)
    l.heading("Every finding comes with the fix", tag="h2", mb=24)
    l.text("<p>Audits fail when they hand a team 200 warnings and no order. Each finding in the report says what is "
           "wrong, the evidence, how much it matters, how hard it is to fix, and who should fix it. Findings are then "
           "ranked into the 90-day plan.</p>"
           "<p>The example on the right shows the format. It is illustrative, not taken from a client report.</p>")
    c.text('<div class="ja-art ja-art-finding">'
           '<p class="ja-art-k">Example finding</p>'
           '<p class="ja-art-t">Product pages can\'t be cited in ChatGPT search</p>'
           '<dl>'
           '<dt>Evidence</dt><dd>robots.txt blocks OAI-SearchBot on /products/, so ChatGPT search can\'t read those pages.</dd>'
           '<dt>Impact</dt><dd><span class="ja-pill ja-pill-hi">High</span> Product questions are answered with competitor pages.</dd>'
           '<dt>Effort</dt><dd><span class="ja-pill">Low</span> One rule in robots.txt.</dd>'
           '<dt>Fix</dt><dd>Allow OAI-SearchBot on public product pages, then re-check the priority prompts after two weeks.</dd>'
           '<dt>Owner</dt><dd>Web developer</dd>'
           '</dl></div>', cls="ja-art-wrap ja-art-light")


SPEC = {
    "path": "/seo-ai-search-audit/",
    "h1": "SEO &amp; AI Search <em>Audit</em>",
    "lead": "A senior review of how your company shows up on Google and inside ChatGPT, Perplexity, Gemini and AI "
            "Overviews. You get a written report in 24 to 72 hours, a walkthrough of every finding, and a ranked plan "
            "your team can start on straight away.",
    "hero_secondary": ("See all consulting", "/consulting/"),
    "art": ART,
    "art_caption": "What you receive: one report in six sections.",
    "intro_h2": "Why audit Google and AI search together",
    "intro": ["A classic SEO audit tells you why you don't rank. It doesn't tell you why ChatGPT recommends your "
              "competitor, or why Google's AI Overview answers your buyer's question without mentioning you.",
              "Both depend on the same foundations: a site search engines can crawl, content that answers real "
              "questions with evidence, and clear signals about who you are. So I audit them as one system and give "
              "you one plan."],
    "signs_h3": "Who it's for",
    "signs": ["B2B, SaaS, pharmaceutical, healthcare and professional services companies",
              "Founders and marketing leaders who want a senior view before they spend more",
              "Teams whose traffic is flat or falling as AI answers take the clicks",
              "Companies planning a redesign, migration or new content programme"],
    "help_h2": "What the audit covers",
    "help": [
        ("Technical SEO", "Crawling, indexing, canonicals, site architecture, internal links, Core Web Vitals and "
                          "structured data: everything that decides whether search engines and AI crawlers can read your site."),
        ("AI search visibility", "Where ChatGPT, Perplexity, Gemini and AI Overviews cite you, where they cite "
                                 "competitors instead, and how they describe your brand."),
        ("Content and authority", "Which pages rank, which are slipping, where pages compete with each other, and "
                                  "where content lacks the evidence and expertise signals Google and AI look for."),
        ("Competitors and demand", "Who wins your most valuable searches and AI answers, where demand is moving, and "
                                   "the quick wins already close to page one."),
    ],
    "unique": unique,
    "price_intro": "The audit is quoted on the size of your site, the number of markets and how deep the AI search "
                   "analysis needs to go. You get a fixed price after a short call.",
    "ways": [("The audit on its own", "The report, the walkthrough and the 90-day plan. Your team takes it from there."),
             ("Audit, then advisory", "Monthly sessions to keep the plan on track and review what has shipped."),
             ("Audit, then implementation", "My company Reinforce Lab carries out the plan end to end.")],
    "faq": [
        ("What is an SEO audit service?",
         "An SEO audit service is a structured review of your website's technical health, content and authority that "
         "explains why it does or doesn't rank, and what to fix first. Mine also covers AI search."),
        ("What is an AI search audit?",
         "An AI search audit checks how AI assistants such as ChatGPT, Perplexity, Gemini and Google's AI Overviews "
         "describe and cite your company and your competitors, and what content and signals would get you cited more often."),
        ("How long does the audit take?",
         "Usually 24 to 72 hours after I receive access. Large or multi-market sites can take longer, and you'll know "
         "the timeline before we start."),
        ("What access do you need?",
         "Read access to Google Search Console and Google Analytics. Access to your CMS isn't needed for the audit."),
        ("How much does an SEO and AI search audit cost?",
         "It depends on site size, markets and goals. You get a fixed price in writing after a short call, before any "
         "work begins."),
        ("Can you implement the fixes?",
         "Yes. Your team can run the plan, I can advise them, or my company Reinforce Lab can implement it end to end."),
    ],
    "service_name": "SEO & AI Search Audit", "service_type": "SEO audit",
    "service_desc": "A senior SEO audit covering Google and AI search (ChatGPT, Perplexity, Gemini, Google AI "
                    "Overviews), delivered in 24 to 72 hours with a walkthrough and a ranked 90-day plan.",
    "close_h2": "Find out what's holding you back on Google <em>and</em> in AI answers",
    "close_text": "Tell me about your company and I'll come back with a fixed quote and a delivery date.",
    "close_secondary": ("See all consulting", "/consulting/", True),
    "steps": [("Send a short brief", "Your site, markets and goals. It takes two minutes."),
              ("Short call and fixed quote", "We agree scope, competitors and timeline."),
              ("Report and walkthrough", "Delivered in 24 to 72 hours, then we go through it together.")],
}

if __name__ == "__main__":
    print(payload(POST_ID, build(SPEC)))
