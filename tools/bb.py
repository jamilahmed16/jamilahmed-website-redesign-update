"""
Tiny helpers that turn a readable page spec into a Beaver Builder node list
for Novamira's `beaver-builder-set-layout` ability.

Every page is native Beaver Builder: rows, column groups, columns and
heading / rich-text / button / photo / post-grid modules. No HTML modules.
Shared look lives in wp-content/themes/bb-theme-child/assets/css/ja26.css,
which only applies to pages whose first row has the class `ja26-root`.
"""

import itertools
import json

# Beaver Builder global colours created on jamilahmed.com (label -> uid).
GLOBAL = {
    "ink": ("03691dfdb", "141312"),
    "graphite": ("dfe687e25", "1F1D1B"),
    "stone": ("1c6c26cf9", "E9E7E3"),
    "stone_deep": ("d5459b7b0", "DFDCD7"),
    "brass": ("cb83eab4f", "AF824B"),
    "brass_deep": ("8f4e0e3ca", "87622F"),
    "brass_light": ("0eca0c646", "CDA56F"),
    "muted": ("f56659eb5", "5E5A55"),
    "line": ("07b63515a", "DAD6D0"),
}

SITE = "https://jamilahmed.com"

_ids = itertools.count(1)
_ns = ["x"]  # per-layout namespace so node ids never collide across header, page and footer


def _id(prefix):
    return f"ja{_ns[0]}{prefix}{next(_ids):03d}"


def _color(field, name):
    """Settings for a colour field bound to a Beaver global colour."""
    uid, hexv = GLOBAL[name]
    return {field: hexv}, {
        field: {"object": "site", "property": f"global_color_{uid}", "field": "color", "settings": []}
    }


class Page:
    def __init__(self):
        self.nodes = []
        self._row_pos = 0

    # ---------- structure ----------

    def row(self, bg="stone", cls="", pad=(112, 112), pad_mobile=(64, 64), width=1200, full_content=False):
        rid = _id("r")
        s = {
            "width": "full",
            "content_width": "full" if full_content else "fixed",
            "max_content_width": width,
            "max_content_width_unit": "px",
            "padding_top": pad[0],
            "padding_bottom": pad[1],
            "padding_left": 32,
            "padding_right": 32,
            "padding_unit": "px",
            "padding_top_responsive": pad_mobile[0],
            "padding_bottom_responsive": pad_mobile[1],
            "padding_left_responsive": 20,
            "padding_right_responsive": 20,
            "padding_responsive_unit": "px",
            "class": cls,
            "container_element": "section",
        }
        if bg:
            colour, conn = _color("bg_color", bg)
            s.update({"bg_type": "color", **colour, "connections": conn})
        self.nodes.append({"id": rid, "type": "row", "position": self._row_pos, "settings": s})
        self._row_pos += 1
        return Row(self, rid)


class Row:
    def __init__(self, page, rid):
        self.page, self.id, self._grp = page, rid, 0

    def cols(self, *sizes, align="top", gap=48, cls=None, mobile_reverse=False, mobile=None, hide_mobile=None):
        gid = _id("g")
        self.page.nodes.append({"id": gid, "type": "column-group", "parent": self.id, "position": self._grp, "settings": {}})
        self._grp += 1
        out = []
        for i, size in enumerate(sizes):
            cid = _id("c")
            s = {
                "size": size,
                "content_alignment": align,
                "padding_left": 0 if i == 0 else gap // 2,
                "padding_right": 0 if i == len(sizes) - 1 else gap // 2,
                "padding_unit": "px",
                "padding_left_responsive": 0,
                "padding_right_responsive": 0,
                "padding_responsive_unit": "px",
                "class": (cls[i] if isinstance(cls, (list, tuple)) else cls) or "",
            }
            if mobile:
                # Keep columns side by side on phones at these widths.
                s.update({"size_responsive": mobile[i], "size_medium": mobile[i]})
            elif len(sizes) > 1:
                # Stack on mobile with breathing room between stacked columns.
                s.update({"margin_bottom_responsive": 40, "margin_responsive_unit": "px"})
            if hide_mobile and hide_mobile[i]:
                s["responsive_display"] = "desktop,large"
            if mobile_reverse:
                s["responsive_order"] = "mobile"
            self.page.nodes.append({"id": cid, "type": "column", "parent": gid, "position": i, "settings": s})
            out.append(Col(self.page, cid))
        return out


class Col:
    def __init__(self, page, cid):
        self.page, self.id, self._pos = page, cid, 0

    def _add(self, module, settings):
        mid = _id("m")
        self.page.nodes.append({"id": mid, "type": "module", "parent": self.id, "position": self._pos, "module": module, "settings": {"type": module, **settings}})
        self._pos += 1
        return self

    def heading(self, text, tag="h2", cls="", mb=24, mt=0):
        return self._add("heading", {
            "heading": text, "tag": tag, "class": cls,
            "margin_top": mt, "margin_bottom": mb, "margin_unit": "px",
        })

    def text(self, html, cls="", mb=0, mt=0):
        return self._add("rich-text", {
            "text": html, "class": cls,
            "margin_top": mt, "margin_bottom": mb, "margin_unit": "px",
        })

    def button(self, label, href, ghost=False, mb=0, mt=0, inline=False):
        cls = "ja-btn-ghost" if ghost else ""
        if inline:
            cls += " ja-inline"
        return self._add("button", {
            "text": label, "click_action": "link", "link": href, "link_target": "_self",
            "align": "left", "width": "auto", "class": cls.strip(),
            "margin_top": mt, "margin_bottom": mb, "margin_unit": "px",
        })

    def photo(self, att_id, url, alt="", cls="", mb=0):
        return self._add("photo", {
            "photo_source": "library", "photo": att_id, "photo_src": url,
            "crop": "", "align": "left", "show_caption": "0", "class": cls,
            "margin_bottom": mb, "margin_unit": "px", "alt": alt,
        })

    def posts(self, count=3, cls=""):
        return self._add("post-grid", {
            "layout": "grid", "post_width": 340, "data_source": "custom_query", "post_type": "post",
            "posts_per_page": str(count), "order": "DESC", "order_by": "date",
            "post_columns": 3, "post_columns_medium": 2, "post_columns_responsive": 1,
            "post_spacing": 40, "post_padding": 0, "match_height": "1",
            "posts_title_tag": "h3", "show_image": "0",
            "show_author": "0", "show_date": "1", "date_format": "M j, Y",
            "show_comments": "0", "show_comments_grid": "0", "show_terms": "0",
            "show_content": "1", "content_type": "excerpt", "content_length": "22",
            "show_more_link": "1", "more_link_text": "Read the article",
            "pagination": "none", "show_search": "0", "class": cls,
        })


    def raw(self, module, settings):
        """Any native module (Themer modules such as fl-post-content) with explicit settings."""
        return self._add(module, settings)

    def menu(self, slug, cls=""):
        return self._add("menu", {
            "menu": slug, "menu_layout": "horizontal", "submenu_hover_toggle": "none",
            "collapse": "1", "mobile_toggle": "hamburger", "mobile_full_width": "below",
            "mobile_breakpoint": "medium-mobile", "mobile_stacked": "yes", "menu_search": "hide",
            "menu_align": "right", "class": cls,
        })

    def subscribe(self, button="Subscribe", cls=""):
        """Newsletter form on the site's existing Beaver 'email-address' service (account 'Jamil')."""
        return self._add("subscribe-form", {
            "service": "email-address", "service_account": "Jamil",
            "layout": "inline", "labels": "hide", "show_name": "hide",
            "email_field_text": "Your work email", "terms_checkbox": "hide",
            "success_action": "message",
            "success_message": "<p>Thanks for subscribing. Check your inbox to confirm.</p>",
            "btn_text": button, "show_recaptcha": "hide", "class": ("ja-form " + cls).strip(),
        })

    def contact(self, cls=""):
        """Native Beaver contact form; mail goes to the site admin address (mailto left empty)."""
        return self._add("contact-form", {
            "mailto_email": "", "name_toggle": "show", "name_placeholder": "Your name",
            "email_toggle": "show", "email_placeholder": "Your work email",
            "subject_toggle": "show", "subject_placeholder": "Company and website",
            "subject_hidden": "jamilahmed.com consultation request",
            "phone_toggle": "hide", "message_placeholder": "What would you like help with?",
            "placeholder_labels": "labels", "terms_checkbox": "hide",
            "success_action": "show_message",
            "success_message": "<p>Thank you. Your message is on its way to Jamil, who replies personally.</p>",
            "btn_text": "Send message", "class": ("ja-form " + cls).strip(),
        })


def payload(post_id, page):
    # Re-key every node with the post id so ids are unique site-wide (Beaver merges equal ids).
    remap = {}
    for n in page.nodes:
        remap[n["id"]] = n["id"].replace("jax", f"ja{post_id}", 1)
    for n in page.nodes:
        n["id"] = remap[n["id"]]
        if n.get("parent"):
            n["parent"] = remap[n["parent"]]
    return json.dumps({"post": post_id, "status": "both", "nodes": page.nodes})
