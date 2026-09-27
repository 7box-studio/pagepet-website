const form = document.querySelector('#convert-form');
if (form) {
const input = document.querySelector('#book-file');
const label = document.querySelector('#file-label');
const status = document.querySelector('#status');
const dropZone = document.querySelector('#drop-zone');
const output = document.querySelector('#output-format');
const button = form.querySelector('button[type="submit"]');
const inputFormats = new Set(['epub', 'fb2', 'mobi', 'azw3', 'docx', 'txt', 'rtf', 'odt']);

function showFile(file) {
  label.textContent = file ? file.name : form.dataset.select;
  const sourceFormat = file?.name.split('.').pop()?.toLowerCase();
  if (sourceFormat && sourceFormat === output.value) {
    output.value = sourceFormat === 'epub' ? 'fb2' : 'epub';
  }
  status.textContent = '';
  status.dataset.state = '';
}

input.addEventListener('change', () => showFile(input.files[0]));
for (const eventName of ['dragenter', 'dragover']) {
  dropZone.addEventListener(eventName, event => {
    event.preventDefault();
    dropZone.classList.add('dragging');
  });
}
for (const eventName of ['dragleave', 'drop']) {
  dropZone.addEventListener(eventName, event => {
    event.preventDefault();
    dropZone.classList.remove('dragging');
  });
}
dropZone.addEventListener('drop', event => {
  if (!event.dataTransfer.files.length) return;
  input.files = event.dataTransfer.files;
  showFile(input.files[0]);
});

form.addEventListener('submit', async event => {
  event.preventDefault();
  const file = input.files[0];
  if (!file) {
    status.textContent = form.dataset.missing;
    status.dataset.state = 'error';
    return;
  }
  const sourceFormat = file.name.split('.').pop().toLowerCase();
  if (!inputFormats.has(sourceFormat) || file.size === 0 || file.size > 20 * 1024 * 1024) {
    status.textContent = form.dataset.invalid;
    status.dataset.state = 'error';
    return;
  }
  if (sourceFormat === output.value) {
    status.textContent = form.dataset.same;
    status.dataset.state = 'error';
    return;
  }
  button.disabled = true;
  button.textContent = form.dataset.working;
  status.textContent = form.dataset.working;
  status.dataset.state = 'working';
  try {
    const data = new FormData();
    data.append('file', file);
    data.append('format', output.value);
    const response = await fetch('/api/convert?lang=' + encodeURIComponent(form.dataset.language), { method: 'POST', body: data });
    if (!response.ok) {
      const body = await response.json();
      throw new Error(body.detail || form.dataset.failed);
    }
    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = file.name.replace(/\.[^.]+$/, '') + '.' + output.value;
    document.body.append(link);
    link.click();
    link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 60000);
    status.textContent = form.dataset.success;
    status.dataset.state = 'success';
  } catch (error) {
    status.textContent = error instanceof Error ? error.message : form.dataset.failed;
    status.dataset.state = 'error';
  } finally {
    button.disabled = false;
    button.replaceChildren(document.createTextNode(form.dataset.button), Object.assign(document.createElement('span'), { textContent: '↗' }));
  }
});
}
