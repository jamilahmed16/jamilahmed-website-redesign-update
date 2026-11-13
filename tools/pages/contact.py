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
info.heading("What helps me reply well", tag="h3", mb=16)
info.text("<ul>"
          "<li>Your company website</li>"
          "<li>Your market and the buyers you want to reach</li>"
          "<li>What is happening with your search traffic today</li>"
          "<li>Any deadline, such as a launch or a migration</li>"
          "</ul>", cls="ja-list", mb=40)
info.heading("Elsewhere", tag="h3", mb=16)
info.text("<p><a href=\"https://www.linkedin.com/in/ahmedjamil16/\">LinkedIn</a><br>"
          "<a href=\"https://www.youtube.com/@jamilahmed.official\">YouTube</a><br>"
          "<a href=\"https://twitter.com/jamilahmed_16\">X</a></p>"
          "<p>Need a full team? Visit <a href=\"https://reinforcelab.com/\">Reinforce Lab</a>.</p>")

if __name__ == "__main__":
    print(payload(POST_ID, p))

