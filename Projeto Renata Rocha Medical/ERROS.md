# Páginas de erro — Dra. Renata Rocha

Foram acrescentadas duas páginas autónomas ao website: `public/404.html` (página não encontrada) e `public/400.html` (pedido inválido). Mantêm a identidade verde-petróleo, sálvia, marfim e monograma RR. Não dependem do formulário ou de ficheiros externos, pelo que a apresentação funciona também quando uma URL inexistente tem vários níveis.

As páginas permitem regressar ao início e consultar as secções Sobre, Anestesiologia, Dúvidas e Contactos. Os destinos são adaptados ao domínio próprio, à pré-visualização e ao caminho `/Projeto-Renata-Rocha-Medical/` em GitHub Pages. Sem JavaScript, os links usam a raiz do domínio.

## Pré-visualização e acesso direto

```bash
python3 dev-server.py --port 3000 --bind 127.0.0.1
```

Abrir `/404.html` e `/400.html` para consultar a apresentação de cada página. Um acesso direto a um ficheiro existente devolve HTTP 200: o número visível não altera o código de resposta.

O servidor de pré-visualização incluído responde a caminhos inexistentes com o conteúdo de `404.html` e HTTP 404. Pedidos HTTP malformados que chegam a este servidor podem receber o conteúdo de `400.html` com HTTP 400. Erros rejeitados por um proxy antes de chegarem ao servidor continuam sob controlo desse proxy.

## GitHub Pages

O workflow existente publica a pasta `public/` inteira, incluindo ambas as páginas. GitHub Pages reconhece `404.html` na raiz do conteúdo publicado e utiliza-a para URLs inexistentes, após uma publicação bem-sucedida. A página 400 fica disponível em `/400.html`, mas não existe neste projeto uma configuração GitHub Pages para substituir automaticamente respostas HTTP 400.

A ativação de Pages pela integração continuava bloqueada na última tentativa. Os novos ficheiros podem ser guardados no repositório sem implicar publicação. Depois de ativar Source: GitHub Actions, executar o workflow e testar tanto uma URL inexistente como os acessos diretos. Não há alterações DNS nesta extensão.

## Publicação estática Manus

As duas páginas podem ser publicadas e consultadas diretamente. O gateway de alojamento controla o fallback de caminhos inexistentes; não atribuir ao ficheiro `404.html` uma capacidade automática que só foi comprovada no servidor de pré-visualização ou documentada para GitHub Pages. Não foi acrescentado um backend de produção apenas para erros.

## Testes

```bash
python3 tests/error-pages.py
```

Os testes verificam HTML, ausência de assets externos, oito cenários de navegação, GET/HEAD 404, pedido inválido 400 e retorno à página inicial. Não acrescentar páginas de erro ao manifesto de rotas de conteúdo.

Fonte: [GitHub — criar uma página 404 personalizada](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-custom-404-page-for-your-github-pages-site).

## Estado confirmado em 9 de outubro de 2026

Ambas as páginas foram verificadas na pré-visualização pública, incluindo um caminho inexistente aninhado que recebeu HTTP 404 com o conteúdo personalizado. A versão foi gravada no projeto Manus (`50a289d95371b0d1d25c21de3be39a63ea600798`). A publicação definitiva foi recusada no cartão de confirmação e ficou cancelada; não foi iniciada novamente. O acesso atual é de pré-visualização, não publicação no domínio próprio.
