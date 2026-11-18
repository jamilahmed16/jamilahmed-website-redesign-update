"""Shared builder for the four service pages (audit, enterprise, b2b, pharma).

Every page shares the brand pieces that should be identical (real credentials, how pricing works, FAQ,
closing call to action) and gets its own hero illustration and one section that only that page has.
"""
import json
from bb import Page
from _cta import closing_cta

CREDENTIALS = [
    ("Semrush Ambassador", "Semrush"),
    ("Janssen (Johnson &amp; Johnson)", "Product Manager, Immunology"),
    ("Founder &amp; CEO, Reinforce Lab", "Since 2018"),
    ("7,600+ readers", "AI Growth Systems newsletter"),
]

PRICE_FIXED = [
    "A fixed price, in writing",
    "Scope and deliverables",
    "Timeline and who is involved",
    "No retainer required",
]


def build(spec):
    p = Page()

    # 1. Hero: copy left, an illustration of the work right.
    hero = p.row(bg="ink", cls="ja26-root ja-dark ja-svc-hero", pad=(104, 104), pad_mobile=(56, 56))
    l, r = hero.cols(56, 44, align="center", gap=72, cls=["", "ja-svc-art-col"])
    l.heading(spec["h1"], tag="h1", mb=28)
    l.text(f"<p>{spec['lead']}</p>", cls="ja-lead", mb=40)
    l.button("Book a consultation", "/contact/", inline=True)
    l.button(*spec.get("hero_secondary", ("Start with an audit", "/seo-ai-search-audit/")), ghost=True, inline=True)
    r.text(spec["art"] + f'<p class="ja-art-cap">{spec["art_caption"]}</p>', cls="ja-art-wrap")

    # 2. Real credentials, the same on every service page.
    cred = p.row(bg="stone", cls="ja-recognition", pad=(56, 56), pad_mobile=(40, 24))
    for col, (t, s) in zip(cred.cols(25, 25, 25, 25, gap=40, cls="ja-hair", mobile=[50, 50, 50, 50]), CREDENTIALS):
        col.text(f'<p class="ja-cred-t">{t}</p><p class="ja-cred-s">{s}</p>', cls="ja-cred")

    # 3. The problem, in this buyer's terms.
    why = p.row(bg="stone", pad=(56, 112), pad_mobile=(40, 64))
    a, b = why.cols(55, 45, gap=72)
    a.heading(spec["intro_h2"], tag="h2", mb=24)
    a.text("".join(f"<p>{x}</p>" for x in spec["intro"]))
    b.heading(spec["signs_h3"], tag="h3", mb=16)
    b.text("<ul>" + "".join(f"<li>{x}</li>" for x in spec["signs"]) + "</ul>", cls="ja-list")

    # 4. What I help with: short definitions in two columns instead of bullet walls.
    cov = p.row(bg="graphite", cls="ja-dark ja-defs", pad=(112, 104), pad_mobile=(64, 56))
    (ch,) = cov.cols(100)
    ch.heading(spec["help_h2"], tag="h2", mb=56)
    items = spec["help"]
    for i in range(0, len(items), 2):
        pair = items[i:i + 2]
        cols = cov.cols(*([50, 50] if len(pair) == 2 else [50, 50]), gap=72, cls=["ja-hair", "ja-hair"])
        for col, (t, d) in zip(cols, pair):
            col.heading(t, tag="h3", mb=12)
            col.text(f"<p>{d}</p>", mb=48)

    # 5. The section only this page has.
    spec["unique"](p)

    # 6. How pricing works, with the ways to work together inside it.
    pr = p.row(bg="ink", cls="ja-dark ja-pricing", pad=(112, 112), pad_mobile=(64, 64))
    pl, pc = pr.cols(55, 45, align="center", gap=80, cls=["", "ja-price-card"])
    pl.heading("How pricing works", tag="h2", mb=20)
    pl.text(f"<p>{spec['price_intro']}</p>", cls="ja-lead", mb=36)
    pl.heading("Ways to work together", tag="h3", mb=16)
    pl.text("<dl class=\"ja-ways\">" + "".join(f"<dt>{t}</dt><dd>{d}</dd>" for t, d in spec["ways"]) + "</dl>")
    pc.heading("Agreed before work starts", tag="h3", mb=20)
    pc.text("<ul>" + "".join(f"<li>{x}</li>" for x in PRICE_FIXED) + "</ul>", cls="ja-list ja-checks", mb=32)
    pc.button("Book a consultation", "/contact/")

    # 7. FAQ with schema.
    qa = p.row(bg="stone", cls="ja-faq", pad=(112, 112), pad_mobile=(64, 64))
    (qh,) = qa.cols(100)
    qh.heading("Frequently Asked Questions (FAQs)", tag="h2", cls="ja-faq-title", mb=48)
    qc = None
    for q, ans in spec["faq"]:
        (qc,) = qa.cols(100, cls="ja-qa")
        qc.heading(q, tag="h3", mb=10)
        qc.text(f"<p>{ans}</p>", mb=32)
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "name": spec["service_name"], "serviceType": spec["service_type"],
         "description": spec["service_desc"],
         "provider": {"@type": "Person", "name": "Jamil Ahmed", "url": "https://jamilahmed.com/"},
         "areaServed": "Worldwide", "url": f"https://jamilahmed.com{spec['path']}"},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {
            "@type": "Answer", "text": a.replace("&amp;", "&")}} for q, a in spec["faq"]]},
    ]}
    qc.text('<script type="application/ld+json">' + json.dumps(schema) + '</script>', mb=0)

    # 8. Closing call to action (shared style across the site).
    closing_cta(p, spec["close_h2"], spec["close_text"],
                [("Book a consultation", "/contact/", False), spec.get("close_secondary", ("Start with an audit", "/seo-ai-search-audit/", True))],
                "What happens next", spec["steps"])
    return p
