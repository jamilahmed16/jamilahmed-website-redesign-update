"""Privacy Policy (/privacy-policy/)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _legal import build

BODY = """
<h2>Who is responsible for your data</h2>
<p>This website, jamilahmed.com, is run by Jamil Ahmed, an SEO and AI Search consultant based in Dhaka, Bangladesh ("I", "me"). I am the controller of the personal data collected through this site. You can reach me about anything in this policy through the <a href="/contact/">contact page</a>.</p>

<h2>What I collect and why</h2>
<ul>
<li><strong>Contact form.</strong> Your name, email address, company or website, and your message. I use it only to reply to you and, if we work together, to scope the engagement. Legal basis: your request and my legitimate interest in answering it.</li>
<li><strong>Newsletter sign-up.</strong> Your email address, used to send the AI Growth Systems for C-Suite newsletter. Legal basis: your consent, which you can withdraw at any time with the unsubscribe link in every email or by contacting me.</li>
<li><strong>Analytics.</strong> Google Analytics, installed through Google Site Kit, records how the site is used: pages viewed, approximate location, device and browser, and how you arrived. I use it in aggregate to improve the content. Legal basis: legitimate interest, or consent where your local law requires it.</li>
<li><strong>Server and security logs.</strong> My host (WP Engine) and its network provider (Cloudflare) process your IP address and request details to deliver the site and protect it from abuse. Legal basis: legitimate interest in running a secure website.</li>
</ul>
<p>I do not sell your personal data, and I do not use it for automated decisions that affect you.</p>

<h2>Cookies</h2>
<p>The site uses a small number of cookies:</p>
<ul>
<li><strong>Analytics cookies</strong> set by Google Analytics (for example <code>_ga</code>) to count visits and sessions.</li>
<li><strong>Functional cookies</strong> that remember interface choices, such as whether the table of contents is open on an article.</li>
<li><strong>Security cookies</strong> set by Cloudflare to tell real visitors from bots.</li>
</ul>
<p>When you click an affiliate link, the partner's site may set its own cookie to credit the referral. That cookie is controlled by the partner under its own privacy policy. You can block or delete cookies in your browser settings; the site will still work.</p>

<h2>Who else processes your data</h2>
<ul>
<li><strong>WP Engine</strong> (hosting) and <strong>Cloudflare</strong> (content delivery and security).</li>
<li><strong>Google</strong> (Analytics and Google Fonts, which receive your IP address when fonts load).</li>
<li><strong>My email provider</strong>, which receives contact-form messages and newsletter sign-ups.</li>
<li><strong>Reinforce Lab Ltd</strong>, my company, if your enquiry turns into a project delivered by its team.</li>
</ul>
<p>Some of these providers are located outside your country, including in the United States. Where the law requires it, transfers rely on the providers' standard contractual clauses or equivalent safeguards.</p>

<h2>How long I keep it</h2>
<ul>
<li>Contact-form messages: up to 24 months after our last exchange, unless we start working together, in which case they are kept for the length of the engagement and any period the law requires.</li>
<li>Newsletter subscriptions: until you unsubscribe.</li>
<li>Analytics data: for the retention period set in Google Analytics, at most 14 months.</li>
</ul>

<h2>Your rights</h2>
<p>Depending on where you live, including under the EU and UK GDPR and California privacy law, you can ask to access, correct, delete or export your personal data, object to or restrict how it is used, and withdraw consent at any time. California residents can also ask what personal information is collected and how it is used; I do not sell or share it for cross-context behavioural advertising. To use any of these rights, send a request through the <a href="/contact/">contact page</a>. I will reply within 30 days. You also have the right to complain to your local data protection authority.</p>

<h2>Children</h2>
<p>This site is written for business professionals and is not directed at children under 16. I do not knowingly collect their data.</p>

<h2>Security</h2>
<p>The site is served only over HTTPS, hosted on managed infrastructure, and protected by a web application firewall. No method of transmission is perfectly secure, but I take reasonable steps to protect what you share.</p>

<h2>Changes to this policy</h2>
<p>If this policy changes, the new version will be posted on this page with a new "last updated" date.</p>
"""

if __name__ == "__main__":
    print(build(int(os.environ["POST_ID"]), "Privacy Policy",
                "How jamilahmed.com collects, uses and protects personal data, and the choices you have.", BODY))
