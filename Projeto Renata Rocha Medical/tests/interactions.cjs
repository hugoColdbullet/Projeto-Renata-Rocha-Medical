const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const path = require('node:path');
const source = fs.readFileSync(path.join(__dirname, '../public/assets/main.js'), 'utf8');

class Element {
  constructor() {
    this.listeners = {};
    this.attributes = {};
    this.children = [];
    this.textContent = '';
    this.hidden = true;
    this.open = false;
    this.dataset = {};
    const classes = new Set();
    this.classList = {
      add: value => classes.add(value),
      remove: value => classes.delete(value),
      contains: value => classes.has(value),
      toggle: (value, enabled = !classes.has(value)) => enabled ? classes.add(value) : classes.delete(value)
    };
  }
  addEventListener(type, handler) { (this.listeners[type] ||= []).push(handler); }
  emit(type, values = {}) { (this.listeners[type] || []).forEach(fn => fn({ preventDefault() {}, target: this, ...values })); }
  setAttribute(key, value) { this.attributes[key] = value; }
  getAttribute(key) { return this.attributes[key]; }
  removeAttribute(key) { delete this.attributes[key]; }
  contains(element) { return element === this || this.children.includes(element); }
  append(element) { this.children.push(element); }
  replaceChildren(...elements) { this.children = elements; }
  querySelectorAll() { return this.children; }
  focus() { this.focused = true; }
  showModal() { this.open = true; }
  close() { this.open = false; }
  getBoundingClientRect() { return { left: 10, top: 10, right: 100, bottom: 100 }; }
}

function fixture(config = {}) {
  const ids = {};
  ['main-nav','contact-form','form-status','year','contact-email','contact-phone','contact-location','privacy-contact-status','privacy-dialog','info-dialog'].forEach(id => ids[id] = new Element());
  const toggle = new Element();
  toggle.setAttribute('aria-expanded', 'false');
  const link = new Element();
  link.hash = '#sobre';
  ids['main-nav'].children = [link];
  ids['contact-form'].valid = true;
  ids['contact-form'].reportValidity = () => ids['contact-form'].valid;
  const note = new Element();
  const warning = new Element();
  const trigger = new Element();
  trigger.dataset.openDialog = 'privacy-dialog';
  const close = new Element();
  ids['privacy-dialog'].children = [close];
  ids['info-dialog'].children = [new Element()];
  const document = new Element();
  document.getElementById = id => ids[id];
  document.querySelector = selector => ({ '.menu-toggle': toggle, '.form-note': note, '.contact-warning': warning })[selector];
  document.querySelectorAll = selector => ({ '[data-open-dialog]': [trigger], '.info-dialog': [ids['privacy-dialog'], ids['info-dialog']], 'main section[id]': [] })[selector] || [];
  document.createElement = () => new Element();
  document.createTextNode = text => ({ textContent: text });
  const window = { SITE_CONFIG: config, matchMedia: () => ({ addEventListener() {} }) };
  class FormDataMock {
    get(key) { return { name: 'Teste Validação', email: 'teste@example.org', subject: 'Informações profissionais', message: 'Mensagem de teste não clínica.' }[key]; }
  }
  vm.runInNewContext(source, { document, window, FormData: FormDataMock, console });
  return { ids, toggle, link, note, warning, document, trigger, close };
}

let tested = 0;
const demo = fixture();
demo.toggle.emit('click');
assert.equal(demo.toggle.getAttribute('aria-expanded'), 'true');
assert(demo.ids['main-nav'].classList.contains('is-open'));
demo.link.emit('click');
assert.equal(demo.toggle.getAttribute('aria-expanded'), 'false');
tested++;
demo.toggle.emit('click');
demo.document.emit('keydown', { key: 'Escape' });
assert.equal(demo.toggle.getAttribute('aria-expanded'), 'false');
assert(demo.toggle.focused);
tested++;
demo.ids['contact-form'].valid = false;
demo.ids['contact-form'].emit('submit');
assert(demo.ids['form-status'].hidden);
tested++;
demo.ids['contact-form'].valid = true;
demo.ids['contact-form'].emit('submit');
assert.match(demo.ids['form-status'].textContent, /Não foi enviada nem guardada/);
assert.equal(demo.ids['form-status'].children.length, 0);
tested++;
demo.trigger.emit('click');
assert(demo.ids['privacy-dialog'].open);
demo.close.emit('click');
assert(!demo.ids['privacy-dialog'].open);
tested++;
const configured = fixture({ email: 'contacto@example.org', contactEnabled: true, phone: '+351 210 000 000', location: 'Local confirmado' });
configured.ids['contact-form'].emit('submit');
const draft = configured.ids['form-status'].children[1];
assert.match(draft.href, /^mailto:contacto@example.org\?subject=/);
assert.match(decodeURIComponent(draft.href), /Email de resposta: teste@example.org/);
assert.match(configured.ids['form-status'].children[0].textContent, /Ainda não foi enviado/);
assert.match(configured.ids['privacy-contact-status'].textContent, /Nenhuma mensagem é enviada automaticamente/);
assert.equal(configured.ids['contact-phone'].children[0].href, 'tel:+351210000000');
tested++;
const invalidConfig = fixture({ email: 'não-é-email', contactEnabled: true });
invalidConfig.ids['contact-form'].emit('submit');
assert.match(invalidConfig.ids['form-status'].textContent, /por configurar/);
assert.equal(invalidConfig.ids['contact-email'].children.length, 0);
tested++;
console.log(`${tested} grupos de testes aprovados: menu, Escape, validação, contacto não configurado, diálogos, rascunho mailto e configuração inválida.`);
