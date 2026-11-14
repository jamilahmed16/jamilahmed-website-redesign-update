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
