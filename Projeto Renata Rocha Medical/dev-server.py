#!/usr/bin/env python3
"""Servidor estático de pré-visualização com páginas de erro 400/404 locais."""
import argparse
from functools import partial
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class WebsiteHandler(SimpleHTTPRequestHandler):
    def send_error(self, code, message=None, explain=None):
        if code not in (400, 404):
            return super().send_error(code, message, explain)
        page = Path(self.directory) / f'{code}.html'
        if not page.is_file():
            return super().send_error(code, message, explain)
        content = page.read_bytes()
        if code == 400 and self.request_version == 'HTTP/0.9':
            self.request_version = 'HTTP/1.0'
        self.send_response(code, HTTPStatus(code).phrase)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(content)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.end_headers()
        if self.command != 'HEAD':
            self.wfile.write(content)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=3000)
    parser.add_argument('--bind', default='0.0.0.0')
    parser.add_argument('--directory', type=Path, default=Path(__file__).resolve().parent / 'public')
    args = parser.parse_args()
    handler = partial(WebsiteHandler, directory=str(args.directory.resolve()))
    with ThreadingHTTPServer((args.bind, args.port), handler) as server:
        print(f'Servidor estático ativo em {args.bind}:{args.port}; erros 400/404 personalizados.', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    main()
