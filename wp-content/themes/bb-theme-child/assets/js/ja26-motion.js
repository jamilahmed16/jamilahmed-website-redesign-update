/* ja26 motion layer (GSAP 3 + ScrollTrigger + SplitText, self-hosted).
 * Each page gets its own authored moment, built from what the page says:
 *   home        – the AI answer console (Google / ChatGPT / Perplexity, cited or not)
 *   audit       – the report is scanned and checked, section by section
 *   enterprise  – the priority matrix fills in priority order; the migration timeline is drawn by scroll
 *   b2b         – the AI shortlist streams in; the buying journey lights stage by stage
 *   pharma      – the review card is verified; each review step is signed off by scroll
 *   timelines   – career years light up as you read down them
 * Content is readable without JS. Under prefers-reduced-motion everything is shown at its end state. */
(function () {
	'use strict';
	var html = document.documentElement;
	function reveal() { html.classList.remove('ja-m'); }
	if (!document.querySelector('.ja26-root')) { reveal(); return; }
	var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
	var fine = window.matchMedia('(pointer: fine)').matches;
	var $ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
	var gsap = window.gsap;

	/* The console works with or without GSAP. */
	$('[data-console]').forEach(function (c) { consoleInit(c); });
	$('[data-brief]').forEach(function (b) { briefInit(b); });

	if (!gsap) { reveal(); return; }
	var ST = window.ScrollTrigger;
	if (ST) gsap.registerPlugin(ST);
	if (window.SplitText) gsap.registerPlugin(window.SplitText);

	/* Reading progress. */
	var bar = document.createElement('div');
	bar.className = 'ja-progress';
	bar.setAttribute('aria-hidden', 'true');
	document.body.appendChild(bar);
	if (ST) ST.create({ start: 0, end: 'max', onUpdate: function (s) { gsap.set(bar, { scaleX: s.progress }); } });

	if (reduce) { reveal(); return; }

	/* ---------- Hero: headline rises from a mask, then the page's own artefact plays ---------- */
	var hero = $('.ja26-root').filter(function (r) { return r.querySelector('h1'); })[0];
	var h1 = hero && hero.querySelector('h1');
	var tl = gsap.timeline({ defaults: { ease: 'power3.out' } });
	if (h1 && window.SplitText) {
		var split = new window.SplitText(h1.querySelector('.fl-heading-text') || h1, { type: 'words', mask: 'words', wordsClass: 'ja-w' });
		gsap.set(h1, { opacity: 1 });
		tl.from(split.words, { yPercent: 110, duration: 0.9, stagger: 0.06 });
	} else if (h1) gsap.set(h1, { opacity: 1 });
	reveal();

	if (hero) {
		var follow = $('.ja-lead, .fl-button-wrap', hero);
		if (follow.length) tl.from(follow, { opacity: 0, y: 14, duration: 0.6, stagger: 0.06, clearProps: 'all' }, '-=0.6');
		var media = $('.ja-hero-photo, .ja-cutout', hero);
		if (media.length) tl.from(media, { clipPath: 'inset(100% 0 0 0)', duration: 1.1, ease: 'expo.out', clearProps: 'clipPath' }, 0.1);
		var art = hero.querySelector('.ja-art');
		if (art) heroArt(art, tl);
		if (fine) glow(hero);
	}

	if (fine) $('.ja-brief-row').forEach(glow);
	$('.ja-brief-title').forEach(function (t) {
		if (!ST || !window.SplitText || t.getBoundingClientRect().top < innerHeight) return;
		var sp = new window.SplitText(t.querySelector('.fl-heading-text') || t, { type: 'words', mask: 'words' });
		gsap.from(sp.words, { yPercent: 110, duration: 0.9, stagger: 0.05, ease: 'power3.out', scrollTrigger: { trigger: t, start: 'top 80%', once: true } });
	});

	if (!ST) return;

	/* ---------- Scroll-linked pieces ---------- */
	var mm = gsap.matchMedia();

	/* Timelines: each year lights when it reaches the reading line. */
	$('.ja-timeline').forEach(function (list) {
		$('li', list).forEach(function (li) {
			ST.create({ trigger: li, start: 'top 72%', end: 'bottom 72%', toggleClass: { targets: li, className: 'is-read' }, onLeave: function () { li.classList.add('is-past'); }, onEnterBack: function () { li.classList.remove('is-past'); } });
		});
		list.classList.add('ja-live');
	});

	/* Enterprise migration: the line is drawn phase by phase as you scroll. */
	$('.fl-row').forEach(function (row) {
		var cols = $('.ja-rule > .fl-col-content', row);
		if (cols.length < 4) return;
		row.classList.add('ja-rule-live');
		var t = gsap.timeline({ scrollTrigger: { trigger: cols[0], start: 'top 80%', end: 'top 30%', scrub: 0.6 } });
		cols.forEach(function (c) {
			t.fromTo(c, { '--p': 0 }, { '--p': 1, ease: 'none', duration: 1, onComplete: function () { c.classList.add('is-on'); }, onReverseComplete: function () { c.classList.remove('is-on'); } });
		});
	});

	/* Pharma review workflow: each step is signed off in order. */
	$('.ja-flow').forEach(function (flow) {
		var steps = $('li', flow);
		flow.classList.add('ja-flow-live');
		var t = gsap.timeline({ scrollTrigger: { trigger: flow, start: 'top 80%', end: 'top 35%', scrub: 0.6 } });
		steps.forEach(function (li) {
			t.fromTo(li, { '--p': 0 }, { '--p': 1, ease: 'none', duration: 1, onComplete: function () { li.classList.add('is-on'); }, onReverseComplete: function () { li.classList.remove('is-on'); } });
		});
	});

	/* B2B buying journey: the stage being read is the one that is lit. */
	$('.ja-table').forEach(function (t) {
		if (t.classList.contains('ja-table-dark')) return;
		$('tbody tr', t).forEach(function (tr) {
			ST.create({ trigger: tr, start: 'top 62%', end: 'bottom 62%', toggleClass: { targets: tr, className: 'is-on' } });
		});
	});

	/* Audit example finding: the rows are written in, then the impact pill lands. */
	$('.ja-art-finding').forEach(function (art) {
		var parts = $('.ja-art-t, dt, dd', art);
		var pill = art.querySelector('.ja-pill-hi');
		var t = gsap.timeline({ scrollTrigger: { trigger: art, start: 'top 75%', once: true } });
		t.from(parts, { opacity: 0, x: -10, duration: 0.45, stagger: 0.06, ease: 'power2.out', clearProps: 'all' });
		if (pill) t.from(pill, { scale: 1.8, opacity: 0, duration: 0.5, ease: 'back.out(3)', clearProps: 'all' }, '-=0.2');
	});

	/* Industries: the strip follows the reader's scroll speed and direction. */
	$('.ja-marquee-track').forEach(function (track) {
		mm.add('(min-width: 769px)', function () {
			track.style.animation = 'none';
			var loop = gsap.fromTo(track, { xPercent: -50 }, { xPercent: 0, duration: 48, ease: 'none', repeat: -1 });
			var st = ST.create({ onUpdate: function (s) {
				var v = gsap.utils.clamp(-6, 6, s.getVelocity() / 250);
				gsap.to(loop, { timeScale: v === 0 ? 1 : v, duration: 0.25, overwrite: true });
				gsap.to(loop, { timeScale: s.direction, duration: 1.2, delay: 0.25 });
			} });
			var m = track.closest('.ja-marquee');
			var stop = function () { gsap.to(loop, { timeScale: 0, duration: 0.5, overwrite: true }); };
			var go = function () { gsap.to(loop, { timeScale: 1, duration: 0.5, overwrite: true }); };
			m.addEventListener('mouseenter', stop); m.addEventListener('mouseleave', go);
			return function () { loop.kill(); st.kill(); track.style.animation = ''; m.removeEventListener('mouseenter', stop); m.removeEventListener('mouseleave', go); };
		});
	});

	/* Latest posts: the image draws open as the card arrives. */
	$('.ja-posts').forEach(function (grid) {
		var imgs = $('.fl-post-grid-image, .fl-post-column img', grid).filter(function (x) { return x.getBoundingClientRect().top > innerHeight; });
		if (!imgs.length) return;
		gsap.set(imgs, { clipPath: 'inset(0 0 100% 0)' });
		ST.batch(imgs, { start: 'top 90%', once: true, onEnter: function (b) { gsap.to(b, { clipPath: 'inset(0 0 0% 0)', duration: 1, stagger: 0.12, ease: 'expo.out', clearProps: 'clipPath' }); } });
	});

	window.addEventListener('load', function () { ST.refresh(); });

	/* ================= helpers ================= */

	function heroArt(art, tl) {
		var k = art.querySelector('.ja-art-k');
		if (art.classList.contains('ja-art-doc')) {
			/* Audit: a scan line passes down the report and checks each section. */
			var rows = $('.ja-art-toc li', art);
			var scan = document.createElement('span');
			scan.className = 'ja-scan';
			art.appendChild(scan);
			tl.from([k, art.querySelector('.ja-art-t')], { opacity: 0, y: 8, duration: 0.4, stagger: 0.08 }, '-=0.4')
			  .addLabel('scan')
			  .fromTo(scan, { top: '0%', opacity: 1 }, { top: '100%', duration: 2.2, ease: 'none' })
			  .to(scan, { opacity: 0, duration: 0.3 });
			var step = 2.2 / rows.length;
			rows.forEach(function (li, i) {
				tl.call(function () { li.classList.add('is-checked'); }, null, 'scan+=' + ((i + 0.6) * step).toFixed(2));
			});
		} else if (art.classList.contains('ja-art-matrix')) {
			/* Enterprise: quadrants appear in the order you would act on them. */
			var q = ['.q1', '.q3', '.q2', '.q4'].map(function (s) { return art.querySelector('.ja-mx-q' + s); }).filter(Boolean);
			tl.from(k, { opacity: 0, duration: 0.3 }, '-=0.4')
			  .from(q, { opacity: 0, scale: 0.92, duration: 0.5, stagger: 0.28, ease: 'back.out(1.6)', clearProps: 'all' })
			  .from($('.ja-mx-q i', art), { opacity: 0, x: -6, duration: 0.3, stagger: 0.08, clearProps: 'all' }, '-=0.6');
			$('.ja-mx-q', art).forEach(function (cell) {
				cell.addEventListener('pointerenter', function () { art.classList.add('is-focus'); cell.classList.add('is-hot'); });
				cell.addEventListener('pointerleave', function () { art.classList.remove('is-focus'); cell.classList.remove('is-hot'); });
			});
		} else if (art.classList.contains('ja-art-chat')) {
			/* B2B: the question is typed, the shortlist streams in, then the empty slot asks for you. */
			var qEl = art.querySelector('.ja-art-q'), ans = art.querySelector('.ja-art-ans');
			var src = $('.ja-art-src li', art), you = art.querySelector('.ja-art-src .you');
			var qText = qEl.textContent, typed = { n: 0 };
			qEl.style.minHeight = qEl.offsetHeight + 'px';
			var words = wrapWords(ans);
			tl.from(k, { opacity: 0, duration: 0.3 }, '-=0.4')
			  .fromTo(typed, { n: 0 }, { n: qText.length, duration: 1.2, ease: 'none', onStart: function () { qEl.classList.add('is-typing'); },
				onUpdate: function () { qEl.textContent = qText.slice(0, Math.round(typed.n)); },
				onComplete: function () { qEl.textContent = qText; qEl.classList.remove('is-typing'); } })
			  .from(words, { opacity: 0, duration: 0.05, stagger: 0.035, ease: 'none' }, '+=0.25')
			  .from(src, { opacity: 0, y: 8, duration: 0.35, stagger: 0.18, clearProps: 'all' });
			if (you) tl.fromTo(you, { boxShadow: '0 0 0 0 rgba(175,130,75,.8)' }, { boxShadow: '0 0 0 12px rgba(175,130,75,0)', duration: 1.2, repeat: 3, ease: 'power2.out' });
		} else if (art.classList.contains('ja-art-review')) {
			/* Pharma: the trust signals are written in, then the review is verified. */
			var dts = $('dt, dd', art);
			var stamp = document.createElement('span');
			stamp.className = 'ja-stamp';
			stamp.textContent = 'Reviewed';
			var reviewed = $('dd', art)[1];
			if (reviewed) reviewed.appendChild(stamp);
			tl.from([k, art.querySelector('.ja-art-t')], { opacity: 0, y: 8, duration: 0.4, stagger: 0.08 }, '-=0.4')
			  .from(dts, { opacity: 0, x: -8, duration: 0.35, stagger: 0.07, clearProps: 'all' })
			  .from(stamp, { opacity: 0, scale: 2.2, rotate: -14, duration: 0.45, ease: 'back.out(2.5)' });
		}
	}

	function wrapWords(el) {
		var out = [];
		var text = el.textContent;
		el.textContent = '';
		text.split(/(\s+)/).forEach(function (w) {
			if (/^\s+$/.test(w) || !w) { el.appendChild(document.createTextNode(w)); return; }
			var s = document.createElement('span');
			s.textContent = w;
			el.appendChild(s);
			out.push(s);
		});
		return out;
	}

	function glow(hero) {
		hero.classList.add('ja-glow');
		var gx = gsap.quickTo(hero, '--gx', { duration: 0.6, ease: 'power3' });
		var gy = gsap.quickTo(hero, '--gy', { duration: 0.6, ease: 'power3' });
		hero.addEventListener('pointermove', function (e) {
			var r = hero.getBoundingClientRect();
			gx(((e.clientX - r.left) / r.width) * 100);
			gy(((e.clientY - r.top) / r.height) * 100);
		});
	}

	/* ---------- Home: the AI answer console ---------- */
	function consoleInit(c) {
		var DATA = {
			google: {
				label: 'AI Overview',
				off: ['Top ERP implementation partners for mid-size manufacturers include Corvane and Meridian Works, both with strong shop-floor integration records.',
					['corvane.com: Manufacturing ERP', 'meridianworks.com: Partner directory', 'Peer review site: ERP partners 2026']],
				on: ['Top ERP implementation partners for mid-size manufacturers include Corvane, Your company and Meridian Works. Your company publishes implementation benchmarks by plant size.',
					['corvane.com: Manufacturing ERP', 'yourcompany.com: ERP implementation benchmarks', 'meridianworks.com: Partner directory']]
			},
			chatgpt: {
				label: 'Answer',
				off: ['For a mid-size manufacturer, three partners come up most often in reviews and case studies: Corvane, Meridian Works and Halden Group. Corvane is strongest on shop-floor integrations...',
					['Corvane: manufacturing case study', 'Gartner peer reviews', 'Halden Group: ERP buyer guide']],
				on: ['For a mid-size manufacturer, the partners cited most often are Corvane, Your company and Meridian Works. Your company stands out for published go-live timelines and named client results...',
					['Your company: go-live timelines by plant size', 'Corvane: manufacturing case study', 'Gartner peer reviews']]
			},
			perplexity: {
				label: 'Answer with sources',
				off: ['Corvane [1] and Meridian Works [2] are the most recommended partners for manufacturers with 200 to 1,000 staff. Halden Group [3] is often chosen for multi-site rollouts.',
					['corvane.com', 'meridianworks.com', 'haldengroup.com']],
				on: ['Corvane [1] and Your company [2] are the most recommended partners for manufacturers with 200 to 1,000 staff, with Your company cited for its original benchmark data [2].',
					['corvane.com', 'yourcompany.com', 'meridianworks.com']]
			}
		};
		var tabs = $('[role="tab"]', c), toggle = c.querySelector('[data-cited]');
		var aEl = c.querySelector('[data-a]'), srcEl = c.querySelector('[data-src]');
		var state = { tab: 'chatgpt', on: false };
		c.classList.add('is-live');

		function render(animate) {
			var d = DATA[state.tab][state.on ? 'on' : 'off'];
			c.setAttribute('data-surface', state.tab);
			c.classList.toggle('is-cited', state.on);
			aEl.innerHTML = '<p class="ja-console-label">' + DATA[state.tab].label + '</p><p class="ja-console-text"></p>';
			var p = aEl.querySelector('.ja-console-text');
			p.innerHTML = d[0].replace(/Your company|yourcompany\.com/g, '<mark>$&</mark>');
			srcEl.innerHTML = d[1].map(function (s) { return '<li' + (/[Yy]our ?company/.test(s) ? ' class="you"' : '') + '>' + s + '</li>'; }).join('');
			if (!animate || reduce || !window.gsap) return;
			var w = wrapWordsKeepMarks(p);
			window.gsap.killTweensOf(w);
			window.gsap.from(w, { opacity: 0, duration: 0.05, stagger: 0.025, ease: 'none' });
			window.gsap.from(srcEl.children, { opacity: 0, y: 6, duration: 0.3, stagger: 0.1, delay: w.length * 0.025, clearProps: 'all' });
		}
		tabs.forEach(function (t, i) {
			t.addEventListener('click', function () { select(i, true); });
			t.addEventListener('keydown', function (e) {
				var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
				if (!d) return;
				e.preventDefault();
				var n = (i + d + tabs.length) % tabs.length;
				select(n, true); tabs[n].focus();
			});
		});
		function select(i, animate) {
			tabs.forEach(function (t, j) { t.setAttribute('aria-selected', j === i ? 'true' : 'false'); t.tabIndex = j === i ? 0 : -1; });
			state.tab = tabs[i].getAttribute('data-tab');
			render(animate);
		}
		toggle.addEventListener('click', function () {
			state.on = !state.on;
			toggle.setAttribute('aria-pressed', state.on ? 'true' : 'false');
			render(true);
		});
		select(1, false);

		/* First view: play the answer once when the console scrolls in, then nudge the toggle. */
		if (!reduce && window.gsap && window.ScrollTrigger) {
			window.ScrollTrigger.create({ trigger: c, start: 'top 75%', once: true, onEnter: function () {
				render(true);
				window.gsap.fromTo(toggle, { boxShadow: '0 0 0 0 rgba(175,130,75,.8)' }, { boxShadow: '0 0 0 10px rgba(175,130,75,0)', duration: 1.1, repeat: 2, delay: 2.4 });
			} });
		}
	}


	/* ---------- Closing call to action: two clicks write the first message ---------- */
	function briefInit(b) {
		var NEED = {
			audit: 'an SEO and AI search audit', enterprise: 'help with enterprise SEO',
			b2b: 'SEO and AI search for our B2B / SaaS company', pharma: 'SEO for a pharma or healthcare brand',
			unsure: 'advice on where to start with SEO and AI search'
		};
		var NOW = {
			falling: 'our organic traffic is falling', ai: "competitors are cited in AI answers and we aren't",
			migration: 'we have a migration or redesign coming up', scratch: "we're starting from scratch"
		};
		var st = { need: b.getAttribute('data-pre') || '', now: '' };
		var out = b.querySelector('[data-out]'), send = b.querySelector('[data-send]');
		var typing;
		b.classList.add('is-live');
		function msg() {
			var need = st.need ? NEED[st.need] : 'help with SEO and AI search';
			var t = 'Hi Jamil, we are looking for ' + need + '.';
			if (st.now) t += ' Right now ' + NOW[st.now] + '.';
			return t + ' Could we talk about where to start?';
		}
		function render(animate) {
			$('[data-need]', b).forEach(function (c) { c.setAttribute('aria-pressed', c.getAttribute('data-need') === st.need ? 'true' : 'false'); });
			$('[data-now]', b).forEach(function (c) { c.setAttribute('aria-pressed', c.getAttribute('data-now') === st.now ? 'true' : 'false'); });
			var text = msg();
			send.href = '/contact/?brief=' + encodeURIComponent(text);
			b.classList.toggle('is-ready', !!(st.need && st.now));
			clearInterval(typing);
			if (!animate || reduce) { out.textContent = text; return; }
			/* Keep what is unchanged, type the rest. */
			var cur = out.textContent, i = 0;
			while (i < cur.length && cur[i] === text[i]) i++;
			out.classList.add('is-typing');
			typing = setInterval(function () {
				i += 2;
				out.textContent = text.slice(0, i);
				if (i >= text.length) { out.textContent = text; out.classList.remove('is-typing'); clearInterval(typing); }
			}, 16);
		}
		b.addEventListener('click', function (e) {
			var c = e.target.closest('.ja-chip');
			if (!c) return;
			if (c.hasAttribute('data-need')) st.need = st.need === c.getAttribute('data-need') ? '' : c.getAttribute('data-need');
			else st.now = st.now === c.getAttribute('data-now') ? '' : c.getAttribute('data-now');
			render(true);
		});
		render(false);
	}

	function wrapWordsKeepMarks(p) {
		var out = [];
		Array.prototype.slice.call(p.childNodes).forEach(function (n) {
			if (n.nodeType === 1) { out.push(n); return; }
			var frag = document.createDocumentFragment();
			n.textContent.split(/(\s+)/).forEach(function (w) {
				if (!w || /^\s+$/.test(w)) { frag.appendChild(document.createTextNode(w)); return; }
				var s = document.createElement('span'); s.textContent = w; frag.appendChild(s); out.push(s);
			});
			p.replaceChild(frag, n);
		});
		return out;
	}
})();
