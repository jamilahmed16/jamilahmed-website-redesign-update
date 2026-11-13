"""About page (/about-me/)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bb import Page, SITE, payload
UP = f"{SITE}/wp-content/uploads"
POST_ID = int(os.environ.get("POST_ID", "0"))
p = Page()

hero = p.row(bg="ink", cls="ja26-root ja-dark ja-hero", pad=(96, 0), pad_mobile=(56, 0))
l, r = hero.cols(58, 42, align="center", gap=64)
l.heading("About <em>Jamil Ahmed</em>", tag="h1", mb=28)
l.text("<p>SEO &amp; AI Search Consultant, Semrush Ambassador, pharmacist, and Founder &amp; CEO of Reinforce Lab Ltd. "
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
        "</ul>", cls="ja-list ja-timeline")

vn = p.row(bg="stone", pad=(112, 112), pad_mobile=(64, 64))
v, e = vn.cols(50, 50, gap=64, cls=["ja-rule", "ja-rule"])
v.heading("Ventures", tag="h3", mb=16)
v.text("<p>I lead a group of connected ventures across consulting, media and digital products, including:</p>"
       "<ul><li><strong><a href=\"https://reinforcelab.com/\">Reinforce Lab</a></strong>: AI Growth Systems, AI search and SEO for growth-stage and B2B companies</li>"
       "<li><strong>FarSightX Media Group</strong>: media and publishing</li>"
       "<li><strong><a href=\"https://jadirectives.com/\">JA Directives</a></strong>: business intelligence and marketing publication</li></ul>",
       cls="ja-list")
e.heading("Education", tag="h3", mb=16)
e.text("<ul><li><strong>Bachelor's degree</strong> East West University</li>"
       "<li><strong>Digital Marketing</strong> University of Illinois Urbana-Champaign, 2026</li>"
       "<li><strong>Content Strategy for Professionals</strong> Northwestern University, 2026</li></ul>",
       cls="ja-list")

cta = p.row(bg="ink", cls="ja-dark", pad=(112, 112), pad_mobile=(64, 64))
(c,) = cta.cols(100)
c.heading("Let's talk about your search visibility", tag="h2", mb=24, cls="ja-measure")
c.text("<p>If your buyers research in Google and AI assistants, I can show you where you stand and what to fix first.</p>", cls="ja-lead", mb=40)
c.button("Book a consultation", "/contact/")

if __name__ == "__main__":
    print(payload(POST_ID, p))

