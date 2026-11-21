"""About page (/about-me/)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _cta import closing_cta, short_cta
from bb import Page, SITE, payload
UP = f"{SITE}/wp-content/uploads"
POST_ID = int(os.environ.get("POST_ID", "0"))
p = Page()

hero = p.row(bg="ink", cls="ja26-root ja-dark ja-hero", pad=(96, 0), pad_mobile=(56, 0))
l, r = hero.cols(58, 42, align="center", gap=64)
l.heading("About <em>Jamil Ahmed</em>", tag="h1", mb=28)
l.text("<p>SEO &amp; AI Search Consultant, Semrush Ambassador, pharmacist, Founder &amp; CEO of Reinforce Lab Ltd and CEO of Ranks On Fire LLC. "
       "For 13+ years I have worked across SEO, international business development, pharmaceutical marketing and digital strategy.</p>",
       cls="ja-lead", mb=40)
l.button("Book a consultation", "/contact/", inline=True)
l.button("Connect on LinkedIn", "https://www.linkedin.com/in/ahmedjamil16/", ghost=True, inline=True)
r.photo(717, f"{UP}/2024/10/Jamil-Ahmed-Cover-Image.webp", alt="Jamil Ahmed", cls="ja-cutout")

st = p.row(bg="stone", pad=(112, 64), pad_mobile=(64, 40))
(h,) = st.cols(100)
h.heading("Evidence first, in pharma and in search", tag="h2", mb=40, cls="ja-measure")
a, b = st.cols(50, 50, gap=64)
a.text("<p>I started my career in pharmaceutical international business at Beacon Pharmaceuticals, coordinating markets "
       "from Sri Lanka, Ghana and Kenya to Latin America, and preparing regulatory dossiers country by country. In a "
       "regulated industry nothing ships without evidence, and every market plays by its own rules.</p>"
       "<p>My first SEO projects came from the same place: I built and optimised Beacon's product websites end to end. "
       "After international marketing at Square Group, I became Product Manager for Immunology at Janssen, part of "
       "Johnson &amp; Johnson.</p>")
b.text("<p>In 2018 I founded Reinforce Lab to bring that discipline to digital growth. Today the company builds AI Growth "
       "Systems that connect a business's website, content and search visibility into one engine, from offices in Dhaka "
       "and Katy, Texas.</p>"
       "<p>Search has changed more in the last two years than in the decade before. Buyers ask AI assistants first, and "
       "the brands those assistants cite win the shortlist. My work now is helping companies earn that position with "
       "the same rule I learned in pharma: prove every claim.</p>")

car = p.row(bg="stone", pad=(48, 112), pad_mobile=(24, 64))
ch, cl = car.cols(35, 65, gap=64)
ch.heading("Career", tag="h2", mb=16)
ch.text("<p>The full record is on <a href=\"https://www.linkedin.com/in/ahmedjamil16/\">LinkedIn</a>.</p>")
cl.text("<ul>"
        "<li><strong>2018 to now</strong> Founder &amp; CEO, SEO &amp; AI Search Consultant, Reinforce Lab Ltd</li>"
        "<li><strong>2020 to 2021</strong> Chief Marketing Officer &amp; SEO Consultant, MyOrganicBD</li>"
        "<li><strong>2017</strong> Product Manager, Immunology, Janssen Pharmaceutical Companies of Johnson &amp; Johnson</li>"
        "<li><strong>2016 to 2017</strong> Executive, International Marketing, Square Toiletries &amp; Square Food and Beverage</li>"
        "<li><strong>2016</strong> IT Consultant, International Business, Beacon Pharmaceuticals</li>"
        "<li><strong>2013 to 2015</strong> Executive, International Business, Beacon Pharmaceuticals</li>"
        "<li><strong>2012 to 2013</strong> Executive, Corporate Marketing, Prescription Point</li>"
        "</ul>", cls="ja-list ja-timeline")

rec = p.row(bg="ink", cls="ja-dark", pad=(112, 112), pad_mobile=(64, 64))
rh, rl = rec.cols(35, 65, gap=64)
rh.heading("Recognition", tag="h2", mb=16)
rh.text("<p>Independent rankings and roles, each from the organisation that issued it.</p>")
rl.text("<ul>"
        "<li><strong>Ambassador</strong> Semrush</li>"
        "<li><strong>2018</strong> Top 3 Business Intelligence Marketing Influencer, Onalytica</li>"
        "<li><strong>Onalytica</strong> jadirectives.com in the Top 20 Business Intelligence Marketing blogs</li>"
        "<li><strong>2022 to 2026</strong> Top 50 eCommerce Online Sellers &amp; Influencers, SaleHoo</li>"
        "<li><strong>2018</strong> Top 8 Ecommerce Influencer, Fit Small Business</li>"
        "<li><strong>New York</strong> Featured in Times Square</li>"
        "<li><strong>2024</strong> Reinforce Lab: Winner, HackerNoon Startups of the Year, Dhaka</li>"
        "<li><strong>Clients</strong> HP, Bikroy.com and United International University, among others</li>"
        "<li><strong>Community</strong> 37K+ followers on LinkedIn and 7,600+ newsletter subscribers</li>"
        "</ul>", cls="ja-list ja-timeline")

vn = p.row(bg="stone", pad=(112, 112), pad_mobile=(64, 64))
v, e = vn.cols(50, 50, gap=64, cls=["ja-rule", "ja-rule"])
v.heading("Ventures", tag="h3", mb=16)
v.text("<p>The ventures I run, across consulting, media and education:</p>"
       "<ul><li><strong><a href=\"https://reinforcelab.com/\">Reinforce Lab Limited</a></strong>: AI Growth Systems for growth-stage founders and B2B brands. Flagship system: Search Authority OS. Offices in Dhaka and Katy, Texas.</li>"
       "<li><strong>Ranks On Fire LLC</strong>: SEO and GEO services (US entity)</li>"
       "<li><strong><a href=\"https://jadirectives.com/\">JA Directives</a></strong>: free online courses and small business insights for career-focused learners and aspiring entrepreneurs</li>"
       "<li><strong><a href=\"https://farsightx.com/\">FarSightX Media Group</a></strong>: a portfolio of niche digital magazines, including BestSportsMag, run on AI-assisted editorial and SEO workflows</li></ul>",
       cls="ja-list")
e.heading("Education", tag="h3", mb=16)
e.text("<ul><li><strong>Bachelor's degree</strong> East West University</li>"
       "<li><strong>Digital Marketing</strong> University of Illinois Urbana-Champaign, 2026</li>"
       "<li><strong>Content Strategy for Professionals</strong> Northwestern University, 2026</li></ul>",
       cls="ja-list")

# Open work: the same projects listed on GitHub.
fw = p.row(bg="stone", cls="ja-open-work", pad=(0, 112), pad_mobile=(0, 64))
fh, fl = fw.cols(35, 65, gap=64)
fh.heading("Open work", tag="h2", mb=16)
fh.text('<p>Tools and standards I publish on <a href="https://github.com/jamilahmed16">GitHub</a>.</p>')
fl.text("<ul>"
        '<li><strong><a href="https://github.com/jamilahmed16/seo-geo-aeo-playbook">SEO, GEO and AEO Playbook</a></strong>: '
        "a vendor-neutral standard for building and fixing sites so they rank in Google and get cited by AI search: build gates, "
        "crawl waste fixes and a URL disposition framework for migrations</li>"
        '<li><strong><a href="https://github.com/jamilahmed16/trendblog-ai">TrendBlog AI</a></strong>: an AI editorial tool that turns '
        "live sports trends into research-backed, SEO and GEO ready articles, with source grounding, extractability scoring and schema export</li>"
        '<li><strong><a href="https://reinforcelab.com/search-authority-diagnostic/">Search Authority Diagnostic</a></strong>: a free '
        "baseline of where your site stands in Google and AI search, with your gaps and the first fixes to make</li>"
        "</ul>", cls="ja-list")

# Closing: a personal note, not the sales step list.
short_cta(p, "If this sounds like your <em>problem</em>, let's talk",
          "If something on this page is close to what you're working on, I'd like to hear about it. I read every message myself.",
          [("Book a consultation", "/contact/", False), ("Connect on LinkedIn", "https://www.linkedin.com/in/ahmedjamil16/", True)])

if __name__ == "__main__":
    print(payload(POST_ID, p))

