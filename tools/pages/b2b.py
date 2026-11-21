"""B2B & SaaS SEO Consultant service page (/b2b-saas-seo-consultant/, post 874).
Targets: b2b seo consultant (1,600, KD 8), saas seo consultant (1,600, KD 9),
fractional seo consultant (210, KD 7), seo consultant for startups (50)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import payload
from _service import build

POST_ID = int(os.environ.get("POST_ID", "874"))

ART = ('<div class="ja-art ja-art-chat" aria-hidden="true">'
       '<p class="ja-art-k">Fictional example</p>'
       '<p class="ja-art-q">Which customer success platforms should a 200-person SaaS company shortlist?</p>'
       '<p class="ja-art-ans">For a team that size, three platforms come up most often in reviews and comparisons: '
       'Northpeak, Tallyfield and Brightloop. Northpeak is strongest on onboarding playbooks...</p>'
       '<ul class="ja-art-src"><li><span>1</span>Northpeak: comparison page</li><li><span>2</span>G2 category report</li>'
       '<li class="you"><span>3</span>Is your company cited here?</li></ul></div>')


def unique(p):
    """The B2B buying journey mapped to searches and the pages that should answer them."""
    r = p.row(bg="stone", pad=(112, 56), pad_mobile=(64, 40))
    (h,) = r.cols(100)
    h.heading("The buying journey, mapped to search", tag="h2", mb=16)
    h.text("<p>Each stage of a B2B purchase has its own searches and AI questions. Most SaaS sites only answer the "
           "last one. This is the map I build with you, using your category's real queries.</p>", cls="ja-lead", mb=40)
    h.text('<table class="ja-table"><thead><tr><th>Stage</th><th>What buyers search or ask AI</th>'
           '<th>The page that should answer</th></tr></thead><tbody>'
           '<tr><td>Problem</td><td>"how to reduce churn in B2B SaaS"</td><td>A guide built on your own data and expertise</td></tr>'
           '<tr><td>Category</td><td>"best customer success platforms"</td><td>A category page and honest comparison content</td></tr>'
           '<tr><td>Shortlist</td><td>"Northpeak vs Tallyfield", "Northpeak alternatives"</td><td>Comparison and alternatives pages</td></tr>'
           '<tr><td>Validation</td><td>"pricing", "reviews", "does it integrate with HubSpot"</td><td>Pricing, integration and proof pages</td></tr>'
           '</tbody></table>', cls="ja-table-wrap")


SPEC = {
    "path": "/b2b-saas-seo-consultant/",
    "h1": "B2B &amp; SaaS SEO <em>Consultant</em>",
    "lead": "Your buyers research for weeks and ask ChatGPT for a shortlist before they book a demo. I help B2B and "
            "SaaS companies show up at each step of that research, on Google and in AI answers, and connect it to "
            "pipeline.",
    "art": ART,
    "art_caption": "Fictional brands. Buyers now ask AI for a vendor shortlist, and the answer cites its sources.",
    "intro_h2": "Most buyers never search your brand name first",
    "intro": ["Most B2B and SaaS buyers never search your brand name first. They search the problem, compare "
              "categories, read alternatives pages and ask AI assistants for a shortlist. If you only rank for your "
              "own name, you meet buyers after the decision is half made.",
              "I build search around the buying committee: the questions each role asks, the comparisons they make "
              "and the proof they need."],
    "signs_h3": "Signs you need a B2B SEO consultant",
    "signs": ["Traffic grows but demo requests and trials don't",
              "Competitors own the \"best\", \"alternatives\" and \"vs\" searches in your category",
              "ChatGPT and Perplexity recommend other vendors when buyers ask",
              "Content goes out every week and nobody can link it to pipeline",
              "You need senior SEO leadership before you can justify a full-time hire"],
    "help_h2": "Where I help B2B and SaaS teams",
    "help": [
        ("Strategy tied to pipeline", "Keywords mapped to buyer stage and role, ranked by likely pipeline value, with "
                                      "reporting that connects organic and AI traffic to demos and deals."),
        ("Comparison and alternatives pages", "The \"vs\", \"alternatives\" and \"best\" pages buyers read when they "
                                              "build a shortlist, written so they rank and stay credible."),
        ("AI shortlist visibility", "How ChatGPT, Perplexity, Gemini and AI Overviews shortlist vendors in your category, "
                                    "and the reviews, comparisons and data they cite."),
        ("Content that earns authority", "Thought leadership built on your own data and expertise, in topic clusters "
                                         "that support your product pages."),
        ("Technical SEO for SaaS sites", "JavaScript rendering, app and marketing site structure, docs and help centre "
                                         "subdomains, speed and indexing."),
        ("Fractional SEO leadership", "Part-time senior direction for your writers, developers and agencies, for teams "
                                      "that aren't ready for a full-time SEO lead."),
    ],
    "unique": unique,
    "brief_need": "b2b",
    "order": ['hero', 'creds', 'unique', 'intro', 'help', 'pricing_short', 'faq', 'close'],
    "close_h2": 'Be on the shortlist <em>before</em> the demo request',
    "close_text": "Send me your category and the three competitors you lose deals to most often. I'll show you where they are cited in AI answers and you aren't.",
    "price_intro": "Every engagement is scoped to your stage, market and goals. After a short call you get a written "
                   "proposal with a fixed price.",
    "ways": [("SEO &amp; AI Search Audit", 'A senior diagnostic of your site and category, with a ranked plan. '
              '<a href="/seo-ai-search-audit/">What the audit includes</a>'),
             ("Fractional SEO lead", "Part-time senior SEO leadership for startups and scale-ups that aren't ready for a "
                                     "full-time hire."),
             ("Implementation with Reinforce Lab", "When you need execution too, my company Reinforce Lab delivers the plan.")],
    "faq": [
        ("What does a B2B SEO consultant do?",
         "A B2B SEO consultant builds search strategy around how business buyers research: problem searches, category "
         "comparisons, alternatives and AI shortlists. The goal is qualified pipeline."),
        ("What does a SaaS SEO consultant do differently?",
         "SaaS SEO focuses on comparison, alternatives, integration and use case pages, product-led content, and "
         "technical issues common to SaaS sites such as JavaScript rendering and docs subdomains."),
        ("What is a fractional SEO consultant?",
         "A fractional SEO consultant gives you senior SEO leadership part-time: strategy, priorities and direction for "
         "your team and agencies, without the cost of a full-time hire."),
        ("Do you work with startups?",
         "Yes. Early-stage companies usually start with the audit or a fractional engagement, so the first pages target "
         "the searches most likely to produce customers."),
    ],
    "service_name": "B2B and SaaS SEO consulting", "service_type": "B2B SEO consulting",
    "service_desc": "SEO and AI search consulting for B2B and SaaS companies, focused on pipeline: buyer-journey strategy, "
                    "comparison and alternatives pages, AI visibility and fractional SEO leadership.",
}

if __name__ == "__main__":
    print(payload(POST_ID, build(SPEC)))
