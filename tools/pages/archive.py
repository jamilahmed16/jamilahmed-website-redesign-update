"""Themer archive layout: /blog/, categories, author and search (fl-theme-layout 393)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bb import Page, payload
p = Page()

hero = p.row(bg="ink", cls="ja26-root ja-dark", pad=(88, 72), pad_mobile=(48, 40))
(h,) = hero.cols(100)
h.text("<p>[wpseo_breadcrumb]</p>", cls="ja-crumbs", mb=20)
h.heading("[wpbb archive:title]", tag="h1", mb=16, cls="ja-measure")
h.text("<p>[wpbb archive:description]</p>", cls="ja-archive-desc")

lst = p.row(bg="stone", cls="ja-writing", pad=(72, 96), pad_mobile=(40, 56))
(c,) = lst.cols(100)
c._add("post-grid", {
    "layout": "grid", "post_width": 340, "data_source": "main_query",
    "post_spacing": 40, "post_padding": 0, "match_height": "1", "posts_title_tag": "h2",
    "show_image": "0", "show_author": "0", "show_date": "1", "date_format": "M j, Y",
    "show_comments": "0", "show_comments_grid": "0", "show_terms": "0",
    "show_content": "1", "content_type": "excerpt", "content_length": "24",
    "show_more_link": "1", "more_link_text": "Read the article",
    "pagination": "numbers", "posts_per_page": "12", "show_search": "0",
    "no_results_message": "Nothing here yet. Try the latest articles on the blog.",
    "class": "ja-posts",
})

nl = p.row(bg="ink", cls="ja-dark", pad=(96, 96), pad_mobile=(56, 56))
l, r = nl.cols(50, 50, align="center", gap=64)
l.heading("AI Growth Systems for C&#8209;Suite", tag="h2", mb=16)
l.text("<p>Practical AI, automation and search strategy for business leaders. Join 7,600+ subscribers.</p>", cls="ja-lead")
r.subscribe("Subscribe")

if __name__ == "__main__":
    print(payload(393, p))
