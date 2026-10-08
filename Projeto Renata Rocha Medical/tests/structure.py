from html.parser import HTMLParser
from pathlib import Path
from collections import Counter
import json
import os
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'public'
BASE = os.environ.get('TEST_BASE_URL', 'http://localhost:3000').rstrip('/')

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.anchors, self.assets, self.tags, self.fields = [], [], [], [], []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a' and attrs.get('href', '').startswith('#'):
            self.anchors.append(attrs['href'][1:])
        if tag in ('script', 'img') and attrs.get('src'):
            self.assets.append(attrs['src'])
        if tag == 'link' and attrs.get('href'):
            self.assets.append(attrs['href'])
        if tag in ('input', 'select', 'textarea'):
            self.fields.append(attrs)

html = (PUBLIC / 'index.html').read_text()
page = PageParser()
page.feed(html)
assert 'lang="pt-PT"' in html
assert page.tags.count('h1') == 1
assert all(page.tags.count(tag) >= 1 for tag in ('header', 'nav', 'main', 'section', 'footer'))
assert not [id for id, count in Counter(page.ids).items() if count > 1], 'IDs duplicados'
assert not set(page.anchors) - set(page.ids), 'Âncoras sem destino'
for asset in page.assets:
    if asset.startswith('assets/'):
        assert (PUBLIC / asset).is_file(), f'Recurso em falta: {asset}'
for field in page.fields:
    assert 'required' in field, f'Campo sem validação: {field}'
    assert f'for="{field["id"]}"' in html or field['id'] == 'consent', 'Campo sem rótulo'
assert 'assets/clinical-hero.webp' in html
assert '/manus-storage/' not in html
assert (PUBLIC / 'assets/clinical-hero.webp').read_bytes()[:4] == b'RIFF'
manifest = json.loads((PUBLIC / 'manus-routes.json').read_text())
assert [route['path'] for route in manifest['routes']] == ['/']
css = (PUBLIC / 'assets/styles.css').read_text()
assert css.count('{') == css.count('}')
assert 'prefers-reduced-motion' in css
assert all(f'max-width:{width}px' in css for width in (1100, 860, 620))
for font in re.findall(r"url\('([^']+)'\)", css):
    data = (PUBLIC / 'assets' / font).read_bytes()
    assert data[:4] == b'wOF2', f'Formato de fonte incorreto: {font}'
js = (PUBLIC / 'assets/main.js').read_text()
assert not any(operation in js for operation in ('localStorage', 'sessionStorage', 'fetch(', 'XMLHttpRequest'))
for route in ('/', '/manus-routes.json', '/assets/styles.css', '/assets/main.js', '/assets/clinical-hero.webp'):
    with urllib.request.urlopen(BASE + route) as response:
        assert response.status == 200
        assert response.read(), f'Resposta vazia: {route}'
print('Estrutura HTML, âncoras, campos, recursos locais, fontes WOFF2, breakpoints, movimento reduzido, manifesto e HTTP: aprovados.')
