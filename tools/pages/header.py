"""Themer header (fl-theme-layout 865), shown only on the redesigned pages."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bb import Page, SITE, payload
UP = f"{SITE}/wp-content/uploads"
p = Page()
r = p.row(bg="ink", cls="ja-dark ja-header", pad=(18, 18), pad_mobile=(14, 14), width=1200)
logo, nav, cta = r.cols(22, 52, 26, align="center", gap=24, mobile=[60, 40, 0], hide_mobile=[0, 0, 1])
logo.photo(72, f"{UP}/2023/01/Jamil-Ahmed-logo.png", alt="Jamil Ahmed", cls="ja-logo")
nav.menu("ja-2026-main", cls="ja-nav")
cta.button("Book a consultation", "/contact/")
if __name__ == "__main__":
    print(payload(865, p))
