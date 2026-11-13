"""Sitewide Themer footer (fl-theme-layout 866): the blocks of the old footer, in the new design."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bb import Page, SITE, payload
UP = f"{SITE}/wp-content/uploads"

# Simple Icons paths (CC0), 24x24.
ICONS = {
    "LinkedIn": ("https://www.linkedin.com/in/ahmedjamil16/", "M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"),
    "X": ("https://twitter.com/jamilahmed_16", "M18.9 1.15h3.68l-8.04 9.19L24 22.85h-7.4l-5.8-7.58-6.63 7.58H.48l8.6-9.83L0 1.15h7.59l5.24 6.93 6.07-6.93zm-1.29 19.5h2.04L6.48 3.24H4.3l13.31 17.41z"),
    "Facebook": ("https://www.facebook.com/jamilahmed.blog/", "M24 12.07C24 5.41 18.63 0 12 0S0 5.4 0 12.07C0 18.1 4.39 23.1 10.13 24v-8.44H7.08v-3.49h3.04V9.41c0-3.02 1.8-4.7 4.54-4.7 1.31 0 2.68.24 2.68.24v2.97h-1.5c-1.5 0-1.96.93-1.96 1.89v2.26h3.32l-.53 3.5h-2.8V24C19.62 23.1 24 18.1 24 12.07"),
    "Instagram": ("https://www.instagram.com/jamilahmed.blog/", "M12 2.16c3.2 0 3.58.01 4.85.07 3.25.15 4.77 1.69 4.92 4.92.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.15 3.23-1.66 4.77-4.92 4.92-1.27.06-1.64.07-4.85.07s-3.58-.01-4.85-.07c-3.26-.15-4.77-1.7-4.92-4.92-.06-1.27-.07-1.64-.07-4.85s.01-3.58.07-4.85C2.38 3.92 3.9 2.38 7.15 2.23 8.42 2.17 8.8 2.16 12 2.16zM12 0C8.74 0 8.33.01 7.05.07 2.7.27.27 2.69.07 7.05.01 8.33 0 8.74 0 12s.01 3.67.07 4.95c.2 4.36 2.62 6.78 6.98 6.98 1.28.06 1.69.07 4.95.07s3.67-.01 4.95-.07c4.35-.2 6.78-2.62 6.98-6.98.06-1.28.07-1.69.07-4.95s-.01-3.67-.07-4.95c-.2-4.35-2.62-6.78-6.98-6.98C15.67.01 15.26 0 12 0zm0 5.84a6.16 6.16 0 1 0 0 12.32 6.16 6.16 0 0 0 0-12.32zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.41-11.85a1.44 1.44 0 1 0 0 2.88 1.44 1.44 0 0 0 0-2.88z"),
    "YouTube": ("https://www.youtube.com/@jamilahmed.official", "M23.5 6.19a3.02 3.02 0 0 0-2.12-2.14C19.5 3.55 12 3.55 12 3.55s-7.5 0-9.38.5A3.02 3.02 0 0 0 .5 6.19C0 8.07 0 12 0 12s0 3.93.5 5.81a3.02 3.02 0 0 0 2.12 2.14c1.88.5 9.38.5 9.38.5s7.5 0 9.38-.5a3.02 3.02 0 0 0 2.12-2.14C24 15.93 24 12 24 12s0-3.93-.5-5.81zM9.55 15.57V8.43L15.82 12l-6.27 3.57z"),
    "Medium": ("https://medium.com/@jamilahmed.blog", "M13.54 12a6.8 6.8 0 0 1-6.77 6.82A6.8 6.8 0 0 1 0 12a6.8 6.8 0 0 1 6.77-6.82A6.8 6.8 0 0 1 13.54 12zm7.42 0c0 3.54-1.51 6.42-3.38 6.42-1.87 0-3.39-2.88-3.39-6.42s1.52-6.42 3.39-6.42 3.38 2.88 3.38 6.42M24 12c0 3.17-.53 5.75-1.19 5.75-.66 0-1.19-2.58-1.19-5.75s.53-5.75 1.19-5.75C23.47 6.25 24 8.83 24 12z"),
    "Quora": ("https://www.quora.com/profile/Jamil-Ahmed-177-1", "M12.74 18.5c-.84-1.67-1.82-3.35-3.73-3.35-.36 0-.73.06-1.06.21l-.65-1.29c.79-.68 2.07-1.22 3.71-1.22 2.55 0 3.86 1.23 4.9 2.8.61-1.33.9-3.13.9-5.36 0-5.57-1.75-8.42-5.81-8.42-4 0-5.73 2.85-5.73 8.42 0 5.54 1.73 8.36 5.73 8.36.64 0 1.22-.07 1.74-.22zm.98 1.92c-.88.24-1.82.37-2.72.37C5.68 20.79.5 16.54.5 10.92.5 5.26 5.68 1 11 1c5.4 0 10.53 4.24 10.53 9.92 0 3.16-1.47 5.73-3.62 7.39.69 1.04 1.4 1.73 2.4 1.73 1.08 0 1.52-.84 1.6-1.49h1.42c.08.88-.36 4.45-4.28 4.45-2.37 0-3.63-1.38-4.57-2.58z"),
}
social = "<p>" + "".join(
    f'<a href="{url}" aria-label="Jamil Ahmed on {name}" rel="me noopener" target="_blank">'
    f'<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="{path}"/></svg></a>'
    for name, (url, path) in ICONS.items()) + "</p>"

GUIDES = [("What is SEO", "/what-is-seo/"), ("SEO basics", "/seo-basics/"), ("Small business SEO", "/small-business-seo/"),
          ("SEO for CEOs", "/seo-for-ceos/"), ("SEO glossary", "/seo-glossary/"), ("SEO FAQs", "/seo-faqs/"),
          ("What is personal branding", "/what-is-personal-branding/"), ("Personal branding strategy", "/personal-branding-strategy/"),
          ("How to start a blog", "/how-to-start-a-blog/")]
QUICK = [("Home", "/"), ("About", "/about-me/"), ("Consulting", "/consulting/"), ("Blog", "/blog/"),
         ("Newsletter", "/newsletter/"), ("Podcast", "/podcast/"), ("Contact", "/contact/"),
         ("Privacy Policy", "/privacy-policy/"), ("Terms &amp; Conditions", "/terms-conditions/"),
         ("Affiliate Disclosure", "/affiliate-disclosure/"), ("Sitemap", "/sitemap_index.xml")]
links = lambda items: "<p>" + "<br>".join(f'<a href="{u}">{t}</a>' for t, u in items) + "</p>"

p = Page()
top = p.row(bg="ink", cls="ja-dark ja-footer", pad=(96, 48), pad_mobile=(64, 32))
brand, guides, latest, quick = top.cols(31, 21, 27, 21, gap=40)
brand.photo(72, f"{UP}/2023/01/Jamil-Ahmed-logo.png", alt="Jamil Ahmed", cls="ja-logo", mb=20)
brand.text("<p>Jamil Ahmed is an SEO &amp; AI Search Consultant, Semrush Ambassador and Founder &amp; CEO of "
           "<a href=\"https://reinforcelab.com/\">Reinforce Lab Ltd</a>. He helps founders, B2B and pharmaceutical "
           "companies get found on Google and cited in AI search.</p>", mb=24)
brand.text(social, cls="ja-social")
guides.heading("Guides", tag="h4", mb=14)
guides.text(links(GUIDES), cls="ja-footer-links")
latest.heading("Latest posts", tag="h4", mb=14)
latest._add("post-grid", {"layout": "feed", "data_source": "custom_query", "post_type": "post", "posts_per_page": "6",
                           "order": "DESC", "order_by": "date", "show_image": "0", "show_author": "0", "show_date": "0",
                           "show_comments": "0", "show_terms": "0", "show_content": "0", "show_more_link": "0",
                           "posts_title_tag": "h4", "pagination": "none", "show_search": "0", "feed_post_spacing": 0,
                           "class": "ja-footer-latest"})
quick.heading("Quick links", tag="h4", mb=14)
quick.text(links(QUICK), cls="ja-footer-links")

bot = p.row(bg="ink", cls="ja-dark ja-footer-bottom", pad=(0, 40), pad_mobile=(0, 32))
(b,) = bot.cols(100, cls="ja-hair")
b.text("<p>&copy; 2026 Jamil Ahmed. All rights reserved.</p>", cls="ja-caption")

if __name__ == "__main__":
    print(payload(866, p))
