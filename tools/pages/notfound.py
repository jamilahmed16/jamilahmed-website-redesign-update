"""Themer 404 layout (fl-theme-layout 883)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bb import Page, payload
p = Page()

hero = p.row(bg="ink", cls="ja26-root ja-dark", pad=(120, 96), pad_mobile=(64, 56))
(h,) = hero.cols(100)
h.heading("This page has <em>moved</em>", tag="h1", mb=24, cls="ja-measure")
h.text("<p>The page you were looking for isn't here. Some older articles were retired or merged when the site was "
       "rebuilt, so the link you followed may be out of date.</p>", cls="ja-lead", mb=40)
h.button("Go to the homepage", "/", inline=True)
h.button("Read the writing", "/blog/", ghost=True, inline=True)

body = p.row(bg="stone", pad=(96, 112), pad_mobile=(56, 64))
a, b = body.cols(50, 50, gap=64)
a.heading("Popular pages", tag="h2", mb=24)
a.text("<ul>"
       '<li><a href="/consulting/">SEO consulting services</a></li>'
       '<li><a href="/seo-ai-search-audit/">SEO &amp; AI Search Audit</a></li>'
       '<li><a href="/generative-engine-optimization/">What is generative engine optimization (GEO)?</a></li>'
       '<li><a href="/about-me/">About Jamil Ahmed</a></li>'
       "</ul>", cls="ja-list")
b.heading("Looking for help with search?", tag="h2", mb=24)
b.text("<p>If you came here for SEO or AI search advice, tell me what you're working on and I'll point you to the right "
       "place.</p>", mb=32)
b.button("Book a consultation", "/contact/")

if __name__ == "__main__":
    print(payload(883, p))
