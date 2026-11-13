# jamilahmed.com redesign (2026)

Personal authority site for **Jamil Ahmed, SEO & AI Search Consultant**. Its sibling is the company site, reinforcelab.com:
both use Oswald, IBM Plex and square corners, but this site uses Jamil's brass `#AF824B` in place of the company red.

Everything is built **natively in Beaver Builder**, so every page stays editable in the Beaver editor.

**Launched 13 Nov 2026:** pages 853 to 859 are published, the front page is Home (853) and the posts page is Blog (859).
To roll back: Settings → Reading → "Your latest posts", then set the new pages back to draft.

## What's on the site

| Page | Draft ID | Slug at launch | Spec |
|---|---|---|---|
| Home | 853 | front page | `tools/pages/home.py` |
| About | 854 | `/about-me/` | `tools/pages/about.py` |
| Consulting | 855 | `/consulting/` | `tools/pages/consulting.py` |
| Newsletter | 856 | `/newsletter/` | `tools/pages/newsletter.py` |
| The Jamil Ahmed Show | 857 | `/podcast/` | `tools/pages/podcast.py` |
| Contact | 858 | `/contact/` | `tools/pages/contact.py` |
| Blog (posts index) | 859 | `/blog/` | empty page, set as the posts page |
| Themer header | 865 | sitewide | `tools/pages/header.py` |
| Themer footer | 866 | sitewide (old footer 277 unpublished) | `tools/pages/footer.py` |
| Single post template | 232 | all posts | `tools/pages/single.py` |
| Blog index template | 870 | `/blog/` | `tools/pages/blog.py` |
| Archive template | 393 | categories, author, search | `tools/pages/archive.py` |
| Legal pages (drafts) | 867, 868, 869 | `/privacy-policy/`, `/terms-conditions/`, `/affiliate-disclosure/` | `tools/pages/privacy.py`, `terms.py`, `disclosure.py` |

Other pieces:

- **Design system:** `design/DESIGN.md`, saved on the site as the active Novamira design `jamil-black-brass`.
- **Beaver global colors:** the "JA Ink / Graphite / Stone / Brass / Brass Deep / Brass Light / Muted / Line" swatches in the color picker.
- **Styles:** `wp-content/themes/bb-theme-child/assets/css/ja26.css`, loaded sitewide with the fonts through Head & Footer Code
  (sitewide head). Rules are scoped to `body:has(.ja26-root)`; every template's first row carries that class.
- **Rollback:** the pre-rollout templates, theme settings, head code and menus are saved in the WordPress option
  `ja26_rollback_20261113`.
- **Menu:** "JA 2026 Main", not assigned to any theme location.
- **Forms:** the newsletter forms use the site's existing Beaver "email-address" service (account "Jamil"). Contact uses
  Beaver's native contact form, which mails the site admin address.

## Editing

- **Visually:** open any draft and click *Beaver Builder*. Section classes such as `ja-dark`, `ja-rule`, `ja-list` and
  `ja-btn-ghost` carry the shared styling, so keep them when you duplicate rows.
- **From code:** edit a spec in `tools/pages/`, then run:

  ```bash
  python3 tools/deploy.py page tools/pages/home.py
  ```

  Running a spec replaces that page's whole layout, so any edits made in the Beaver editor are overwritten.
- **CSS:** edit `ja26.css`, then run `python3 tools/deploy.py css`.
- **Screenshots of drafts:** `node tools/shoot.js <outdir> 853,854 1440,390`. It logs in with a one-time Novamira admin link.

Both deploy and screenshot need the Novamira CLI logged in to `jamilahmed.com` (`novamira auth login https://jamilahmed.com/ --device`).

## Why there is a PHP class nobody loads yet

`wp-content/themes/bb-theme-child/classes/class-ja-redesign.php` and the matching `functions.php` line are the "proper" way
to scope fonts and CSS. But WP Engine blocks PHP files from being written by the web server, so Novamira can't deploy them.
The site works without them: the `ja26-root` CSS scope and the per-page head code do the same job. If you ever deploy the
child theme through WP Engine Git push or SFTP, both files are safe to include.

## Still open after launch

1. ~~Publish pages 853 to 859.~~ Done.
2. ~~Settings → Reading: front page Home (853), posts page Blog (859).~~ Done.
3. Restore or recreate **Privacy Policy, Terms & Conditions and Affiliate Disclosure**. They return 404 today and the new
   footer links to them.
4. Decide what happens to the old Beaver page **"Home" (820, `/home/`)**: redirect it to `/` with Yoast, or delete it.
5. Podcast: add the real Spotify or Apple link. Also confirm the show name, since the cover art reads "Talk About Brand".
6. Phase 2: roll the header, footer and type system out to blog archives and single posts (Themer layouts 393 and 232).
   `/blog/` still uses the old archive layout, including the old "2M+ innovators" newsletter claim.
7. After launch, consider deactivating the Novamira plugin on production, or moving this work to a WP Engine staging copy.
   The plugin describes itself as meant for development and staging.

## Design skills

Impeccable is installed for this project in `.claude/skills/impeccable` (Apache 2.0). Use `/impeccable critique` or
`/impeccable audit` on a rendered page.
