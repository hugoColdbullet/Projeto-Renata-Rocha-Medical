# Projeto Renata Rocha Medical

Cópia de segurança pública do website **Renata Rocha — Médica Especialista em Anestesiologia**, criada a pedido do titular da conta GitHub. A pasta principal chama-se **`Projeto Renata Rocha Medical`**.

## Gerir o website

Abrir o **[Painel de gestão](PAINEL-GESTAO.md)** para editar textos, fotografias, contactos e estilos com a conta GitHub existente. Inclui atalhos para o editor, histórico, publicação manual e recuperação. Não cria uma nova conta nem uma aplicação CMS.

## Conteúdo

| Local | Conteúdo |
| --- | --- |
| `Projeto Renata Rocha Medical/public/` | Página HTML e todos os recursos locais: CSS, JavaScript, fotografia clínica conceptual, favicon e fontes |
| `Projeto Renata Rocha Medical/tests/` | Verificações de estrutura e sete grupos de testes de interação |
| `Projeto Renata Rocha Medical/README.md` | Edição de conteúdo, configuração do formulário e expansão futura |
| `Projeto Renata Rocha Medical/plan.md` | Plano de implementação e decisões de design |
| `Projeto Renata Rocha Medical/TODO.md` | Estado dos resultados e verificações |
| `Projeto Renata Rocha Medical/app.config.ts` | Metadados da identidade visual do projeto |
| `historico/origem-manus.bundle` | Histórico Git completo do projeto de origem até ao snapshot arquivado |
| `RESTAURO.md` | Instruções de restauro local, alojamento e recuperação do histórico |
| `BACKUP-MANIFEST.json` | Inventário, tamanho e SHA-256 dos ficheiros de backup |
| `ALOJAMENTO-DOMINIO.md` | Verificação do domínio e instruções para GitHub Pages, ainda sem ativação |
| `.github/workflows/pages.yml` | Workflow manual preparado para publicar apenas a pasta `public/` |
| `PAINEL-GESTAO.md` | Atalhos de edição, contactos, imagens, versões e publicação pelo GitHub existente |

## Abrir o website

```bash
git clone https://github.com/hugoColdbullet/Projeto-Renata-Rocha-Medical.git
cd Projeto-Renata-Rocha-Medical
python3 -m http.server 3000 --directory "Projeto Renata Rocha Medical/public"
```

Abra `http://localhost:3000`. Não são necessárias dependências npm, compilação, base de dados ou credenciais da Manus. A imagem e as fontes estão incluídas localmente.

## Estado e limites

Esta é uma cópia separada para backup; não muda o repositório canónico do projeto Manus e não ativa GitHub Pages ou publicação do website. Por ser um repositório **público**, qualquer pessoa pode consultar e descarregar estes ficheiros. Não foram incluídos `.env`, credenciais, dados clínicos, bases de dados ou ficheiros internos de autenticação.

O nome e a especialidade foram fornecidos para o projeto. Biografia, formação, cédula profissional, contactos e locais de atividade permanecem por confirmar. O formulário não envia mensagens automaticamente nem tem armazenamento. A imagem é conceptual, não representa uma clínica real ou a médica. A página mantém `noindex, nofollow` enquanto aguarda validação dos dados profissionais.

O snapshot de origem corresponde ao commit `9bcb0ecde30e99f2a763e40163556b43a879b0b8`. A versão transferível altera apenas o necessário para tornar a imagem local, documentar o backup e permitir a verificação num servidor de testes alternativo. O bundle conserva o histórico e o código original.

## Atualização futura

Depois de editar o website, execute os testes e atualize o inventário do backup antes de criar um novo commit. Nunca coloque palavras-passe, chaves de API ou dados de pacientes neste repositório público. Para instruções completas, consulte [RESTAURO.md](RESTAURO.md).

## Atualizar o inventário

Depois de guardar alterações legítimas e antes de fazer commit, execute na raiz:

```bash
python3 tools/update-backup.py
```

Este comando atualiza o SHA-256 de cada ficheiro e rejeita ficheiros de credenciais comuns. Não substitui a revisão de segurança: a pasta `.gitignore` evita ficheiros transitórios, mas é sempre necessário rever os ficheiros a publicar.

## Preparação de alojamento e domínio

Consultar [ALOJAMENTO-DOMINIO.md](ALOJAMENTO-DOMINIO.md) para os requisitos de associação de `www.renatarochamedical.com`. Foi preparado um workflow manual que publica somente `Projeto Renata Rocha Medical/public/`, sem mover os ficheiros ou expor o histórico como website. A publicação da versão atual foi aprovada pelo utilizador, mas a ativação pela integração foi bloqueada com HTTP 403. É necessário o titular selecionar **GitHub Actions** em [Settings → Pages](https://github.com/hugoColdbullet/Projeto-Renata-Rocha-Medical/settings/pages). Não houve publicação nem alterações DNS. O painel do fornecedor do domínio ainda tem de ser identificado para a associação final.

## Páginas de erro personalizadas

A pasta pública contém `400.html` e `404.html`, ambas com a identidade médica da Dra. Renata Rocha e navegação para a página inicial. Consultar [ERROS.md](Projeto%20Renata%20Rocha%20Medical/ERROS.md) para os testes e diferenças de alojamento.

Para testar respostas HTTP de erro localmente:

```bash
python3 "Projeto Renata Rocha Medical/dev-server.py" --port 3000 --bind 127.0.0.1
python3 "Projeto Renata Rocha Medical/tests/error-pages.py"
```

A página 404 será utilizada automaticamente por GitHub Pages depois de uma publicação bem-sucedida. A página 400 é acessível por URL; a personalização automática de HTTP 400 só foi implementada no servidor de pré-visualização incluído. Guardar os ficheiros no repositório não executa o workflow manual e não configura DNS. A publicação definitiva do projeto Manus solicitada em 9 de outubro foi cancelada após recusa do cartão de confirmação.
