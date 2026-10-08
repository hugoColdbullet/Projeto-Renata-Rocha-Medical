# Painel de gestão — Renata Rocha Medical

Usar a conta GitHub existente **hugoColdbullet** para gerir o website. Este painel organiza atalhos para o editor e as ferramentas nativas do GitHub: não é uma aplicação CMS separada, não cria contas nem exige nova autenticação fora do GitHub. Consultar o documento não permite a outras pessoas editar o projeto; a escrita continua dependente das permissões da conta GitHub.

## Atalhos de gestão

| O que pretende fazer | Abrir |
| --- | --- |
| Editar textos, apresentação, Sobre e perguntas frequentes | [Editar a página HTML](https://github.com/hugoColdbullet/Projeto-Renata-Rocha-Medical/edit/main/Projeto%20Renata%20Rocha%20Medical/public/index.html) |
| Configurar email, telefone e local de atividade | [Editar os contactos](https://github.com/hugoColdbullet/Projeto-Renata-Rocha-Medical/edit/main/Projeto%20Renata%20Rocha%20Medical/public/assets/site-config.js) |
| Alterar cores, fontes, espaçamento e versão móvel | [Editar os estilos CSS](https://github.com/hugoColdbullet/Projeto-Renata-Rocha-Medical/edit/main/Projeto%20Renata%20Rocha%20Medical/public/assets/styles.css) |
| Consultar ou adicionar fotografias e outros recursos | [Abrir a pasta de recursos](https://github.com/hugoColdbullet/Projeto-Renata-Rocha-Medical/tree/main/Projeto%20Renata%20Rocha%20Medical/public/assets) |
| Editar vários ficheiros no mesmo ambiente web | [Abrir o editor github.dev](https://github.dev/hugoColdbullet/Projeto-Renata-Rocha-Medical) |
| Consultar a pasta completa do website | [Abrir o projeto](https://github.com/hugoColdbullet/Projeto-Renata-Rocha-Medical/tree/main/Projeto%20Renata%20Rocha%20Medical) |
| Rever alterações antes de integrar | [Pull requests](https://github.com/hugoColdbullet/Projeto-Renata-Rocha-Medical/pulls) |
| Consultar versões e commits anteriores | [Histórico de versões](https://github.com/hugoColdbullet/Projeto-Renata-Rocha-Medical/commits/main/) |
| Executar a publicação, depois de ativar Pages | [Workflow de publicação](https://github.com/hugoColdbullet/Projeto-Renata-Rocha-Medical/actions/workflows/pages.yml) |
| Ativar e configurar o alojamento | [Settings → Pages](https://github.com/hugoColdbullet/Projeto-Renata-Rocha-Medical/settings/pages) |
| Obter o código atual num ficheiro ZIP | [Descarregar a branch main](https://github.com/hugoColdbullet/Projeto-Renata-Rocha-Medical/archive/refs/heads/main.zip) |

## Editar sem perder a estrutura

Abrir o atalho de edição, localizar o texto e alterar apenas o conteúdo pretendido. Manter etiquetas HTML, IDs e referências a imagens. Em conteúdo HTML, escrever `&amp;` para um `&` literal e `&lt;` para um `<` literal. O editor do GitHub edita código: o seu Preview não equivale à visualização completa do website num browser.

Clicar em **Commit changes…** e escrever uma descrição curta da alteração. Para mudanças importantes, criar uma branch e um pull request, rever e integrar em `main`. Se houver proteção de branch, respeitar o fluxo exigido; não a desativar para permitir a edição.

Guardar um commit **não publica automaticamente**: o workflow deste projeto continua manual. Antes de publicar, validar o conteúdo e executar os testes. Depois de ativar GitHub Pages, abrir o workflow, selecionar **Run workflow**, escolher `main` e confirmar. Verificar a execução e o endereço servido antes de declarar a nova versão publicada.

## Configurar contactos

Editar `site-config.js` apenas com dados profissionais reais:

```js
window.SITE_CONFIG = Object.freeze({
  email: 'EMAIL_REAL_CONFIRMADO',
  phone: 'TELEFONE_REAL_CONFIRMADO',
  location: 'LOCAL_REAL_CONFIRMADO',
  contactEnabled: true
});
```

Não copiar literalmente os valores de exemplo. Sem email válido e `contactEnabled: true`, não é preparado um rascunho de contacto. Com configuração válida, o formulário prepara um rascunho para o programa de email; a pessoa tem de o rever e enviar nesse programa. Não existe envio automático, receção num servidor ou arquivo de mensagens.

Atualizar também os campos pendentes no HTML e a informação de privacidade antes de divulgar contactos. A biografia, formação e cédula não podem ser inventadas. Não colocar palavras-passe, tokens ou dados de pacientes em ficheiros deste repositório público.

## Substituir ou adicionar imagens

Abrir a pasta de recursos e usar **Add file → Upload files**. Preferir nomes simples, sem espaços, por exemplo `fotografia-renata.webp`. Ajustar o `src` correspondente em `index.html` e a descrição `alt`. Usar uma fotografia real autorizada para representar a médica; a imagem clínica atual é conceptual e está identificada como ilustrativa.

Não apagar uma imagem ainda referenciada. Confirmar que o caminho começa por `assets/` quando se trata de recursos locais da página. As fontes e respetivas licenças devem ser mantidas.

## Adicionar páginas posteriormente

Criar o novo HTML dentro de `Projeto Renata Rocha Medical/public/`, reutilizar os estilos, adaptar a navegação e atualizar `manus-routes.json`. O JavaScript atual pressupõe a existência de elementos da página inicial: adaptar as guardas antes de o reutilizar numa página sem formulário ou menu. Não criar links para ficheiros inexistentes.

## Validar e manter o backup

No computador, depois de obter a versão atual:

```bash
node "Projeto Renata Rocha Medical/tests/interactions.cjs"
python3 -m http.server 3000 --directory "Projeto Renata Rocha Medical/public"
```

Com o servidor ativo, noutro terminal:

```bash
python3 "Projeto Renata Rocha Medical/tests/structure.py"
python3 tools/update-backup.py
```

Guardar o manifesto atualizado junto das alterações. Se editar apenas no browser, os hashes do manifesto não se atualizam por si; usar um computador com Python ou solicitar a atualização antes de apresentar essa versão como backup verificado. Não usar o editor web como terminal. Consultar [RESTAURO.md](RESTAURO.md) para recuperar o projeto e o histórico.

## Estado do alojamento e domínio

Em 8 de outubro de 2026, a publicação da versão atual foi autorizada pelo utilizador. A tentativa de ativar Pages pela integração devolveu **403 — Resource not accessible by integration**. A consulta posterior não encontrou um site Pages ativo.

**Passo manual necessário:** abrir Settings → Pages, escolher **GitHub Actions** em Build and deployment → Source e guardar, se solicitado. Este painel não altera nem contorna essa permissão. Ainda não existe um endereço Pages confirmado como publicado.

O domínio `www.renatarochamedical.com` não foi associado e os registos DNS não foram alterados. A gestão DNS continua no painel do fornecedor do domínio, que ainda tem de ser identificado pelo titular. Não é necessária transferência do domínio. Consultar [ALOJAMENTO-DOMINIO.md](ALOJAMENTO-DOMINIO.md) para os registos propostos e a verificação HTTPS.

## Documentação de apoio

- [GitHub — editar ficheiros](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)
- [Documentação do projeto](Projeto%20Renata%20Rocha%20Medical/README.md)
- [Instruções de restauro](RESTAURO.md)
- [Alojamento e domínio](ALOJAMENTO-DOMINIO.md)
