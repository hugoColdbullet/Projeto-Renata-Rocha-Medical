# Alojamento GitHub Pages — Renata Rocha Medical

## Resultado da verificação em 8 de outubro de 2026

**É possível alojar o website no GitHub Pages e associar `www.renatarochamedical.com` sem transferir o domínio.** O domínio permanece no seu registador; apenas os registos web DNS deverão ser atualizados no painel que gere a zona.

O repositório é público: https://github.com/hugoColdbullet/Projeto-Renata-Rocha-Medical. A conta ligada tem administração do repositório e GitHub Actions está ativo. GitHub Pages ainda não está ativo. Não foi efetuada qualquer alteração DNS ou publicação durante esta verificação.

| Elemento | Observação |
| --- | --- |
| Registador público (RDAP) | Global Domain Group LLC; o fornecedor contratado pode ser um revendedor |
| Servidores DNS atuais | `ns1.globaldomaingroup.com` e `ns2.globaldomaingroup.com` |
| `renatarochamedical.com` — A | `104.18.26.246` |
| `www.renatarochamedical.com` — A | `104.18.26.246` |
| `www` — CNAME | Não encontrado |
| MX | Não encontrados; o utilizador confirmou que não há emails associados |
| AAAA e CAA | Não encontrados na consulta |
| Website atual em HTTPS | Conteúdo obtido indicava erro 404; não aponta para este projeto |

Estes são dados públicos observados, não prova de acesso ao painel do domínio. Não é necessário código EPP, desbloqueio de transferência ou mudança de nameservers para o apontamento pretendido.

## Pasta que será publicada

Publicar **apenas** o conteúdo de:

```text
Projeto Renata Rocha Medical/public/
```

Esta pasta já inclui HTML, CSS, JavaScript, fontes e imagem locais. O workflow preparado em `.github/workflows/pages.yml` valida a página, empacota esta pasta e publica-a. O bundle histórico, README e documentos de backup permanecem no repositório mas não integram o website alojado.

GitHub Pages não permite escolher diretamente qualquer subpasta como origem por branch: as opções normais são a raiz ou `/docs`. Usar uma ação de publicação com caminho explícito permite manter a pasta atual sem a mover ou duplicar. O workflow preparado é **manual**; guardar o ficheiro não publica o website nem ativa Pages. Não há compras ou serviços adicionais nesta preparação.

## Ativação no GitHub após aprovação

1. Ativar Pages no repositório com origem **GitHub Actions** (`build_type: workflow`).
2. Executar manualmente o workflow preparado.
3. Confirmar o resultado da ação e a resposta do endereço inicialmente atribuído pelo GitHub. Antes do domínio próprio, o endereço de projeto esperado é `https://hugocoldbullet.github.io/Projeto-Renata-Rocha-Medical/`; só declarar ativo depois de verificar.
4. Verificar a titularidade do domínio nas definições da conta GitHub mediante o TXT fornecido pelo próprio GitHub. Não inventar o valor de verificação.
5. Configurar **Custom domain** no repositório: `www.renatarochamedical.com`.
6. Aplicar no painel DNS os registos aprovados da secção seguinte.
7. Verificar DNS, associação do domínio e certificado. Ativar **Enforce HTTPS** quando o certificado estiver disponível e testar ambas as variantes do endereço.

A ordem de verificação/associação/DNS deverá evitar deixar apontamentos para GitHub sem uma associação correspondente. O ficheiro `CNAME` não configura a associação quando se publica por workflow de Actions: usar as definições de Pages.

## Registos DNS propostos

Manter os nameservers atuais. Para que ambos os endereços funcionem e o domínio sem `www` redirecione para `www`, aplicar os valores oficiais:

| Tipo | Nome/Host | Valor |
| --- | --- | --- |
| CNAME | `www` | `hugocoldbullet.github.io` |
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |

Substituir o A atual de `www` por CNAME: não podem coexistir para o mesmo nome. Substituir o A web atual de `@` pelos quatro valores listados. Não apagar registos não relacionados e exportar a zona antes de editar. O CNAME **não** inclui `https://`, nome do repositório ou caminho da pasta. Usar o TTL permitido pelo painel; a propagação depende de caches externos.

Os registos IPv6 são opcionais; se forem adicionados, usar os quatro valores oficiais: `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`. Não adicionar wildcards. Acrescentar o TXT de verificação GitHub quando o valor real estiver disponível.

Não será necessário transferir o domínio nem alterar email. Futuras alterações de DNS exigem confirmar o painel correto e os registos exatos antes de aplicar. A emissão do certificado e a opção HTTPS podem não estar imediatamente disponíveis; só declarar ligação concluída depois dos testes.

## Conteúdo que irá para o público

A página mostra Renata Rocha — Médica Especialista em Anestesiologia, informação educativa sobre a especialidade, perguntas frequentes e contactos. Contém campos de biografia, formação, cédula e contactos ainda pendentes. A imagem é conceptual. O formulário não envia nem guarda mensagens enquanto não estiver configurado. A página mantém `noindex, nofollow` enquanto esses dados estão por validar.

Publicar no Pages tornará esta versão acessível como website, ainda que já exista como código no repositório público. Não preencher dados profissionais fictícios para a publicação. A remoção de `noindex`, novas informações médicas e configuração de contactos são alterações separadas.

## Reversão

Se for necessário regressar ao endereço anterior, repor os registos da exportação DNS e retirar a associação do domínio no Pages conforme apropriado. Não apagar o repositório, o histórico ou os backups. O apontamento anterior observado era `104.18.26.246`, mas usar sempre a exportação real do painel como referência de reversão.

## Fontes oficiais consultadas

- [GitHub — gerir um domínio próprio](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- [GitHub — workflows personalizados de Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [Verisign RDAP — registo do domínio](https://rdap.verisign.com/com/v1/domain/renatarochamedical.com)
