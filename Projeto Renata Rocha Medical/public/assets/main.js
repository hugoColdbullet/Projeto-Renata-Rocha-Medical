'use strict';

(() => {
  const config = window.SITE_CONFIG || {};
  const navigation = document.getElementById('main-nav');
  const toggle = document.querySelector('.menu-toggle');
  const form = document.getElementById('contact-form');
  const status = document.getElementById('form-status');
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const emailReady = config.contactEnabled === true && emailPattern.test(config.email || '');

  function closeMenu() {
    navigation.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Abrir menu');
  }

  toggle.addEventListener('click', () => {
    const isOpen = toggle.getAttribute('aria-expanded') === 'true';
    navigation.classList.toggle('is-open', !isOpen);
    toggle.setAttribute('aria-expanded', String(!isOpen));
    toggle.setAttribute('aria-label', isOpen ? 'Abrir menu' : 'Fechar menu');
  });

  navigation.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', closeMenu);
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      closeMenu();
      toggle.focus();
    }
  });
  document.addEventListener('click', (event) => {
    if (!navigation.contains(event.target) && !toggle.contains(event.target)) closeMenu();
  });
  window.matchMedia('(min-width: 861px)').addEventListener('change', closeMenu);

  if ('IntersectionObserver' in window) {
    const navLinks = [...navigation.querySelectorAll('a[href^="#"]')];
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        navLinks.forEach((link) => {
          const active = link.hash === `#${entry.target.id}`;
          link.classList.toggle('active', active);
          if (active) link.setAttribute('aria-current', 'location');
          else link.removeAttribute('aria-current');
        });
      });
    }, { rootMargin: '-15% 0px -60% 0px', threshold: 0 });
    document.querySelectorAll('main section[id]').forEach((section) => observer.observe(section));
  }

  document.getElementById('year').textContent = String(new Date().getFullYear());

  function addContact(id, text, href) {
    const element = document.getElementById(id);
    if (!text) return;
    element.textContent = '';
    if (href) {
      const link = document.createElement('a');
      link.href = href;
      link.textContent = text;
      element.append(link);
    } else {
      element.textContent = text;
    }
  }
  if (emailPattern.test(config.email || '')) addContact('contact-email', config.email, `mailto:${config.email}`);
  if (config.phone) addContact('contact-phone', config.phone, `tel:${String(config.phone).replace(/[^+\d]/g, '')}`);
  if (config.location) addContact('contact-location', config.location);
  if (emailReady) {
    document.querySelector('.form-note').textContent = 'Campos com * são obrigatórios. Será aberto um rascunho no seu programa de email; confirme o envio nesse programa.';
    document.querySelector('.contact-warning').textContent = 'Para assuntos não urgentes. Este website não é um canal de urgência.';
    document.getElementById('privacy-contact-status').textContent = 'O formulário prepara um rascunho que pode abrir no seu programa de email. Nenhuma mensagem é enviada automaticamente; reveja o rascunho e confirme o envio nesse programa.';
  }

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    status.hidden = false;
    if (!emailReady) {
      status.textContent = 'O contacto profissional ainda está por configurar. Não foi enviada nem guardada qualquer mensagem. Volte a consultar esta página quando os contactos estiverem disponíveis.';
      return;
    }
    const data = new FormData(form);
    const subject = `Contacto — ${data.get('subject')}`;
    const body = `Nome: ${String(data.get('name')).trim()}\nEmail de resposta: ${String(data.get('email')).trim()}\n\n${String(data.get('message')).trim()}`;
    const emailUrl = `mailto:${config.email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    const draftLink = document.createElement('a');
    draftLink.href = emailUrl;
    draftLink.textContent = 'Abrir rascunho no programa de email';
    draftLink.className = 'text-link';
    status.replaceChildren(document.createTextNode('O rascunho está preparado. Ainda não foi enviado. Abra o seu programa de email para rever e enviar a mensagem. '), draftLink);
  });

  // <dialog> fornece gestão de foco e fecho com Escape nativos.
  document.querySelectorAll('[data-open-dialog]').forEach((trigger) => {
    trigger.addEventListener('click', () => {
      const dialog = document.getElementById(trigger.dataset.openDialog);
      if (dialog && !dialog.open) dialog.showModal();
    });
  });
  document.querySelectorAll('.info-dialog').forEach((dialog) => {
    dialog.querySelectorAll('.dialog-close, .dialog-dismiss').forEach((button) => {
      button.addEventListener('click', () => dialog.close());
    });
    dialog.addEventListener('click', (event) => {
      if (event.target !== dialog) return;
      const rect = dialog.getBoundingClientRect();
      if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
    });
  });
})();
