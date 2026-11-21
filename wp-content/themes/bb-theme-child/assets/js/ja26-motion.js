/* ja26 motion layer (GSAP 3 + ScrollTrigger + SplitText, self-hosted).
 * Rules: content is readable without JS; nothing moves under prefers-reduced-motion;
 * only elements below the fold start hidden, so there is no flash and no layout shift. */
(function () {
	'use strict';
	var html = document.documentElement;
	function reveal() { html.classList.remove('ja-m'); }
	if (!document.querySelector('.ja26-root') || !window.gsap) { reveal(); return; }
	var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

	var gsap = window.gsap;
	if (window.ScrollTrigger) gsap.registerPlugin(window.ScrollTrigger);
	if (window.SplitText) gsap.registerPlugin(window.SplitText);
	var ST = window.ScrollTrigger;
	var $ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

	/* 1. Reading progress: a thin brass line under the sticky header. */
	var bar = document.createElement('div');
	bar.className = 'ja-progress';
	bar.setAttribute('aria-hidden', 'true');
	document.body.appendChild(bar);
	if (ST) {
		gsap.set(bar, { scaleX: 0 });
		ST.create({ start: 0, end: 'max', onUpdate: function (s) { gsap.set(bar, { scaleX: s.progress }); } });
	}

	if (reduce) { reveal(); return; }

	/* 2. First-screen headline: words rise out of a mask, then the lead and buttons follow. */
	var hero = $('.ja26-root').filter(function (r) { return r.querySelector('h1'); })[0];
	var h1 = hero && hero.querySelector('h1');
	var tl = gsap.timeline({ defaults: { ease: 'power3.out' } });
	if (h1 && window.SplitText) {
		var split = new window.SplitText(h1.querySelector('.fl-heading-text') || h1, { type: 'words', mask: 'words', wordsClass: 'ja-w' });
		gsap.set(h1, { opacity: 1 });
		tl.from(split.words, { yPercent: 110, duration: 0.9, stagger: 0.06 });
	} else if (h1) {
		gsap.set(h1, { opacity: 1 });
	}
	reveal();
	if (hero) {
		var follow = $('.ja-lead, .fl-button-wrap, .ja-hero-photo, .ja-art-wrap', hero);
		if (follow.length) tl.from(follow, { opacity: 0, y: 18, duration: 0.7, stagger: 0.08, clearProps: 'transform,opacity' }, h1 ? '-=0.55' : 0);
		/* Hero illustrations assemble line by line, like a report being written. */
		var art = hero.querySelector('.ja-art');
		if (art) {
			var parts = $('.ja-art-k, .ja-art-t, .ja-art-toc li, .ja-mx-q, .ja-art-q, .ja-art-ans, .ja-art-src li, dt, dd', art);
			tl.from(parts, { opacity: 0, x: -10, duration: 0.45, stagger: 0.07, clearProps: 'transform,opacity' }, '-=0.3');
			var you = art.querySelector('.ja-art-src .you');
			if (you) tl.fromTo(you, { boxShadow: '0 0 0 0 rgba(184,137,74,0.7)' }, { boxShadow: '0 0 0 10px rgba(184,137,74,0)', duration: 1.1, repeat: 2, ease: 'power2.out' });
		}
		/* Desktop: a soft brass light follows the pointer across the dark hero. */
		if (window.matchMedia('(pointer: fine)').matches) {
			hero.classList.add('ja-glow');
			var gx = gsap.quickTo(hero, '--gx', { duration: 0.6, ease: 'power3' });
			var gy = gsap.quickTo(hero, '--gy', { duration: 0.6, ease: 'power3' });
			hero.addEventListener('pointermove', function (e) {
				var r = hero.getBoundingClientRect();
				gx(((e.clientX - r.left) / r.width) * 100);
				gy(((e.clientY - r.top) / r.height) * 100);
			});
		}
	}

	if (!ST) return;

	/* Only animate what the reader has not seen yet. */
	function below(el) { return el.getBoundingClientRect().top > window.innerHeight * 0.92; }

	/* 3. Section headings and their content rise in as they enter. */
	var groups = [
		'.fl-row:not(.ja26-root) .fl-heading:not(.ja-dup-title)',
		'.ja-cred, .ja-recognition .ja-hair > .fl-col-content',
		'.ja-defs .ja-hair > .fl-col-content, .ja-work .fl-col-content > .fl-module',
		'.ja-acc', '.ja-posts .fl-post-column, .ja-posts .fl-post-grid-post',
		'.ja-ways dt, .ja-ways dd', '.ja-portrait', '.ja-list li'
	];
	groups.forEach(function (sel) {
		var els = $(sel).filter(function (el) { return !el.closest('.ja-header, .ja-footer, header, footer') && below(el); });
		if (!els.length) return;
		gsap.set(els, { opacity: 0, y: 24 });
		ST.batch(els, {
			start: 'top 88%', once: true,
			onEnter: function (b) { gsap.to(b, { opacity: 1, y: 0, duration: 0.7, stagger: 0.07, ease: 'power3.out', clearProps: 'transform,opacity' }); }
		});
	});

	/* 4. Step sequences draw left to right: migration timeline, review workflow, tables. */
	$('.ja-flow').forEach(function (flow) {
		var steps = $('li', flow);
		if (!below(flow)) return;
		gsap.set(steps, { opacity: 0, y: 16 });
		gsap.to(steps, { opacity: 1, y: 0, duration: 0.6, stagger: 0.16, ease: 'power2.out', clearProps: 'transform,opacity',
			scrollTrigger: { trigger: flow, start: 'top 82%', once: true } });
	});
	$('.fl-row').forEach(function (row) {
		var rules = $('.ja-rule > .fl-col-content', row);
		if (rules.length < 2 || !below(rules[0])) return;
		gsap.set(rules, { opacity: 0, y: 16 });
		gsap.to(rules, { opacity: 1, y: 0, duration: 0.6, stagger: 0.15, ease: 'power2.out', clearProps: 'transform,opacity',
			scrollTrigger: { trigger: rules[0], start: 'top 85%', once: true } });
	});
	$('.ja-table').forEach(function (t) {
		var rows = $('tbody tr', t);
		if (!below(t)) return;
		gsap.set(rows, { opacity: 0, x: -12 });
		gsap.to(rows, { opacity: 1, x: 0, duration: 0.5, stagger: 0.08, ease: 'power2.out', clearProps: 'transform,opacity',
			scrollTrigger: { trigger: t, start: 'top 85%', once: true } });
	});

	/* 5. Illustrations further down the page (the audit's example finding). */
	$('.ja-art').forEach(function (art) {
		if (art.closest('.ja26-root') || !below(art)) return;
		var parts = $('.ja-art-k, .ja-art-t, dt, dd', art);
		gsap.set(parts, { opacity: 0, x: -10 });
		gsap.to(parts, { opacity: 1, x: 0, duration: 0.45, stagger: 0.06, ease: 'power2.out', clearProps: 'transform,opacity',
			scrollTrigger: { trigger: art, start: 'top 80%', once: true } });
	});

	/* Builder modules can change height after fonts load. */
	window.addEventListener('load', function () { ST.refresh(); });
})();
