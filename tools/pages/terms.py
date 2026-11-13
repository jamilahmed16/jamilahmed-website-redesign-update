"""Terms & Conditions (/terms-conditions/)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _legal import build

BODY = """
<h2>About these terms</h2>
<p>These terms apply to your use of jamilahmed.com, run by Jamil Ahmed, Dhaka, Bangladesh. By using the site you agree to them. If you do not agree, please do not use the site.</p>

<h2>Information, not professional advice</h2>
<p>Articles, guides, reviews, the newsletter and the podcast are general information about SEO, AI search, automation and digital growth. They are not legal, financial, medical or regulatory advice, and they are not tailored to your business. Search engines and AI platforms change often, so results described on this site are not guaranteed. Make decisions with professional advice that fits your situation.</p>

<h2>Consulting engagements</h2>
<p>Booking a consultation through this site does not create a client relationship. Paid work, whether with me directly or with Reinforce Lab Ltd, is governed by a separate written agreement that sets out scope, fees and responsibilities. If that agreement conflicts with these terms, the agreement wins.</p>

<h2>Intellectual property</h2>
<p>The text, design, graphics, logos and media on this site belong to Jamil Ahmed unless stated otherwise. You may quote short passages with a clear credit and a link to the original page. You may not republish whole articles, scrape the site for commercial reuse, or present the content as your own without written permission. Trademarks of third parties, such as Semrush or Google, belong to their owners.</p>

<h2>Acceptable use</h2>
<p>Do not use the site to break the law, send spam through its forms, attempt to access systems you are not authorised to use, or interfere with how the site runs.</p>

<h2>Third-party links and affiliate links</h2>
<p>The site links to other websites and tools. I do not control them and am not responsible for their content, products or privacy practices. Some links are affiliate links; see the <a href="/affiliate-disclosure/">Affiliate Disclosure</a> for how they work.</p>

<h2>No warranties</h2>
<p>The site is provided "as is". I work to keep it accurate and available, but I do not guarantee that it is error-free, complete, current or uninterrupted.</p>

<h2>Limitation of liability</h2>
<p>To the extent the law allows, I am not liable for any indirect, incidental or consequential loss, including lost profits, revenue, rankings or data, arising from your use of the site or reliance on its content. Nothing in these terms limits liability that cannot be limited by law.</p>

<h2>Governing law</h2>
<p>These terms are governed by the laws of Bangladesh. Disputes will be handled by the courts of Dhaka, unless the consumer law of your country gives you the right to bring a claim where you live.</p>

<h2>Changes</h2>
<p>I may update these terms. The current version is always on this page, with its "last updated" date. Questions about these terms are welcome through the <a href="/contact/">contact page</a>.</p>
"""

if __name__ == "__main__":
    print(build(int(os.environ["POST_ID"]), "Terms &amp; Conditions",
                "The rules for using jamilahmed.com and its content.", BODY))
