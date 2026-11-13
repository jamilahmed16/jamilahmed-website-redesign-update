"""Shared layout for legal pages: compact dark title band, then one readable column."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bb import Page, payload

UPDATED = "13 November 2026"


def build(post_id, title, intro, body_html):
    p = Page()
    hero = p.row(bg="ink", cls="ja26-root ja-dark", pad=(96, 72), pad_mobile=(56, 48), width=820)
    (h,) = hero.cols(100)
    h.heading(title, tag="h1", mb=20)
    h.text(f"<p>Last updated {UPDATED}</p>", cls="ja-caption", mb=20)
    h.text(f"<p>{intro}</p>", cls="ja-lead")
    body = p.row(bg="stone", cls="ja-legal", pad=(72, 112), pad_mobile=(48, 64), width=820)
    (b,) = body.cols(100)
    b.text(body_html)
    return payload(post_id, p)
