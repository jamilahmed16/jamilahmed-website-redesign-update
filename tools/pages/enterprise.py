"""Enterprise SEO Consultant service page (/enterprise-seo-consultant/, post 873).
Target: enterprise seo consultant (2,400, KD 18, CPC $49.27)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import payload
from _service import build

POST_ID = int(os.environ.get("POST_ID", "873"))

ART = ('<div class="ja-art ja-art-matrix" aria-hidden="true">'
       '<p class="ja-art-k">Priority matrix</p>'
       '<div class="ja-mx">'
       '<span class="ja-mx-y">Impact</span><span class="ja-mx-x">Effort</span>'
       '<div class="ja-mx-q q1"><b>Do first</b><i>Fix canonical chains on category templates</i><i>Allow AI search crawlers</i></div>'
       '<div class="ja-mx-q q2"><b>Plan</b><i>Merge duplicate regional pages</i></div>'
       '<div class="ja-mx-q q3"><b>Quick fixes</b><i>Missing titles on 1,200 URLs</i></div>'
       '<div class="ja-mx-q q4"><b>Park</b><i>Rebuild faceted navigation</i></div>'
       '</div></div>')


def unique(p):
    """Migrations: a timeline that carries information (when each check happens)."""
    r = p.row(bg="stone", pad=(112, 56), pad_mobile=(64, 40))
    (h,) = r.cols(100)
    h.heading("Migrations without losing rankings", tag="h2", mb=16)
    h.text("<p>A replatform or redesign is where large sites lose the most search traffic, usually in the first "
           "month. This is how I run one with your teams.</p>", cls="ja-lead", mb=48)
    for col, (when, what) in zip(r.cols(25, 25, 25, 25, gap=40, cls="ja-rule"), [
        ("Before launch", "URL inventory, redirect map, template checks on staging, and a benchmark of current "
                          "rankings, traffic and AI citations."),
        ("Launch week", "Redirects verified, a full crawl of the live site, and Search Console and server logs "
                        "checked for errors."),
        ("First 30 days", "Indexing, rankings and traffic tracked by template, with fixes ranked as issues appear."),
        ("By day 90", "Recovery confirmed against the benchmark, and the lessons written into your release process."),
    ]):
        col.heading(when, tag="h3", mb=12)
        col.text(f"<p>{what}</p>")


SPEC = {
    "path": "/enterprise-seo-consultant/",
    "h1": "Enterprise SEO <em>Consultant</em>",
    "lead": "Senior SEO and AI search consulting for large, complex and regulated websites. I set the priorities "
            "leadership can sign off, and help product, engineering and content teams ship them without breaking what "
            "already ranks.",
    "art": ART,
    "art_caption": "Example: how findings are ranked on a large site.",
    "intro_h2": "Enterprise SEO is a coordination problem",
    "intro": ["On a large site, the hard part is rarely knowing what to fix. It's getting product, engineering, "
              "content, legal and regional teams to fix the right things in the right order.",
              "I bring a senior outside view, a ranked plan leadership can approve, and changes written so your teams "
              "can ship them through normal release cycles."],
    "signs_h3": "Signs you need outside help",
    "signs": ["Organic traffic is flat or falling while AI Overviews answer your buyers' questions",
              "Competitors are named in ChatGPT and Perplexity, and your brand isn't",
              "A migration, replatform or redesign is on the roadmap",
              "Several markets, languages or business units compete for the same keywords",
              "SEO reports talk about rankings while leadership asks about revenue"],
    "help_h2": "Where I help enterprise teams",
    "help": [
        ("Strategy and governance", "What to own in search by product, market and audience, and SEO requirements built "
                                    "into how product and engineering already work."),
        ("Technical SEO at scale", "Crawl budget, indexing and duplicate content across very large URL sets, plus "
                                   "templates, internal linking and JavaScript rendering."),
        ("International SEO", "Market and language structure, hreflang, and stopping regions and business units from "
                              "competing for the same searches."),
        ("AI search visibility", "How ChatGPT, Perplexity, Gemini and AI Overviews describe your brand, and the "
                                 "entity, structured data and evidence work that gets you cited."),
        ("Reporting leadership trusts", "Search reporting tied to pipeline and revenue, with a short list of measures "
                                        "the board can follow."),
        ("Regulated content", "Evidence-led content and workflows that pass medical, legal and compliance review."),
    ],
    "unique": unique,
    "price_intro": "Enterprise work is scoped to your sites, markets and teams. After a short call you get a written "
                   "proposal with a fixed price.",
    "ways": [("SEO &amp; AI Search Audit", 'A senior diagnostic of the whole site and a ranked plan. '
              '<a href="/seo-ai-search-audit/">What the audit includes</a>'),
             ("Executive advisory", "Monthly sessions with leadership and in-house teams, and reviews of agency and team work."),
             ("Implementation with Reinforce Lab", "When the plan needs more hands, my company Reinforce Lab delivers it.")],
    "faq": [
        ("What does an enterprise SEO consultant do?",
         "An enterprise SEO consultant sets search strategy for large or complex websites, finds the technical, content "
         "and authority issues that limit growth at scale, and helps in-house teams, agencies and engineering "
         "prioritise and ship fixes."),
        ("How is enterprise SEO different from regular SEO?",
         "Scale and coordination. Enterprise sites have more pages, markets, stakeholders and release processes, so the "
         "work is as much about governance and prioritisation as about individual fixes."),
        ("Do you replace our SEO agency or in-house team?",
         "No. I usually work alongside them, setting direction and reviewing work. If you need more capacity, my "
         "company Reinforce Lab can implement."),
        ("Can you help with a site migration?",
         "Yes. I plan the redirect map and pre-launch checks with your teams, monitor the launch, and track recovery "
         "against a benchmark taken before the move."),
        ("Do you work with regulated industries?",
         "Yes. My background is in pharmaceuticals, including Janssen (Johnson &amp; Johnson), so evidence-led content "
         "and compliance review are familiar ground."),
        ("How do we start?",
         "Book a consultation. Most enterprise engagements start with the SEO &amp; AI Search Audit."),
    ],
    "service_name": "Enterprise SEO consulting", "service_type": "Enterprise SEO consulting",
    "service_desc": "Senior enterprise SEO consulting for large, complex and regulated websites, covering Google and AI search.",
    "close_h2": "Make search a revenue channel your board <em>understands</em>",
    "close_text": "Tell me about your sites, markets and what leadership expects from search, and I'll recommend where to start.",
    "steps": [("Send a short brief", "Your sites, markets and what you need from search."),
              ("Call and proposal", "We agree scope, stakeholders and timeline."),
              ("Audit or kickoff", "Most engagements start with the audit, then a plan your teams can ship.")],
}

if __name__ == "__main__":
    print(payload(POST_ID, build(SPEC)))
