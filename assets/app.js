/* Papeterie Pro — scripts */
(function () {
	'use strict';

	/* Slider d'accueil */
	document.querySelectorAll('[data-slider]').forEach(function (hero) {
		var slides = hero.querySelectorAll('.hero__slide');
		var dots = hero.querySelectorAll('.hero__dots button');
		if (slides.length < 2) return;
		var i = 0, timer;
		function go(n) {
			slides[i].classList.remove('is-active');
			if (dots[i]) dots[i].classList.remove('is-active');
			i = (n + slides.length) % slides.length;
			slides[i].classList.add('is-active');
			if (dots[i]) dots[i].classList.add('is-active');
		}
		function play() { stop(); timer = setInterval(function () { go(i + 1); }, 5500); }
		function stop() { clearInterval(timer); }
		var prev = hero.querySelector('.hero__nav--prev');
		var next = hero.querySelector('.hero__nav--next');
		if (prev) prev.addEventListener('click', function () { go(i - 1); play(); });
		if (next) next.addEventListener('click', function () { go(i + 1); play(); });
		dots.forEach(function (d, n) { d.addEventListener('click', function () { go(n); play(); }); });
		hero.addEventListener('mouseenter', stop);
		hero.addEventListener('mouseleave', play);
		/* glisser au doigt */
		var x0 = null;
		hero.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
		hero.addEventListener('touchend', function (e) {
			if (x0 === null) return;
			var dx = e.changedTouches[0].clientX - x0;
			if (Math.abs(dx) > 40) { go(i + (dx < 0 ? 1 : -1)); play(); }
			x0 = null;
		});
		play();
	});

	/* Carrousels de produits */
	document.querySelectorAll('.psection, .nb-block').forEach(function (sec) {
		var track = sec.querySelector('.carousel');
		if (!track) return;
		sec.querySelectorAll('.carousel-btn').forEach(function (btn) {
			btn.addEventListener('click', function () {
				var dir = parseInt(btn.getAttribute('data-dir'), 10);
				var max = track.scrollWidth - track.clientWidth, pos = Math.abs(track.scrollLeft);
				var step = dir * Math.max(track.clientWidth * 0.8, 200);
				if (document.documentElement.dir === 'rtl') step = -step;
				if (dir > 0 && pos >= max - 4) track.scrollTo({ left: 0, behavior: 'smooth' });
				else if (dir < 0 && pos <= 4) track.scrollTo({ left: document.documentElement.dir === 'rtl' ? -max : max, behavior: 'smooth' });
				else track.scrollBy({ left: step, behavior: 'smooth' });
			});
		});
		var sync = function () { var max = track.scrollWidth - track.clientWidth; sec.querySelectorAll('.carousel-btn').forEach(function (b) { b.style.visibility = max > 4 ? '' : 'hidden'; }); };
		sync(); window.addEventListener('resize', sync);
	});

	/* Menu mobile */
	var drawer = document.querySelector('[data-drawer]');
	function setDrawer(open) {
		if (!drawer) return;
		drawer.classList.toggle('is-open', open);
		drawer.setAttribute('aria-hidden', open ? 'false' : 'true');
		document.body.classList.toggle('drawer-open', open);
	}
	document.querySelectorAll('[data-drawer-open]').forEach(function (b) { b.addEventListener('click', function () { setDrawer(true); }); });
	document.querySelectorAll('[data-drawer-close]').forEach(function (b) { b.addEventListener('click', function () { setDrawer(false); }); });
	document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setDrawer(false); });
	if (drawer) {
		drawer.querySelectorAll('.catmenu__toggle').forEach(function (t) {
			t.addEventListener('click', function () { t.parentElement.classList.toggle('is-open'); });
		});
	}

	/* En-tête collant au défilement */
	var header = document.querySelector('[data-sticky]');
	if (header) {
		var onScroll = function () { header.classList.toggle('is-stuck', window.scrollY > 160); };
		window.addEventListener('scroll', onScroll, { passive: true });
		onScroll();
	}
})();

/* ===== Librairie digitale : commandes et services par WhatsApp, recherche ===== */
(function () {
  var C = window.BOUTIQUE || {}, T = window.I18N || {}, ROOT = window.ROOT || '';
  var NUM = String(C.whatsapp || '212760923785').replace(/\D/g, '');
  function wa(msg) { return 'https://wa.me/' + NUM + (msg ? '?text=' + encodeURIComponent(msg) : ''); }
  function open(msg) { window.open(wa(msg), '_blank', 'noopener'); }
  function toast(t) { var el = document.getElementById('toast'); if (!el) return; el.textContent = t || T.toast; el.hidden = false; clearTimeout(el._t); el._t = setTimeout(function () { el.hidden = true; }, 3200); }
  document.querySelectorAll('a.js-wa, a[href^="https://wa.me/"]').forEach(function (a) { var q = a.href.split('?')[1]; a.href = wa('') + (q ? '?' + q : ''); });
  if (C.telephone) document.querySelectorAll('a[href^="tel:"]').forEach(function (a) { a.href = 'tel:' + C.telephone.replace(/[^\d+]/g, ''); if (/\d/.test(a.textContent)) { var sp = a.querySelector('span') || a; if (sp === a) { a.lastChild.textContent = ' ' + C.telephone; } else sp.textContent = C.telephone; } });
  if (C.email) document.querySelectorAll('.js-email').forEach(function (r) { r.hidden = false; var a = r.querySelector('a'); a.href = 'mailto:' + C.email; a.textContent = C.email; });
  if (C.adresse && false) document.querySelectorAll('.js-adresse').forEach(function (r) { r.hidden = false; r.querySelector('strong').textContent = C.adresse; });
  function orderMsg(name, price, qty) { return T.wa_hello + '\n- ' + qty + ' × ' + name + (price ? ' (' + price + ' ' + T.wa_unit + ')' : '') + '\n' + T.wa_name + '\n' + T.wa_addr; }
  document.addEventListener('click', function (e) {
    var a = e.target.closest('.js-order, .js-order-single, .js-service'); if (!a) return;
    e.preventDefault();
    if (a.classList.contains('js-service')) return open(T.wa_service + ' ' + a.dataset.service);
    var q = 1; if (a.classList.contains('js-order-single')) { var i = document.querySelector('input.qty'); q = Math.max(1, parseInt(i && i.value, 10) || 1); }
    var name = a.dataset.name + (a.dataset.variant ? ' — ' + a.dataset.variant : '');
    open(orderMsg(name, a.dataset.price, q));
  });
  window.LD_WA = wa;
  /* recherche */
  var box = document.getElementById('resultats');
  if (box) {
    var params = new URLSearchParams(location.search), q = (params.get('s') || '').trim(), cat = params.get('cat') || '';
    var inp = document.querySelector('.search__input'); if (inp) inp.value = q;
    var norm = function (s) { return (s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase(); };
    var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
    fetch('recherche.json').then(function (r) { return r.json(); }).then(function (D) {
      var w = norm(q).split(/\s+/).filter(Boolean);
      var hit = function (x) { var t = norm(x.n + ' ' + (x.k || '') + ' ' + (x.d || '')); return w.every(function (k) { return t.indexOf(k) > -1; }); };
      var P = D.filter(function (x) { return x.t === 'p' && hit(x) && (!cat || x.c === cat); });
      var S = cat ? [] : D.filter(function (x) { return x.t === 's' && w.length && hit(x); });
      document.getElementById('titre-recherche').textContent = q ? (T.results_for + ' « ' + q + ' » (' + (P.length + S.length) + ')') : T.all_products;
      box.innerHTML = P.map(function (p) { return '<li class="product"><a class="woocommerce-LoopProduct-link" href="' + p.u + '"><img src="' + ROOT + p.i + '" alt="" loading="lazy"><h2 class="woocommerce-loop-product__title">' + esc(p.n) + '</h2><span class="price">' + (p.o ? '<del>' + p.o + '</del> <ins>' + p.p + '</ins>' : p.p) + '</span><span class="stock-badge in">' + esc(T.in_stock) + '</span></a><a href="#" class="button add_to_cart_button js-order" data-name="' + esc(p.n) + '" data-price="' + esc(p.p) + '">' + esc(T.order) + '</a></li>'; }).join('');
      document.getElementById('resultats-services').innerHTML = S.map(function (s) { return '<article class="svc"><h3 class="svc__name">' + esc(s.n) + '</h3><p class="svc__desc">' + esc(s.d) + '</p><div class="svc__foot"><a href="#" class="svc__btn js-service" data-service="' + esc(s.n) + '">WhatsApp</a></div></article>'; }).join('');
      if (!P.length && !S.length) box.innerHTML = '<p>' + esc(T.no_result) + '</p>';
    });
  }
})();

/* ===== Variantes de couleur ===== */
(function () {
  var box = document.querySelector('[data-variants]');
  if (box) {
    var img = document.getElementById('pimg'), lab = box.querySelector('[data-vlabel]'), sku = document.getElementById('psku');
    var setColor = function (b) {
      box.querySelectorAll('.swatch').forEach(function (x) { x.classList.toggle('is-active', x === b); x.setAttribute('aria-checked', x === b ? 'true' : 'false'); });
      if (img) { img.src = b.dataset.img; }
      if (lab) lab.textContent = b.dataset.color;
      if (sku) sku.textContent = b.dataset.sku;
      document.querySelectorAll('.js-order-single, .js-add-single').forEach(function (a) { a.dataset.variant = b.dataset.color; });
      document.querySelectorAll('.js-add-single').forEach(function (a) { a.dataset.id = b.dataset.sku; a.dataset.img = b.dataset.img.replace(/^(\.\.\/)+/, ''); });
    };
    box.querySelectorAll('.swatch').forEach(function (b) { b.setAttribute('role', 'radio'); b.addEventListener('click', function () { setColor(b); }); });
    var first = box.querySelector('.swatch.is-active'); if (first) setColor(first);
  }
  /* survol des pastilles sur les cartes : aperçu de la couleur */
  document.querySelectorAll('.nb-sw .sw').forEach(function (d) {
    var li = d.closest('li'); var im = li && li.querySelector('img'); if (!im) return;
    var orig = im.getAttribute('src');
    d.addEventListener('mouseenter', function () { im.src = d.dataset.img; });
    d.addEventListener('click', function () { im.src = d.dataset.img; orig = d.dataset.img; });
    li.addEventListener('mouseleave', function () { im.src = orig; });
  });
})();

/* ===== Panier et bon de commande ===== */
(function () {
  var C = window.BOUTIQUE || {}, T = window.I18N || {}, ROOT = window.ROOT || '', LANG = window.LANG || 'fr';
  var PAY = C.paiement || {}, KEY = 'ld_cart_v1', mem = [];
  function load() { try { return JSON.parse(localStorage.getItem(KEY) || '[]') || []; } catch (e) { return mem; } }
  function save(c) { mem = c; try { localStorage.setItem(KEY, JSON.stringify(c)); } catch (e) {} badge(); }
  function money(v) { return (Math.round(v * 100) / 100).toFixed(2) + ' ' + T.cur; }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function count(c) { return c.reduce(function (n, x) { return n + x.qty; }, 0); }
  function total(c) { return c.reduce(function (n, x) { return n + x.qty * x.p; }, 0); }
  function badge() { var n = count(load()); document.querySelectorAll('[data-cart-count]').forEach(function (b) { b.textContent = n; b.hidden = !n; }); }
  function toast(html) { var el = document.getElementById('toast'); if (!el) return; el.innerHTML = html; el.hidden = false; clearTimeout(el._t); el._t = setTimeout(function () { el.hidden = true; }, 4000); }
  var pre = LANG === 'fr' ? '' : LANG + '/';
  document.addEventListener('click', function (e) {
    var a = e.target.closest('.js-add'); if (!a) return;
    e.preventDefault();
    var q = 1; if (a.classList.contains('js-add-single')) { var i = document.querySelector('input.qty'); q = Math.max(1, parseInt(i && i.value, 10) || 1); }
    var id = a.dataset.id + (a.dataset.variant ? '|' + a.dataset.variant : ''), c = load(), it = null;
    c.forEach(function (x) { if (x.key === id) it = x; });
    if (it) it.qty += q; else c.push({ key: id, sku: a.dataset.id, name: a.dataset.name, variant: a.dataset.variant || '', p: parseFloat(a.dataset.p) || 0, img: a.dataset.img, url: pre + a.dataset.url, qty: q });
    save(c);
    toast('✓ ' + esc(T.added) + ' — <a href="panier.html">' + esc(T.view_cart) + ' (' + count(c) + ')</a>');
  });
  badge();

  function lines(c, edit) {
    return c.map(function (x, n) {
      return '<div class="cline"><a class="cline__img" href="' + ROOT + x.url + '"><img src="' + ROOT + x.img + '" alt=""></a><div class="cline__info"><a href="' + ROOT + x.url + '">' + esc(x.name) + '</a>' +
        (x.variant ? '<small>' + esc(x.variant) + '</small>' : '') + '<small dir="ltr">' + esc(x.sku) + '</small><span class="cline__pu">' + money(x.p) + '</span></div>' +
        (edit ? '<div class="cline__qty"><button type="button" data-q="-1" data-n="' + n + '" aria-label="-">−</button><input type="number" min="1" value="' + x.qty + '" data-n="' + n + '" aria-label="' + esc(T.qty) + '"><button type="button" data-q="1" data-n="' + n + '" aria-label="+">+</button></div>'
              : '<span class="cline__x">× ' + x.qty + '</span>') +
        '<strong class="cline__tot">' + money(x.p * x.qty) + '</strong>' + (edit ? '<button type="button" class="cline__rm" data-rm="' + n + '" aria-label="' + esc(T.remove) + '" title="' + esc(T.remove) + '">✕</button>' : '') + '</div>';
    }).join('');
  }
  function sums(c, store) {
    return '<dl class="sumt"><dt>' + esc(T.subtotal) + ' (' + count(c) + ')</dt><dd>' + money(total(c)) + '</dd><dt>' + esc(T.shipping) + '</dt><dd>' + esc(store ? T.ship_free : T.ship_tbd) + '</dd>' +
      '<dt class="sumt__total">' + esc(T.total) + '</dt><dd class="sumt__total">' + money(total(c)) + '</dd></dl>';
  }
  function emptyMsg() { return '<div class="cart-empty"><p>' + esc(T.empty) + '</p><a class="btn btn--primary" href="boutique.html">' + esc(T.continue_) + '</a></div>'; }

  /* page panier */
  var cb = document.getElementById('cart-box');
  if (cb) {
    var draw = function () {
      var c = load();
      cb.innerHTML = c.length ? lines(c, true) : emptyMsg();
      document.getElementById('cart-sum').innerHTML = sums(c, false);
      document.getElementById('go-checkout').classList.toggle('is-disabled', !c.length);
    };
    cb.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return; var c = load();
      if (b.dataset.rm != null) c.splice(+b.dataset.rm, 1);
      else if (b.dataset.q) { var x = c[+b.dataset.n]; x.qty = Math.max(1, x.qty + (+b.dataset.q)); }
      save(c); draw();
    });
    cb.addEventListener('change', function (e) { var i = e.target; if (i.dataset.n == null) return; var c = load(); c[+i.dataset.n].qty = Math.max(1, parseInt(i.value, 10) || 1); save(c); draw(); });
    draw();
  }

  /* bon de commande */
  var f = document.getElementById('coform');
  if (f) {
    var c = load(), sumBox = document.getElementById('co-sum');
    var labelOf = function (name) { var i = f.querySelector('input[name="' + name + '"]:checked'); return i ? i.closest('label').querySelector('strong').textContent : ''; };
    var opt = function (v) { return f.querySelector('.opt[data-opt="' + v + '"]'); };
    var card = PAY.carte || {}, bank = PAY.virement || {};
    if (!card.actif) { var o = opt('card'); o.classList.add('is-off'); o.querySelector('input').disabled = true; o.querySelector('strong').insertAdjacentHTML('beforeend', ' <em class="soon">' + esc(T.pay_card_soon) + '</em>'); }
    else opt('card').querySelector('small').textContent += ' ' + T.pay_card_link;
    if (bank.actif === false) opt('bank').hidden = true;
    if (PAY.livraison === false) opt('cod').hidden = true;
    if (PAY.magasin === false) opt('store').hidden = true;
    var sync = function () {
      var store = f.ship.value === 'store';
      opt('store').hidden = !store || PAY.magasin === false; opt('cod').hidden = store || PAY.livraison === false;
      var cur = f.querySelector('input[name="pay"]:checked');
      if (!cur || cur.closest('.opt').hidden) { var first = Array.prototype.filter.call(f.querySelectorAll('input[name="pay"]'), function (i) { return !i.disabled && !i.closest('.opt').hidden; })[0]; if (first) first.checked = true; }
      f.querySelectorAll('[name="city"],[name="addr"]').forEach(function (i) { i.required = !store; i.closest('.fld').classList.toggle('is-opt', store); });
      f.querySelectorAll('.opt').forEach(function (l) { l.classList.toggle('is-on', l.querySelector('input').checked); });
      sumBox.innerHTML = (c.length ? '<div class="co__lines">' + lines(c, false) + '</div>' : '') + sums(c, store);
    };
    f.addEventListener('change', sync); sync();
    if (!c.length) { f.outerHTML = emptyMsg(); }
    else f.addEventListener('submit', function (e) {
      e.preventDefault();
      var bad = Array.prototype.filter.call(f.querySelectorAll('[required]'), function (i) { return i.type === 'checkbox' ? !i.checked : !i.value.trim(); });
      f.querySelectorAll('.fld, .co__accept').forEach(function (x) { x.classList.remove('is-bad'); });
      bad.forEach(function (i) { (i.closest('.fld') || i.closest('.co__accept')).classList.add('is-bad'); });
      document.getElementById('co-err').hidden = !bad.length;
      if (bad.length) { bad[0].focus(); return; }
      var d = new Date(), no = 'LD-' + String(d.getFullYear()).slice(2) + ('0' + (d.getMonth() + 1)).slice(-2) + ('0' + d.getDate()).slice(-2) + '-' + Math.floor(1000 + Math.random() * 9000);
      var store = f.ship.value === 'store', pay = f.pay.value;
      var msg = T.wa_order + '\n' + T.order_no + ' ' + no + '\n\n' +
        c.map(function (x) { return '• ' + x.qty + ' × ' + x.name + (x.variant ? ' (' + x.variant + ')' : '') + ' [' + x.sku + '] — ' + money(x.p * x.qty); }).join('\n') +
        '\n\n' + T.wa_total + ' : ' + money(total(c)) + (store ? '' : ' + ' + T.shipping.toLowerCase()) +
        '\n' + T.wa_ship + ' : ' + labelOf('ship') + '\n' + T.wa_pay + ' : ' + labelOf('pay') +
        '\n\n' + T.wa_client + ' : ' + f.elements['name'].value.trim() + '\n' + T.f_phone + ' : ' + f.phone.value.trim() +
        (store ? '' : '\n' + T.f_city + ' : ' + f.city.value.trim() + '\n' + T.f_addr + ' : ' + f.addr.value.trim()) +
        (f.note.value.trim() ? '\n' + T.f_note.replace(/\s*\(.*\)/, '') + ' : ' + f.note.value.trim() : '');
      var link = window.LD_WA(msg);
      document.getElementById('co-no').textContent = no;
      document.getElementById('co-wa').href = link;
      if (pay === 'bank') {
        var bb = document.getElementById('co-bank'); bb.hidden = false;
        bb.innerHTML = bank.rib ? '<h3>' + esc(T.bank_info) + '</h3><dl>' + (bank.titulaire ? '<dt>' + esc(T.bank_holder) + '</dt><dd>' + esc(bank.titulaire) + '</dd>' : '') + (bank.banque ? '<dt>' + esc(T.bank_bank) + '</dt><dd>' + esc(bank.banque) + '</dd>' : '') +
          '<dt>' + esc(T.bank_rib) + '</dt><dd dir="ltr"><strong>' + esc(bank.rib) + '</strong></dd></dl><p>' + esc(T.bank_ref) + '</p>' : '<p>' + esc(T.bank_wa) + '</p>';
      }
      if (pay === 'card' && card.lien) { var cp = document.getElementById('co-pay'); cp.href = card.lien; cp.hidden = false; }
      f.hidden = true; document.getElementById('codone').hidden = false;
      document.querySelectorAll('.costeps li').forEach(function (li, n) { li.className = n < 2 ? 'is-done' : 'is-on'; });
      save([]); window.scrollTo({ top: 0, behavior: 'smooth' });
      window.open(link, '_blank', 'noopener');
    });
  }
})();

/* ===== Mode nuit ===== */
(function () {
  var root = document.documentElement;
  function set(dark) {
    if (dark) root.setAttribute('data-theme', 'dark'); else root.removeAttribute('data-theme');
    try { localStorage.setItem('ld_theme', dark ? 'dark' : 'light'); } catch (e) {}
    document.querySelectorAll('[data-theme-toggle]').forEach(function (b) { b.setAttribute('aria-pressed', dark ? 'true' : 'false'); });
  }
  document.querySelectorAll('[data-theme-toggle]').forEach(function (b) {
    b.setAttribute('aria-pressed', root.getAttribute('data-theme') === 'dark' ? 'true' : 'false');
    b.addEventListener('click', function () { set(root.getAttribute('data-theme') !== 'dark'); });
  });
  /* suivre le réglage du téléphone / ordinateur tant que le visiteur n'a pas choisi */
  if (window.matchMedia) {
    var mq = matchMedia('(prefers-color-scheme: dark)');
    var follow = function () {
      var t = null; try { t = localStorage.getItem('ld_theme'); } catch (e) {}
      if (t) return;
      if (mq.matches) root.setAttribute('data-theme', 'dark'); else root.removeAttribute('data-theme');
      document.querySelectorAll('[data-theme-toggle]').forEach(function (b) { b.setAttribute('aria-pressed', mq.matches ? 'true' : 'false'); });
    };
    if (mq.addEventListener) mq.addEventListener('change', follow); else if (mq.addListener) mq.addListener(follow);
  }
})();

/* ===== Vidéo itinéraire : choix de la langue ===== */
(function () {
  var v = document.getElementById('vroute'); if (!v) return;
  document.querySelectorAll('.vtab').forEach(function (b) {
    b.addEventListener('click', function () {
      document.querySelectorAll('.vtab').forEach(function (x) { x.classList.toggle('is-on', x === b); x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      var play = !v.paused; v.pause(); v.poster = b.dataset.vposter; v.querySelector('source').src = b.dataset.vsrc; v.load(); if (play) v.play();
    });
  });
})();

/* ===== Bannière : une nouvelle palette de couleurs à chaque passage ===== */
(function () {
  var slides = document.querySelectorAll('.nb-hero .hero__slide');
  if (!slides.length) return;
  var N = 4;
  slides.forEach(function (s) {
    s.dataset.pal = '0';
    var was = s.classList.contains('is-active');
    new MutationObserver(function () {
      var now = s.classList.contains('is-active');
      if (now && !was) s.dataset.pal = String((parseInt(s.dataset.pal, 10) + 1) % N);
      was = now;
    }).observe(s, { attributes: true, attributeFilter: ['class'] });
  });
})();
