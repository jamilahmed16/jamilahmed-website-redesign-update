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
	var heads = Array.prototype.filter.call(article.querySelectorAll('h2'), function (h) {
		return !h.closest(skip) && h.textContent.trim();
	});
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
		window.scrollTo({ top: h.getBoundingClientRect().top + window.pageYOffset - 24, behavior: reduce ? 'auto' : 'smooth' });
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
