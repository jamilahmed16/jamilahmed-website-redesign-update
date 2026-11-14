"""Podcast page (/podcast/)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _cta import closing_cta
from bb import Page, SITE, payload
UP = f"{SITE}/wp-content/uploads"
POST_ID = int(os.environ.get("POST_ID", "0"))
p = Page()

hero = p.row(bg="ink", cls="ja26-root ja-dark", pad=(120, 112), pad_mobile=(64, 64))
l, r = hero.cols(58, 42, align="center", gap=64)
l.heading("The Jamil Ahmed <em>Show</em>", tag="h1", mb=28)
l.text("<p>Conversations with industry experts, CEOs, entrepreneurs and thought leaders about search, AI and building a "
       "business people can find.</p>", cls="ja-lead", mb=40)
l.button("Watch on YouTube", "https://www.youtube.com/@jamilahmed.official", inline=True)
l.button("Be a guest", "/contact/", ghost=True, inline=True)
r.photo(411, f"{UP}/2023/07/take-about-brand-Jamil-Ahmed.png", alt="The Jamil Ahmed Show")

ab = p.row(bg="stone", pad=(112, 112), pad_mobile=(64, 64))
a, b = ab.cols(45, 55, gap=64)
a.heading("What we talk about", tag="h2", mb=24)
a.text("<p>Each episode goes deep with one guest on what is actually working, with the numbers and the mistakes left in.</p>")
b.text("<ul>"
       "<li><strong>SEO and AI search</strong>: how buyers find companies now</li>"
       "<li><strong>Founders and leadership</strong>: building and scaling service businesses</li>"
       "<li><strong>Content and authority</strong>: earning trust in crowded markets</li>"
       "<li><strong>AI in practice</strong>: automation that pays for itself</li>"
       "</ul>", cls="ja-list")

# Closing call to action (shared style)
closing_cta(p, "Have a story worth <em>sharing</em>?",
            "I invite operators, founders and specialists with real experience to share. Tell me about yourself and the topic you would bring.",
            [("Be a guest", "/contact/", False), ("Read the newsletter", "/newsletter/", True)],
            "How it works", [("Send your idea", "Who you are and the topic you'd bring."),
                              ("Quick call", "We shape the conversation together."),
                              ("Record the episode", "A relaxed, practical conversation.")])

if __name__ == "__main__":
    print(payload(POST_ID, p))

