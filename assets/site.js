(function () {
  // мобильное меню
  var b = document.querySelector('.burger'), m = document.getElementById('mnav');
  if (b && m) b.addEventListener('click', function () {
    var o = m.classList.toggle('open'); b.setAttribute('aria-expanded', o ? 'true' : 'false');
  });
  // cookie-уведомление
  var c = document.getElementById('cookie');
  try {
    if (c && !localStorage.getItem('kapm_cookie')) c.hidden = false;
    if (c) c.querySelectorAll('[data-c]').forEach(function (x) {
      x.addEventListener('click', function () { try { localStorage.setItem('kapm_cookie', x.dataset.c); } catch (e) {} c.hidden = true; });
    });
  } catch (e) { if (c) c.hidden = true; }
  // фильтр проектов
  document.querySelectorAll('[data-filter]').forEach(function (group) {
    group.querySelectorAll('.chip').forEach(function (chip) {
      chip.addEventListener('click', function () {
        group.querySelectorAll('.chip').forEach(function (x) { x.classList.remove('on'); });
        chip.classList.add('on'); apply();
      });
    });
  });
  function apply() {
    var sel = {};
    document.querySelectorAll('[data-filter]').forEach(function (g) { var on = g.querySelector('.chip.on'); sel[g.dataset.filter] = on ? on.dataset.v : 'all'; });
    document.querySelectorAll('[data-sector]').forEach(function (card) {
      var ok = Object.keys(sel).every(function (k) { return sel[k] === 'all' || card.dataset[k] === sel[k]; });
      card.style.display = ok ? '' : 'none';
    });
  }
  // форма заявки — отправка без перезагрузки
  var f = document.getElementById('lead');
  if (f) f.addEventListener('submit', function (e) {
    e.preventDefault();
    if (f.querySelector('.hp input') && f.querySelector('.hp input').value) return;
    var btn = f.querySelector('button[type=submit]'); btn.disabled = true;
    fetch(f.action, { method: 'POST', body: new FormData(f), headers: { Accept: 'application/json' } })
      .then(function (r) { if (!r.ok) throw 0; f.querySelector('.form-ok').style.display = 'block'; f.querySelector('.grid2').style.display = 'none'; f.querySelector('.form-foot').style.display = 'none'; f.querySelector('.chk').style.display = 'none'; })
      .catch(function () { btn.disabled = false; alert(f.dataset.err); });
  });
})();
