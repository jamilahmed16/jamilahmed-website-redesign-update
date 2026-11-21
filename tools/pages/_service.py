"""Shared builder for the four service pages (audit, enterprise, b2b, pharma).

Each page picks its own section order (spec["order"]) so the pages stop sharing one skeleton. Sections:
hero, creds, story, intro, help, help_table, unique, pricing, pricing_short, faq, close.
"""
import json
from bb import Page
from _cta import short_cta

CREDENTIALS = [
    ("Top 3 BI Marketing Influencer", "Onalytica"),
    ("HackerNoon Startups of the Year", "Reinforce Lab, Dhaka winner, 2024"),
    ("Clients include HP", "Bikroy.com, United International University"),
    ("Semrush Ambassador", "Semrush"),
]

PRICE_FIXED = [
    "A fixed price, in writing",
    "Scope and deliverables",
    "Timeline and who is involved",
    "No retainer required",
]


def _hero(p, spec):
    hero = p.row(bg="ink", cls="ja26-root ja-dark ja-svc-hero", pad=(104, 104), pad_mobile=(56, 56))
    l, r = hero.cols(56, 44, align="center", gap=72, cls=["", "ja-svc-art-col"])
    l.heading(spec["h1"], tag="h1", mb=28)
    l.text(f"<p>{spec['lead']}</p>", cls="ja-lead", mb=40)
    l.button("Book a consultation", "/contact/", inline=True)
    l.button(*spec.get("hero_secondary", ("Start with an audit", "/seo-ai-search-audit/")), ghost=True, inline=True)
    r.text(spec["art"] + f'<p class="ja-art-cap">{spec["art_caption"]}</p>', cls="ja-art-wrap")


def _creds(p, spec):
    cred = p.row(bg="stone", cls="ja-recognition", pad=(56, 56), pad_mobile=(40, 24))
    for col, (t, s) in zip(cred.cols(25, 25, 25, 25, gap=40, cls="ja-hair", mobile=[50, 50, 50, 50]), CREDENTIALS):
        col.text(f'<p class="ja-cred-t">{t}</p><p class="ja-cred-s">{s}</p>', cls="ja-cred")


def _story(p, spec):
    """First-person story with a portrait: only for pages where Jamil's own background is the reason to hire him."""
    st = spec["story"]
    r = p.row(bg="stone", cls="ja-story", pad=(112, 112), pad_mobile=(64, 64))
    ph, tx = r.cols(36, 64, align="top", gap=80)
    ph.photo(st["photo_id"], st["photo_url"], alt=st["photo_alt"], cls="ja-portrait")
    tx.heading(st["h2"], tag="h2", mb=28)
    tx.text("".join(f"<p>{x}</p>" for x in st["paras"]), mb=0)


def _intro(p, spec):
    why = p.row(bg="stone", pad=(spec.get("intro_pad_top", 112), 112), pad_mobile=(64, 64))
    a, b = why.cols(55, 45, gap=72)
    a.heading(spec["intro_h2"], tag="h2", mb=24)
    a.text("".join(f"<p>{x}</p>" for x in spec["intro"]))
    b.heading(spec["signs_h3"], tag="h3", mb=16)
    b.text("<ul>" + "".join(f"<li>{x}</li>" for x in spec["signs"]) + "</ul>", cls="ja-list")


def _help(p, spec):
    cov = p.row(bg="graphite", cls="ja-dark ja-defs", pad=(112, 104), pad_mobile=(64, 56))
    (ch,) = cov.cols(100)
    ch.heading(spec["help_h2"], tag="h2", mb=56)
    items = spec["help"]
    for i in range(0, len(items), 2):
        cols = cov.cols(50, 50, gap=72, cls=["ja-hair", "ja-hair"])
        for col, (t, d) in zip(cols, items[i:i + 2]):
            col.heading(t, tag="h3", mb=12)
            col.text(f"<p>{d}</p>", mb=48)


def _help_table(p, spec):
    """Same content as _help, as a three-column table: area, what breaks, what I do."""
    cov = p.row(bg="graphite", cls="ja-dark ja-help-table", pad=(112, 104), pad_mobile=(64, 56))
    (c,) = cov.cols(100)
    c.heading(spec["help_h2"], tag="h2", mb=40)
    rows = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{d}</td></tr>" for a, b, d in spec["help_rows"])
    c.text('<table class="ja-table ja-table-dark"><thead><tr><th>Area</th><th>What breaks at scale</th>'
           f'<th>What I do</th></tr></thead><tbody>{rows}</tbody></table>', cls="ja-table-wrap")


def _pricing(p, spec):
    pr = p.row(bg="ink", cls="ja-dark ja-pricing", pad=(112, 112), pad_mobile=(64, 64))
    pl, pc = pr.cols(55, 45, align="center", gap=80, cls=["", "ja-price-card"])
    pl.heading("How pricing works", tag="h2", mb=20)
    pl.text(f"<p>{spec['price_intro']}</p>", cls="ja-lead", mb=36)
    pl.heading("Ways to work together", tag="h3", mb=16)
    pl.text("<dl class=\"ja-ways\">" + "".join(f"<dt>{t}</dt><dd>{d}</dd>" for t, d in spec["ways"]) + "</dl>")
    pc.heading("Agreed before work starts", tag="h3", mb=20)
    pc.text("<ul>" + "".join(f"<li>{x}</li>" for x in PRICE_FIXED) + "</ul>", cls="ja-list ja-checks", mb=32)
    pc.button("Book a consultation", "/contact/")


def _pricing_short(p, spec):
    """One band, one paragraph: the ways to work and the pricing rule, without the repeated card."""
    pr = p.row(bg="stone", cls="ja-price-short", pad=(96, 96), pad_mobile=(56, 56))
    l, r = pr.cols(40, 60, gap=72)
    l.heading("Ways to work together", tag="h2", mb=0)
    r.text("<dl class=\"ja-ways ja-ways-light\">" + "".join(f"<dt>{t}</dt><dd>{d}</dd>" for t, d in spec["ways"])
           + "</dl>" + f'<p class="ja-price-note">{spec["price_intro"]}</p>')


def _unique(p, spec):
    spec["unique"](p)


def _faq(p, spec):
    qa = p.row(bg="stone", cls="ja-faq", pad=(112, 112), pad_mobile=(64, 64))
    (c,) = qa.cols(100)
    c.heading("Frequently Asked Questions (FAQs)", tag="h2", cls="ja-faq-title", mb=40)
    items = "".join(f"<details class=\"ja-acc\"><summary>{q}</summary><p>{a}</p></details>" for q, a in spec["faq"])
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "name": spec["service_name"], "serviceType": spec["service_type"],
         "description": spec["service_desc"],
         "provider": {"@type": "Person", "name": "Jamil Ahmed", "url": "https://jamilahmed.com/"},
         "areaServed": "Worldwide", "url": f"https://jamilahmed.com{spec['path']}"},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {
            "@type": "Answer", "text": a.replace("&amp;", "&")}} for q, a in spec["faq"]]},
    ]}
    c.text(f'<div class="ja-accs">{items}</div>'
           '<script type="application/ld+json">' + json.dumps(schema) + '</script>', cls="ja-faq-list")


def _close(p, spec):
    short_cta(p, spec["close_h2"], spec["close_text"], [("Book a consultation", "/contact/", False)])


SECTIONS = {"hero": _hero, "creds": _creds, "story": _story, "intro": _intro, "help": _help,
            "help_table": _help_table, "unique": _unique, "pricing": _pricing, "pricing_short": _pricing_short,
            "faq": _faq, "close": _close}
DEFAULT_ORDER = ["hero", "creds", "intro", "help", "unique", "pricing", "faq", "close"]


def build(spec):
    p = Page()
    for name in spec.get("order", DEFAULT_ORDER):
        SECTIONS[name](p, spec)
    return p
