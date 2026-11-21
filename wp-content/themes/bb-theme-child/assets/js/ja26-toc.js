/*
 * Jamil Ahmed: sticky "Table of Contents" sidebar for single posts.
 * Builds a numbered table of contents from the H2s in the article (.ja-prose),
 * highlights the chapter in view, shows reading progress and total reading time.
 * Mounts into .ja-toc-mount (left column of the single-post template). No dependencies.
 */
(function () {
	'use strict';
	var mount = document.querySelector('.ja-toc-mount');
	var article = document.querySelector('.ja-prose');
	if (!mount || !article) return;

	var skip = '.ja-takeaways, .ja-answer, .ja-sponsor, #ez-toc-container';
	var norm = function (t) { return (t || '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim(); };
	var h1 = document.querySelector('h1');
	var title = norm(h1 && h1.textContent);
	// Older posts repeat the post title as the first H2: hide that duplicate.
	Array.prototype.forEach.call(article.querySelectorAll('h2'), function (h) {
		if (title && norm(h.textContent) === title) { h.classList.add('ja-dup-title'); }
	});
	var pick = function (sel) {
		return Array.prototype.filter.call(article.querySelectorAll(sel), function (h) {
			return !h.closest(skip) && !h.classList.contains('ja-dup-title') && h.textContent.trim();
		});
	};
	var heads = pick('h2');
	// Older posts use H3 for their sections: fall back to H2 + H3 so they still get a contents list.
	if (heads.length < 3) heads = pick('h2, h3');
	if (heads.length < 3) { document.documentElement.classList.add('ja-no-toc'); return; }

	var slug = function (t) { return t.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 60); };
	var words = (article.innerText || article.textContent).split(/\s+/).length;
	var minutes = Math.max(1, Math.round(words / 230));

	var nav = document.createElement('nav');
	nav.className = 'ja-toc';
	nav.setAttribute('aria-label', 'Table of contents');
	var html = '<div class="ja-toc-head"><span>Table of Contents</span><span class="ja-toc-pct" aria-hidden="true">0%</span></div><ol class="ja-toc-list">';
	heads.forEach(function (h, i) {
		var inner = h.querySelector('[id]');
		var id = h.id || (inner && inner.id) || ('ch-' + (i + 1) + '-' + slug(h.textContent));
		if (!h.id && !(inner && inner.id)) h.id = id;
		h.setAttribute('data-ja-ch', i);
		var n = (i + 1 < 10 ? '0' : '') + (i + 1);
		html += '<li><a href="#' + id + '" data-i="' + i + '"><span class="ja-toc-n">' + n + '</span><span class="ja-toc-t"></span></a></li>';
	});
	html += '</ol><div class="ja-toc-foot">About ' + minutes + ' min in total</div>';
	nav.innerHTML = html;
	var titles = nav.querySelectorAll('.ja-toc-t');
	heads.forEach(function (h, i) { titles[i].textContent = h.textContent.trim(); });
	mount.appendChild(nav);
	document.documentElement.classList.add('ja-has-toc');

	var links = nav.querySelectorAll('.ja-toc-list a');
	var pct = nav.querySelector('.ja-toc-pct');
	var list = nav.querySelector('.ja-toc-list');
	var current = -1;

	nav.addEventListener('click', function (e) {
		var a = e.target.closest('a[data-i]');
		if (!a) return;
		e.preventDefault();
		var h = heads[+a.getAttribute('data-i')];
		var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
		var hd = document.querySelector('.fl-builder-content[data-type="header"]');
		var off = (hd ? hd.getBoundingClientRect().height : 0) + 24;
		window.scrollTo({ top: h.getBoundingClientRect().top + window.pageYOffset - off, behavior: reduce ? 'auto' : 'smooth' });
		if (history.replaceState) history.replaceState(null, '', '#' + (h.id || a.getAttribute('href').slice(1)));
	});

	var ticking = false;
	function update() {
		ticking = false;
		var r = article.getBoundingClientRect();
		var total = r.height - window.innerHeight * 0.6;
		var p = total > 0 ? Math.min(100, Math.max(0, Math.round((-r.top + window.innerHeight * 0.2) / total * 100))) : 100;
		pct.textContent = p + '%';
		var active = 0;
		for (var i = 0; i < heads.length; i++) {
			if (heads[i].getBoundingClientRect().top < window.innerHeight * 0.3) active = i; else break;
		}
		if (active !== current) {
			if (links[current]) { links[current].classList.remove('is-active'); links[current].removeAttribute('aria-current'); }
			links[active].classList.add('is-active');
			links[active].setAttribute('aria-current', 'true');
			current = active;
			var li = links[active].parentNode;
			if (list.scrollHeight > list.clientHeight) {
				var top = li.offsetTop - list.clientHeight / 2 + li.clientHeight / 2;
				list.scrollTo ? list.scrollTo({ top: top }) : (list.scrollTop = top);
			}
		}
	}
	window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
	window.addEventListener('resize', update);
	update();
})();

/* Contact form helpers: autofill hints, a correct error label for the
 * "Company and website" field, and focus moved to the first error on submit. */
(function () {
	var form = document.querySelector('.fl-contact-form');
	if (!form) return;
	var hints = { 'fl-name': 'name', 'fl-email': 'email', 'fl-subject': 'organization' };
	Object.keys(hints).forEach(function (n) {
		var el = form.querySelector('[name="' + n + '"]');
		if (el) el.setAttribute('autocomplete', hints[n]);
	});
	var subject = form.querySelector('[name="fl-subject"]');
	if (subject) {
		var wrap = subject.closest('.fl-input-group') || subject.parentNode;
		var err = wrap && wrap.querySelector('.fl-contact-error');
		if (err) err.textContent = 'Please add your company and website.';
	}
	var btn = form.querySelector('.fl-button');
	if (btn) btn.addEventListener('click', function () {
		setTimeout(function () {
			var bad = form.querySelector('[aria-invalid="true"], .fl-error input, .fl-error textarea');
			if (bad) bad.focus();
		}, 60);
	});
})();

/* Mobile menu: announce open/closed state and stop the page scrolling behind it. */
(function () {
	var btn = document.querySelector('.ja-nav .fl-menu-mobile-toggle');
	if (!btn) return;
	var menu = document.getElementById(btn.getAttribute('aria-controls') || '') || document.querySelector('.ja-nav .fl-menu .menu');
	function sync() {
		var open = btn.classList.contains('fl-active') && window.matchMedia('(max-width: 992px)').matches;
		btn.setAttribute('aria-expanded', open ? 'true' : 'false');
		document.documentElement.style.overflow = open ? 'hidden' : '';
	}
	btn.setAttribute('aria-expanded', 'false');
	btn.addEventListener('click', function () { setTimeout(sync, 0); setTimeout(sync, 350); });
	document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setTimeout(sync, 60); });
	window.addEventListener('resize', sync);
	if (menu) menu.addEventListener('click', function (e) { if (e.target.closest('a[href]')) { document.documentElement.style.overflow = ''; } });
})();

/* Breadcrumb on posts: drop the last crumb (it repeats the H1) and the separator before it. */
(function () {
	Array.prototype.forEach.call(document.querySelectorAll('.ja-crumbs .breadcrumb_last'), function (last) {
		var wrap = last.closest('.ja-crumbs');
		var prev = last.previousSibling;
		if (prev && prev.nodeType === 3) prev.textContent = prev.textContent.replace(/\s*»\s*$/, '');
		last.remove();
		// Only "Home" left (blog index): the breadcrumb adds nothing, so hide it.
		if (wrap && wrap.querySelectorAll('a').length < 2) wrap.style.display = 'none';
	});
})();
