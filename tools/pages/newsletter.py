"""Newsletter page (/newsletter/)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _cta import closing_cta
from bb import Page, SITE, payload
UP = f"{SITE}/wp-content/uploads"
POST_ID = int(os.environ.get("POST_ID", "0"))
p = Page()

hero = p.row(bg="ink", cls="ja26-root ja-dark", pad=(120, 112), pad_mobile=(64, 64))
(l,) = hero.cols(100)
l.heading("AI Growth Systems <em>for C&#8209;Suite</em>", tag="h1", mb=28, cls="ja-measure")
l.text("<p>My newsletter for business leaders who want practical AI, not hype. Join 7,600+ subscribers.</p>", cls="ja-lead", mb=36)
l.subscribe("Subscribe", cls="ja-form-narrow")
l.text("<p>Free. Unsubscribe any time.</p>", cls="ja-caption", mt=16)

inside = p.row(bg="stone", pad=(112, 112), pad_mobile=(64, 64))
a, b = inside.cols(45, 55, gap=64)
a.heading("What every issue includes", tag="h2", mb=24)
a.text("<p>Everything I build and test at Reinforce Lab, written up so leaders can apply it inside their own organisations.</p>")
b.text("<ul>"
       "<li><strong>Practical AI solutions</strong> you can deploy this quarter</li>"
       "<li><strong>Automation workflows</strong> for marketing, research and reporting</li>"
       "<li><strong>Search strategy</strong> for Google and AI assistants</li>"
       "<li><strong>Implementation guides</strong> with the steps, tools and costs</li>"
       "<li><strong>Real case studies</strong> from regulated and B2B markets</li>"
       "</ul>", cls="ja-list")

who = p.row(bg="stone", pad=(0, 112), pad_mobile=(0, 64))
for col, (title, body) in zip(who.cols(33.33, 33.33, 33.34, gap=40, cls="ja-rule"), [
    ("For founders", "Decide where AI and search fit in your growth plan, and what to leave alone."),
    ("For C-suite leaders", "Turn AI from experiments into systems with owners, budgets and measurable returns."),
    ("For marketing teams", "Ship faster with workflows that cut repetitive work without cutting quality."),
]):
    col.heading(title, tag="h3", mb=10)
    col.text(f"<p>{body}</p>")

# Closing call to action (shared style, with the subscribe form)
closing_cta(p, "Get the next <em>issue</em>", "One email, practical and to the point.", [],
            "What you get", [("Practical AI solutions", "Tools and ideas you can use this week."),
                              ("Automation workflows", "Step-by-step systems that save your team hours."),
                              ("Search strategy and case studies", "What's working on Google and in AI search.")],
            form=lambda col: col.subscribe("Subscribe"))

if __name__ == "__main__":
    print(payload(POST_ID, p))

