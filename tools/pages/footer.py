"""Themer footer (fl-theme-layout 866), shown only on the redesigned pages."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bb import Page, SITE, payload
UP = f"{SITE}/wp-content/uploads"
p = Page()
top = p.row(bg="ink", cls="ja-dark ja-footer", pad=(96, 48), pad_mobile=(64, 32))
brand, pages, connect, news = top.cols(37, 18, 18, 27, gap=40)
brand.photo(72, f"{UP}/2023/01/Jamil-Ahmed-logo.png", alt="Jamil Ahmed", cls="ja-logo", mb=20)
brand.text("<p>SEO &amp; AI Search Consultant, Semrush Ambassador and Founder &amp; CEO of "
           "<a href=\"https://reinforcelab.com/\">Reinforce Lab Ltd</a>. Based in Dhaka, working with companies worldwide.</p>")
pages.heading("Pages", tag="h4", mb=14)
pages.text("<p><a href=\"/about-me/\">About</a><br><a href=\"/consulting/\">Consulting</a><br><a href=\"/blog/\">Writing</a><br>"
           "<a href=\"/newsletter/\">Newsletter</a><br><a href=\"/podcast/\">Podcast</a><br><a href=\"/contact/\">Contact</a></p>",
           cls="ja-footer-links")
connect.heading("Connect", tag="h4", mb=14)
connect.text("<p><a href=\"https://www.linkedin.com/in/ahmedjamil16/\">LinkedIn</a><br>"
             "<a href=\"https://www.youtube.com/@jamilahmed.official\">YouTube</a><br>"
             "<a href=\"https://twitter.com/jamilahmed_16\">X</a><br>"
             "<a href=\"https://medium.com/@jamilahmed.blog\">Medium</a><br>"
             "<a href=\"https://www.instagram.com/jamilahmed.blog/\">Instagram</a></p>", cls="ja-footer-links")
news.heading("AI Growth Systems for C&#8209;Suite", tag="h4", mb=14)
news.text("<p>The newsletter for leaders who want practical AI. 7,600+ subscribers.</p>", mb=20)
news.button("Subscribe", "/newsletter/", ghost=True)
bot = p.row(bg="ink", cls="ja-dark ja-footer-bottom", pad=(0, 40), pad_mobile=(0, 32))
(b,) = bot.cols(100, cls="ja-hair")
b.text("<p>&copy; 2026 Jamil Ahmed &nbsp;/&nbsp; <a href=\"/privacy-policy/\">Privacy Policy</a> &nbsp;/&nbsp; "
       "<a href=\"/terms-conditions/\">Terms</a> &nbsp;/&nbsp; <a href=\"/affiliate-disclosure/\">Affiliate disclosure</a> "
       "&nbsp;/&nbsp; <a href=\"/sitemap_index.xml\">Sitemap</a></p>", cls="ja-caption")
if __name__ == "__main__":
    print(payload(866, p))
