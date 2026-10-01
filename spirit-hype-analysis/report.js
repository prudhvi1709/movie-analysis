(() => {
  'use strict';
  const themeButton = document.querySelector('#theme');
  const filter = document.querySelector('#kind');
  const rows = [...document.querySelectorAll('#evidence-table tbody tr')];
  const count = document.querySelector('#count');
  const params = new URLSearchParams(location.search);
  const controller = new AbortController();
  const options = { signal: controller.signal };
  function applyTheme(isLight) {
    document.documentElement.dataset.theme = isLight ? 'light' : 'dark';
    themeButton.setAttribute('aria-pressed', String(isLight));
    themeButton.textContent = isLight ? 'Dark theme' : 'Light theme';
  }
  function applyFilter() {
    let visible = 0;
    for (const row of rows) {
      row.hidden = filter.value !== 'all' && row.dataset.kind !== filter.value;
      if (!row.hidden) visible += 1;
    }
    count.textContent = `${visible} of ${rows.length} selected posts`;
  }
  function updateUrl() {
    const url = new URL(location.href);
    url.searchParams.set('theme', document.documentElement.dataset.theme);
    url.searchParams.set('kind', filter.value);
    history.replaceState(null, '', url);
  }
  applyTheme(params.get('theme') === 'light');
  if ([...filter.options].some(option => option.value === params.get('kind'))) {
    filter.value = params.get('kind');
  }
  applyFilter();
  themeButton.addEventListener('click', () => {
    applyTheme(document.documentElement.dataset.theme !== 'light');
    updateUrl();
  }, options);
  filter.addEventListener('change', () => { applyFilter(); updateUrl(); }, options);
  window.addEventListener('pagehide', () => controller.abort(), { once: true });
})();
