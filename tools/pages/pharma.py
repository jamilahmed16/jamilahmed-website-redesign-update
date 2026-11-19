"""Pharma & Healthcare SEO Consultant service page (/pharma-healthcare-seo/, post 875).
Targets: healthcare seo consultant (1,600, KD 17), pharma seo (390, KD 24), pharmaceutical seo (320, KD 17)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bb import payload
from _service import build

POST_ID = int(os.environ.get("POST_ID", "875"))

ART = ('<div class="ja-art ja-art-review" aria-hidden="true">'
       '<p class="ja-art-k">Fictional example</p><p class="ja-art-t">Managing eczema flare-ups at home</p>'
       '<dl>'
       '<dt>Written by</dt><dd>Sara Malik, health writer</dd>'
       '<dt>Medically reviewed by</dt><dd>Dr Amir Rahman, consultant dermatologist</dd>'
       '<dt>Sources</dt><dd>9 references, each linked in the text</dd>'
       '<dt>Last reviewed</dt><dd>12 October 2026</dd>'
       '<dt>Next review</dt><dd>October 2027</dd>'
       '</dl></div>')


def unique(p):
    """A content workflow planned around medical, legal and regulatory review."""
    r = p.row(bg="stone", pad=(112, 56), pad_mobile=(64, 40))
    (h,) = r.cols(100)
    h.heading("A content workflow built for review", tag="h2", mb=16)
    h.text("<p>Health content slows down in review when sources arrive late and claims have to be checked twice. "
           "I plan the work so evidence travels with every draft.</p>", cls="ja-lead", mb=48)
    h.text('<ol class="ja-flow">'
           '<li><strong>Brief with sources</strong><span>Topic, audience and every claim mapped to a reference before writing starts.</span></li>'
           '<li><strong>Draft</strong><span>Written for patients or professionals, with citations in place.</span></li>'
           '<li><strong>Medical review</strong><span>Accuracy checked by your medical reviewer, named on the page.</span></li>'
           '<li><strong>Legal and regulatory</strong><span>Claims and wording cleared against your MLR process.</span></li>'
           '<li><strong>Publish and re-review</strong><span>A review date set, so content never quietly goes out of date.</span></li>'
           '</ol>', cls="ja-flow-wrap")


SPEC = {
    "path": "/pharma-healthcare-seo/",
    "h1": "Pharma &amp; Healthcare SEO <em>Consultant</em>",
    "lead": "Pharmaceutical and healthcare SEO from a pharmacist who worked inside the industry. I help pharma, life "
            "sciences and healthcare companies become the source Google and AI assistants trust, with content built to "
            "pass medical, legal and regulatory review.",
    "art": ART,
    "art_caption": "A fictional article showing the trust signals Google and AI look for on health content.",
    "story": {
        "photo_id": 791, "photo_url": "https://jamilahmed.com/wp-content/uploads/2025/09/Jamil-Ahmed-Personal-Avatar.jpg",
        "photo_alt": "Jamil Ahmed, pharmacist and SEO and AI search consultant",
        "h2": "I learned content in a regulated industry",
        "paras": [
            "Before search, I was a pharmacist working in pharmaceutical international business. At Beacon "
            "Pharmaceuticals I coordinated markets from Sri Lanka, Ghana and Kenya to Latin America, and prepared "
            "regulatory dossiers country by country. Later I was Product Manager for Immunology at Janssen, part of "
            "Johnson &amp; Johnson.",
            "That work taught me two things that matter in health search: nothing goes out without a source, and every "
            "market has its own rules. My SEO work started there too, building and optimising Beacon's product websites "
            "myself.",
            "So I plan health content the way a regulatory file is built: evidence first, reviewers involved from the "
            "brief, and nothing published that you would have to take back.",
        ],
    },
    "intro_h2": "Health search holds you to a higher standard",
    "intro": ["Google treats health as \"Your Money or Your Life\" content: pages that can affect someone's health are "
              "held to the highest bar for expertise, accuracy and trust. AI assistants are just as cautious about "
              "which health sources they cite.",
              "At the same time, every word on a pharma or healthcare site may need medical, legal and regulatory "
              "sign-off. The work has to be evidence-led from the start and planned around your review process."],
    "signs_h3": "Who I work with",
    "signs": ["Pharmaceutical and biotech companies, including export-driven and multi-market brands",
              "Life sciences, medical device and diagnostics companies",
              "Healthcare providers, clinics and digital health platforms",
              "Health information publishers and B2B healthcare SaaS"],
    "help_h2": "Where I help pharma and healthcare teams",
    "help": [
        ("Expertise and trust signals", "Author, reviewer and organisation signals Google and AI engines look for "
                                        "(often called E-E-A-T), with reviewer bylines, references and update dates."),
        ("Evidence-led content", "Topics planned around real patient, caregiver and healthcare professional questions, "
                                 "with separate journeys for each audience."),
        ("AI search for condition areas", "How ChatGPT, Perplexity, Gemini and AI Overviews answer questions in your "
                                          "therapy areas, which sources they cite, and correcting what they get wrong about your brand."),
        ("Technical and international SEO", "Product, condition and HCP site structure, multi-market sites, and gated "
                                            "areas and PDFs that search engines can't read."),
        ("Local healthcare SEO", "Google Business Profiles, location and service pages, and reviews for clinics and providers."),
        ("Fractional SEO leadership", "Part-time senior SEO direction that works with your medical, regulatory and brand teams."),
    ],
    "unique": unique,
    "order": ['hero', 'story', 'unique', 'intro', 'help', 'pricing_short', 'faq', 'close'],
    "close_h2": 'Become the source patients and doctors <em>trust</em>',
    "close_text": "Tell me your therapy areas and how your review process works. I'll tell you honestly what search can and can't do inside those limits.",
    "price_intro": "Every engagement is scoped to your products, markets and review process. After a short call you "
                   "get a written proposal with a fixed price.",
    "ways": [("SEO &amp; AI Search Audit", 'A senior diagnostic of your site, condition areas and competitors, with a '
              'ranked plan. <a href="/seo-ai-search-audit/">What the audit includes</a>'),
             ("Fractional SEO lead", "Part-time senior SEO leadership alongside your medical, regulatory and brand teams."),
             ("Implementation with Reinforce Lab", "When you need execution, my company Reinforce Lab delivers the plan "
                                                   "with evidence-verified content.")],
    "faq": [
        ("What is pharma SEO?",
         "Pharma SEO is search engine optimization for pharmaceutical and life sciences companies. It works within "
         "regulatory and compliance limits and focuses on evidence, expertise and trust, because Google holds health "
         "content to its highest quality standards."),
        ("What does a healthcare SEO consultant do?",
         "A healthcare SEO consultant helps providers, health platforms and health brands rank for the questions "
         "patients and professionals search, with accurate, well-sourced content and strong expertise and trust signals."),
        ("Can SEO work within MLR and compliance review?",
         "Yes. I plan topics, briefs and drafts so sources travel with the content, which makes medical, legal and "
         "regulatory review faster. Your reviewers stay in charge; their job just gets easier."),
        ("Do you cover AI search for health topics?",
         "Yes. I check how ChatGPT, Perplexity, Gemini and Google's AI Overviews answer questions in your condition "
         "areas, which sources they cite, and what it takes for your content to become one of them."),
    ],
    "service_name": "Pharma and healthcare SEO consulting", "service_type": "Healthcare SEO consulting",
    "service_desc": "SEO and AI search consulting for pharmaceutical, life sciences and healthcare companies: expertise "
                    "and trust signals, review-ready content, AI visibility and local healthcare SEO.",
}

if __name__ == "__main__":
    print(payload(POST_ID, build(SPEC)))
