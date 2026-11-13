"""Affiliate Disclosure (/affiliate-disclosure/)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _legal import build

BODY = """
<h2>The short version</h2>
<p>Some links on jamilahmed.com are affiliate links. If you click one and buy, I may earn a commission at no extra cost to you. It never changes what I recommend or how I rate a product.</p>

<h2>Which links are affiliate links</h2>
<p>Affiliate links mainly appear in tool reviews, comparisons and "best of" lists. Programs I take part in include Semrush (through the Impact partner network), Moosend, Leonardo AI and other software companies whose tools I write about. Partners may set a cookie when you click so the referral is credited to me; see the <a href="/privacy-policy/">Privacy Policy</a>.</p>

<h2>My relationship with Semrush</h2>
<p>I am a Semrush Ambassador. That is a material connection: Semrush may give me product access, early information, promotional opportunities or other benefits, and I earn commission on referred subscriptions. I write about Semrush because I use it daily in client work, and I point out its limits as well as its strengths.</p>

<h2>My relationship with Reinforce Lab</h2>
<p>I am the Founder and CEO of Reinforce Lab Ltd. When I recommend Reinforce Lab's services, I benefit financially from that recommendation.</p>

<h2>How I review products</h2>
<ul>
<li>Recommendations are based on my own use, client work and research, and I say when a review is based on research rather than hands-on testing.</li>
<li>Companies cannot pay for a positive review or a higher ranking in a list.</li>
<li>When a product changes its pricing or features, the review is updated or marked with the date it was last checked.</li>
</ul>

<h2>Why this page exists</h2>
<p>This disclosure follows the US Federal Trade Commission's Endorsement Guides (16 CFR Part 255) and similar rules in other countries, which ask publishers to make financial relationships clear. If anything here is unclear, ask me through the <a href="/contact/">contact page</a>.</p>
"""

if __name__ == "__main__":
    print(build(int(os.environ["POST_ID"]), "Affiliate Disclosure",
                "How affiliate links and partnerships work on this site, and how they do not affect my recommendations.", BODY))
