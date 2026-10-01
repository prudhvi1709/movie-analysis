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
  const eventDetails = [...document.querySelectorAll('[data-event-id]')];
  const eventLinks = [...document.querySelectorAll('a[data-event]')];
  const previousEvent = document.querySelector('#event-prev');
  const nextEvent = document.querySelector('#event-next');
  const eventPosition = document.querySelector('#event-position');
  let selectedEvent = 0;
  function selectEvent(index, shouldUpdateUrl = false) {
    selectedEvent = Math.max(0, Math.min(index, eventDetails.length - 1));
    const selected = eventDetails[selectedEvent];
    for (const detail of eventDetails) {
      detail.hidden = detail !== selected;
      detail.open = detail === selected;
    }
    for (const link of eventLinks) {
      if (link.dataset.event === selected.dataset.eventId) link.setAttribute('aria-current', 'true');
      else link.removeAttribute('aria-current');
    }
    previousEvent.disabled = selectedEvent === 0;
    nextEvent.disabled = selectedEvent === eventDetails.length - 1;
    eventPosition.textContent = `${selectedEvent + 1} / ${eventDetails.length}`;
    if (shouldUpdateUrl) {
      const url = new URL(location.href);
      url.searchParams.set('event', selected.dataset.eventId);
      history.replaceState(null, '', url);
    }
  }
  const requestedEvent = params.get('event') ?? location.hash.replace('#event-', '');
  const initialEvent = eventDetails.findIndex(detail => detail.dataset.eventId === requestedEvent);
  selectEvent(initialEvent < 0 ? 0 : initialEvent);
  document.querySelector('.event-controls').hidden = false;
  for (const link of eventLinks) {
    link.addEventListener('click', event => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      selectEvent(eventDetails.findIndex(detail => detail.dataset.eventId === link.dataset.event), true);
    }, options);
  }
  previousEvent.addEventListener('click', () => selectEvent(selectedEvent - 1, true), options);
  nextEvent.addEventListener('click', () => selectEvent(selectedEvent + 1, true), options);
  const matrix = document.querySelector('.reception-matrix');
  matrix.addEventListener('keydown', event => {
    const summary = event.target.closest('summary');
    if (!summary || !['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'].includes(event.key)) return;
    const cell = summary.closest('td');
    const row = cell.parentElement;
    const matrixRows = [...matrix.tBodies[0].rows];
    const rowStep = event.key === 'ArrowDown' ? 1 : event.key === 'ArrowUp' ? -1 : 0;
    const columnStep = event.key === 'ArrowRight' ? 1 : event.key === 'ArrowLeft' ? -1 : 0;
    let rowIndex = matrixRows.indexOf(row) + rowStep;
    let columnIndex = cell.cellIndex + columnStep;
    while (rowIndex >= 0 && rowIndex < matrixRows.length && columnIndex > 0 && columnIndex < 4) {
      const target = matrixRows[rowIndex].cells[columnIndex].querySelector('summary');
      if (target) { event.preventDefault(); target.focus(); return; }
      rowIndex += rowStep;
      columnIndex += columnStep;
    }
  }, options);
  window.addEventListener('pagehide', () => controller.abort(), { once: true });
})();
