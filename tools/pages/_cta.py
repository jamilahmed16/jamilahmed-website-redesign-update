"""Shared closing call to action: graphite band, brass rule, headline + buttons left, numbered steps right."""


def closing_cta(p, heading, text, buttons, steps_title, steps, form=None):
    """buttons: [(label, href, ghost)], steps: [(title, line)], form: optional callable(col) instead of buttons."""
    cta = p.row(bg="graphite", cls="ja-dark ja-closing", pad=(112, 112), pad_mobile=(64, 64))
    cl, cr = cta.cols(55, 45, align="center", gap=80)
    cl.heading(heading, tag="h2", mb=24)
    cl.text(f"<p>{text}</p>", cls="ja-lead", mb=40)
    if form:
        form(cl)
    for label, href, ghost in buttons:
        cl.button(label, href, ghost=ghost, inline=True)
    cr.heading(steps_title, tag="h3", mb=20)
    cr.text("<ol class=\"ja-next\">" + "".join(f"<li><strong>{t}</strong><span>{s}</span></li>" for t, s in steps)
            + "</ol>", cls="ja-next-wrap")
    return cta


def short_cta(p, heading, text, buttons):
    """Same graphite band and brass rule as closing_cta, but one message and the buttons only: no step list."""
    cta = p.row(bg="graphite", cls="ja-dark ja-closing ja-closing-short", pad=(104, 104), pad_mobile=(64, 64))
    (c,) = cta.cols(100)
    c.heading(heading, tag="h2", mb=24, cls="ja-measure")
    c.text(f"<p>{text}</p>", cls="ja-lead", mb=40)
    for label, href, ghost in buttons:
        c.button(label, href, ghost=ghost, inline=True)
    return cta


NEEDS = [("audit", "SEO &amp; AI search audit"), ("enterprise", "Enterprise SEO"), ("b2b", "B2B &amp; SaaS growth"),
         ("pharma", "Pharma &amp; healthcare"), ("unsure", "Not sure yet")]
NOW = [("falling", "Traffic is falling"), ("ai", "Competitors are cited in AI, we aren't"),
       ("migration", "A migration or redesign is coming"), ("scratch", "We're starting from scratch")]
STEPS = [("Send a short brief", "Your company, markets and goals."),
         ("Short call", "We agree what to fix first, scope and timeline."),
         ("Audit or kickoff", "Usually the audit first, then a 90-day plan your team can ship.")]


def _chips(name, items, legend):
    chips = "".join(f'<button type="button" class="ja-chip" aria-pressed="false" data-{name}="{k}">{label}</button>'
                    for k, label in items)
    return f'<fieldset class="ja-brief-set"><legend>{legend}</legend><div class="ja-chips">{chips}</div></fieldset>'


def brief_cta(p, heading, text, preselect=None, secondary=("Email me instead", "mailto:hello@jamilahmed.com")):
    """The closing call to action for sales pages: an oversized headline and the booking button on the left, and on
    the right a two-click brief builder that writes the first message and carries it into the contact form."""
    cta = p.row(bg="ink", cls="ja-dark ja-closing ja-brief-row", pad=(128, 112), pad_mobile=(72, 64))
    l, r = cta.cols(52, 48, align="top", gap=80)
    l.heading(heading, tag="h2", mb=28, cls="ja-brief-title")
    l.text(f"<p>{text}</p>", cls="ja-lead", mb=40)
    l.button("Book a consultation", "/contact/", inline=True)
    l.button(*secondary, ghost=True, inline=True)
    l.text('<ol class="ja-brief-steps">' + "".join(f"<li><strong>{t}</strong><span>{s}</span></li>" for t, s in STEPS)
           + "</ol>", mt=56)
    r.text(f'<div class="ja-brief" data-brief data-pre="{preselect or ""}">'
           '<p class="ja-brief-h">Write your first message in two clicks</p>'
           + _chips("need", NEEDS, "What do you need?") + _chips("now", NOW, "What's happening now?")
           + '<div class="ja-brief-out"><p class="ja-brief-label">Your message</p><p class="ja-brief-msg" data-out aria-live="polite"></p></div>'
           '<a class="ja-brief-send" href="/contact/" data-send>Send this brief <span aria-hidden="true"></span></a>'
           '</div>', cls="ja-brief-wrap")
    return cta
