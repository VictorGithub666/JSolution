document.addEventListener('DOMContentLoaded', function () {

  /* Preloader */
  var pre = document.getElementById('preloader');
  if (pre) {
    window.addEventListener('load', function () {
      setTimeout(function () { pre.classList.add('hidden'); }, 500);
    });
    setTimeout(function () { pre.classList.add('hidden'); }, 2500);
  }

  /* Mobile nav - FIXED */
  var toggle = document.querySelector('.mobile-toggle');
  var navmenu = document.getElementById('navmenu');
  var scrim = document.querySelector('.nav-scrim');
  var body = document.body;

  function openNav() {
    if (navmenu) navmenu.classList.add('open');
    if (scrim) scrim.classList.add('open');
    if (body) body.style.overflow = 'hidden';
  }

  function closeNav() {
    if (navmenu) navmenu.classList.remove('open');
    if (scrim) scrim.classList.remove('open');
    if (body) body.style.overflow = '';
  }

  function toggleNav() {
    if (navmenu && navmenu.classList.contains('open')) {
      closeNav();
    } else {
      openNav();
    }
  }

  if (toggle && navmenu) {
    toggle.addEventListener('click', function (e) {
      e.stopPropagation();
      toggleNav();
    });

    // Close menu when clicking on a link
    document.querySelectorAll('.navmenu a').forEach(function (a) {
      a.addEventListener('click', closeNav);
    });

    // Close menu when clicking the scrim
    if (scrim) {
      scrim.addEventListener('click', closeNav);
    }

    // Close menu on Escape key
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        closeNav();
      }
    });
  }

  /* Scroll-to-top */
  var stop = document.getElementById('scroll-top');
  window.addEventListener('scroll', function () {
    if (stop) stop.classList.toggle('show', window.scrollY > 400);
  });
  stop && stop.addEventListener('click', function (e) {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  /* Reveal on scroll */
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add('in');
          io.unobserve(en.target);
        }
      });
    }, { threshold: .15 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }

  /* Poster popup (Black Gold) */
  var posterTrigger = document.getElementById('posterTrigger');
  var posterLightbox = document.getElementById('posterLightbox');
  var posterLightboxClose = document.getElementById('posterLightboxClose');
  if (posterTrigger && posterLightbox) {
    posterTrigger.addEventListener('click', function () {
      posterLightbox.classList.add('open');
    });
    posterLightboxClose && posterLightboxClose.addEventListener('click', function () {
      posterLightbox.classList.remove('open');
    });
    posterLightbox.addEventListener('click', function (e) {
      if (e.target === posterLightbox) posterLightbox.classList.remove('open');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') posterLightbox.classList.remove('open');
    });
  }

  /* Product filter (products.html) */
  var filterBtns = document.querySelectorAll('.filter-btn');
  var productCards = document.querySelectorAll('[data-cat]');

  function applyFilter(cat) {
    filterBtns.forEach(function (b) {
      b.classList.toggle('active', b.getAttribute('data-filter') === cat);
    });
    productCards.forEach(function (card) {
      card.style.display = (cat === 'all' || card.getAttribute('data-cat') === cat) ? '' : 'none';
    });
  }

  filterBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      applyFilter(btn.getAttribute('data-filter'));
    });
  });

  if (filterBtns.length) {
    var hash = window.location.hash.replace('#', '');
    var validFilters = ['all', 'fert', 'pgpr', 'pest', 'kit'];
    if (hash && validFilters.indexOf(hash) !== -1) applyFilter(hash);
  }

  /* Order form: prefill product name + web3forms submit handling */
  document.querySelectorAll('.order-form').forEach(function (form) {
    var status = form.querySelector('.form-status');
    form.addEventListener('submit', function (e) {
      var accessKey = form.querySelector('input[name="access_key"]');
      if (!accessKey || !accessKey.value) {
        e.preventDefault();
        if (status) {
          status.textContent = 'Ordering isn\'t connected yet — please call or WhatsApp us directly using the number above.';
          status.className = 'form-status err';
        }
        return;
      }
    });
  });

  /* Generic contact form same handling */
  document.querySelectorAll('.contact-form').forEach(function (form) {
    var status = form.querySelector('.form-status');
    form.addEventListener('submit', function (e) {
      var accessKey = form.querySelector('input[name="access_key"]');
      if (!accessKey || !accessKey.value) {
        e.preventDefault();
        if (status) {
          status.textContent = 'This form isn\'t connected yet — please email jsolutionkenya@gmail.com directly.';
          status.className = 'form-status err';
        }
      }
    });
  });

});
