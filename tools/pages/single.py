"""Themer singular layout for blog posts (fl-theme-layout 232)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bb import Page, payload
p = Page()

# Title band: breadcrumbs, H1 (post title), author and dates.
hero = p.row(bg="ink", cls="ja26-root ja-dark ja-post-hero", pad=(72, 56), pad_mobile=(40, 36), width=1200)
(h,) = hero.cols(100)
h.text("<p>[wpseo_breadcrumb]</p>", cls="ja-crumbs", mb=20)
h._add("heading", {"heading": "Post title", "tag": "h1", "class": "", "margin_top": 0, "margin_bottom": 22, "margin_unit": "px",
                   "connections": {"heading": {"object": "post", "property": "title", "field": "text"}}})
h.text("<p>By [wpbb post:author_name type='display' link='yes' link_type='archive'] &nbsp;/&nbsp; "
       "Updated [wpbb post:modified_date format='j M Y']</p>", cls="ja-meta")

# Article column.
body = p.row(bg="stone", cls="ja-article", pad=(56, 72), pad_mobile=(32, 48), width=1200)
toc, c = body.cols(28, 72, gap=56, cls=["ja-toc-col", "ja-article-col"])
toc.text('<div class="ja-toc-mount"></div>', cls="ja-toc-wrap")
c._add("photo", {"photo_source": "library", "photo": "", "photo_src": "", "align": "center", "class": "ja-featured",
                 "margin_bottom": 40, "margin_unit": "px",
                 "connections": {"photo": {"object": "post", "property": "featured_image_url", "field": "photo",
                                           "settings": {"size": "large", "default_img": "", "default_img_src": ""}}}})
c.text("<p>__THEMER__fl-post-content</p>", cls="ja-prose")

# Author box and navigation.
au = p.row(bg="stone", cls="ja-after", pad=(0, 64), pad_mobile=(0, 40), width=1200)
pic, a = au.cols(20, 80, gap=32, cls=["ja-author-wrap", "ja-author-wrap"], mobile=[30, 70])
pic.photo(871, "https://jamilahmed.com/wp-content/uploads/2026/11/jamil-ahmed-author.jpg", alt="Jamil Ahmed, SEO and AI Search Consultant", cls="ja-author-pic")
a.heading("<a href=\"/about-me/\">Jamil Ahmed</a>", tag="h3", mb=10)
a.text("<p>SEO &amp; AI Search Consultant, Semrush Ambassador and Founder &amp; CEO of Reinforce Lab Ltd, with 13+ "
       "years across SEO, digital strategy and international pharmaceutical business. Named a Top 3 Business "
       "Intelligence Marketing Influencer by Onalytica.</p>", cls="ja-author-text", mb=20)
a.button("Work with Jamil", "/consulting/", ghost=True)
(nav,) = au.cols(100, cls="ja-hair")
nav.text("<p>__THEMER__fl-post-navigation</p>", cls="ja-postnav")

# Keep reading.
kr = p.row(bg="stone", cls="ja-writing", pad=(64, 96), pad_mobile=(40, 56), width=1200)
(k,) = kr.cols(100)
k.heading("Keep reading", tag="h2", mb=40)
k.posts(3, cls="ja-posts")

# Newsletter.
nl = p.row(bg="ink", cls="ja-dark", pad=(96, 96), pad_mobile=(56, 56))
l, r = nl.cols(50, 50, align="center", gap=64)
l.heading("AI Growth Systems for C&#8209;Suite", tag="h2", mb=16)
l.text("<p>Practical AI, automation and search strategy for business leaders. Join 7,600+ subscribers.</p>", cls="ja-lead")
r.subscribe("Subscribe")

if __name__ == "__main__":
    print(payload(232, p))
