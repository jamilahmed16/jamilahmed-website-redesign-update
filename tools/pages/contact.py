"""Contact page (/contact/)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bb import Page, SITE, payload
UP = f"{SITE}/wp-content/uploads"
POST_ID = int(os.environ.get("POST_ID", "0"))
p = Page()

hero = p.row(bg="ink", cls="ja26-root ja-dark", pad=(120, 96), pad_mobile=(64, 56))
(h,) = hero.cols(100)
h.heading("Book a <em>consultation</em>", tag="h1", mb=28)
h.text("<p>Tell me about your company and what you want search to do for it. I read every message myself.</p>", cls="ja-lead")

body = p.row(bg="stone", pad=(96, 112), pad_mobile=(56, 64))
f, info = body.cols(60, 40, gap=80)
f.contact()
info.heading("What helps me reply well", tag="h2", mb=16)
info.text("<ul>"
          "<li>Your company website</li>"
          "<li>Your market and the buyers you want to reach</li>"
          "<li>What is happening with your search traffic today</li>"
          "<li>Any deadline, such as a launch or a migration</li>"
          "</ul>", cls="ja-list", mb=40)
info.text('<p>Prefer email? Write to <a href="mailto:hello@jamilahmed.com">hello@jamilahmed.com</a>.</p>', mb=16)
info.text("<p>Need a full team rather than a consultant? Say so in your message and I'll point you to "
          "<a href=\"https://reinforcelab.com/\">Reinforce Lab</a>.</p>")

if __name__ == "__main__":
    print(payload(POST_ID, p))

