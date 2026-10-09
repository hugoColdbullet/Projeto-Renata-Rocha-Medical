#!/usr/bin/env python3
from functools import partial
from html.parser import HTMLParser
import importlib.util
from pathlib import Path
import re
import socket
import subprocess
import threading
from http.server import ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'public'


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.h1, self.sections, self.assets = [], 0, [], []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h1': self.h1 += 1
        if 'id' in attrs: self.ids.append(attrs['id'])
        if 'data-home-section' in attrs: self.sections.append(attrs['data-home-section'])
        if tag == 'script' and 'src' in attrs: self.assets.append(attrs['src'])
        if tag == 'link' and attrs.get('rel') == 'stylesheet': self.assets.append(attrs.get('href'))


home = (PUBLIC / 'index.html').read_text()
for code in (400, 404):
    html = (PUBLIC / f'{code}.html').read_text()
    page = Page()
    page.feed(html)
    assert 'lang="pt-PT"' in html and 'noindex, nofollow' in html
    assert page.h1 == 1 and len(page.ids) == len(set(page.ids))
    assert not page.assets, 'Páginas de erro devem ser autónomas em caminhos aninhados'
    assert all(not section or f'id="{section}"' in home for section in page.sections)
    assert 'prefers-reduced-motion' in html
    assert f'>{code}</span>' in html
    scripts = re.findall(r'<script>(.*?)</script>', html, flags=re.S)
    assert len(scripts) == 1
    check = """
const vm = require('node:vm');
const source = process.argv[1];
for (const test of [
  {hostname:'www.renatarochamedical.com',pathname:'/pasta/inexistente',protocol:'https:',base:'/'},
  {hostname:'hugocoldbullet.github.io',pathname:'/Projeto-Renata-Rocha-Medical/a/b',protocol:'https:',base:'/Projeto-Renata-Rocha-Medical/'},
  {hostname:'preview.example',pathname:'/404.html',protocol:'https:',base:'/'},
  {hostname:'',pathname:'/tmp/404.html',protocol:'file:',base:'./'}
]) {
  const links = ['', 'sobre', 'perguntas', 'contactos', 'especialidade'].map(section => ({section, getAttribute(){return this.section;},setAttribute(name,value){this.href=value;}}));
  const year = {};
  let ready;
  const document = {addEventListener(event,handler){ready=handler;},querySelectorAll(){return links;},getElementById(){return year;}};
  vm.runInNewContext(source,{document,location:test,Date});
  ready();
  for (const link of links) {
    const wanted = test.base+'index.html'+(link.section?'#'+link.section:'');
    if(link.href !== wanted) throw new Error('Destino de navegação errado');
  }
  if(year.textContent !== String(new Date().getFullYear())) throw new Error('Ano incorreto');
}
"""
    subprocess.run(['node', '-e', check, scripts[0]], check=True)

spec = importlib.util.spec_from_file_location('dev_server', ROOT / 'dev-server.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
handler = partial(module.WebsiteHandler, directory=str(PUBLIC))
server = ThreadingHTTPServer(('127.0.0.1', 0), handler)
thread = threading.Thread(target=server.serve_forever, daemon=True)
thread.start()
base = f'http://127.0.0.1:{server.server_port}'
try:
    for path in ('/400.html', '/404.html'):
        with urlopen(base + path) as response:
            assert response.status == 200
            assert b'Renata Rocha' in response.read()
    try:
        urlopen(base + '/pasta/nao-existe')
        raise AssertionError('URL inexistente deve devolver 404')
    except HTTPError as response:
        assert response.code == 404
        assert response.read() == (PUBLIC / '404.html').read_bytes()
    try:
        urlopen(Request(base + '/pasta/nao-existe', method='HEAD'))
        raise AssertionError('HEAD deve devolver 404')
    except HTTPError as response:
        assert response.code == 404 and response.read() == b''
    with socket.create_connection(('127.0.0.1', server.server_port), timeout=5) as client:
        client.sendall(b'GET / HTTP/invalid\r\nHost: localhost\r\n\r\n')
        content = b''
        while True:
            chunk = client.recv(65536)
            if not chunk: break
            content += chunk
        assert content.startswith(b'HTTP/1.0 400')
        assert (PUBLIC / '400.html').read_bytes() in content
finally:
    server.shutdown()
    server.server_close()
    thread.join(timeout=5)
print('Erros 400/404: HTML autónomo, 8 cenários de navegação, GET/HEAD 404 e pedido inválido 400 aprovados.')
