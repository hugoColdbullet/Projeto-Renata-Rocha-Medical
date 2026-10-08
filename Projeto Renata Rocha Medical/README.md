# Renata Rocha — Médica Especialista em Anestesiologia

Website de página única, em português europeu, feito com HTML, CSS e JavaScript sem framework. A identidade visual combina verde-petróleo, sálvia e marfim, com tipografia editorial e elementos discretos associados à monitorização clínica.

## Abrir e editar

Os ficheiros do website estão em `public/`. Para uma visualização local, execute na pasta do projeto:

```bash
python3 -m http.server 3000 --directory public
```

Abra `http://localhost:3000`. Também pode abrir `public/index.html` diretamente para editar e consultar a versão transferível. O servidor é recomendado para todas as funcionalidades e recursos.

| Ficheiro | Utilização |
| --- | --- |
| `public/index.html` | Textos, secções, navegação, formulário e diálogos |
| `public/assets/styles.css` | Cores, tipografia e adaptação a telemóvel/tablet |
| `public/assets/main.js` | Menu, navegação, diálogos e preparação de contacto |
| `public/assets/site-config.js` | Configuração dos contactos profissionais |
| `public/assets/favicon.svg` | Monograma RR |
| `public/assets/*.woff2` | Fontes locais; licenças OFL incluídas |
| `public/manus-routes.json` | Declaração das páginas existentes |

A imagem clínica final está incluída em `public/assets/clinical-hero.webp`. A versão de backup usa uma referência local, pelo que o website não depende da imagem gerida ou de um endereço temporário de pré-visualização. Todas as fontes, scripts e estilos também estão guardados localmente.

## Conteúdo por confirmar

O nome e a especialidade foram fornecidos para o projeto. Antes da publicação definitiva, substituir os campos pendentes de biografia, formação, cédula profissional, email, telefone e local de atividade por informações reais aprovadas. A imagem é ilustrativa, não uma fotografia da médica ou da sua clínica. Os contextos de atuação apresentados explicam a especialidade e não confirmam serviços efetivamente prestados. Não existem testemunhos ou qualificações inventadas.

Os textos informativos têm como referência [Guy’s and St Thomas’ NHS Foundation Trust — Anaesthetic](https://www.guysandstthomas.nhs.uk/health-information/anaesthetic). Devem ser revistos pela médica antes da publicação. Não substituem uma avaliação médica.

## Contactos e formulário

Preencher `public/assets/site-config.js` com os dados confirmados:

```js
window.SITE_CONFIG = Object.freeze({
  email: 'EMAIL_PROFISSIONAL_CONFIRMADO',
  phone: 'TELEFONE_CONFIRMADO',
  location: 'LOCAL_CONFIRMADO',
  contactEnabled: true
});
```

Com o email válido e `contactEnabled: true`, o formulário permite preparar um rascunho num programa de email através de `mailto:`. A pessoa deve abrir, rever e enviar a mensagem nesse programa; o website não confirma entrega. Sem configuração, aparece uma mensagem explícita de que nada foi enviado ou guardado.

Não há backend, armazenamento de mensagens, base de dados, analytics ou sistema de marcação. Não incluir exames, diagnósticos ou outros dados sensíveis no formulário. Antes de ativar os contactos, atualizar a informação de privacidade com os dados do responsável pelo tratamento e as condições reais. O alojamento pode manter registos técnicos de acesso independentemente do código do website.

## Adicionar páginas posteriormente

Criar novas páginas em `public/`, por exemplo `sobre.html` e `contactos.html`. Reutilizar `assets/styles.css` e o cabeçalho/rodapé, adaptar os links e atualizar `manus-routes.json`. O JavaScript atual foi feito para a página inicial: se for reutilizado numa página sem o formulário ou outras secções, acrescentar guardas para elementos ausentes. Não existem links para páginas vazias nesta versão.

## Metadados e publicação

A versão de apresentação tem `noindex, nofollow` para não indexar campos profissionais incompletos. Depois de validar todo o conteúdo, trocar para `index, follow`. Adicionar o domínio real ao canonical, `og:url`, `og:image` e sitemap; esses endereços não foram inventados. O output estático é `public/`, sem etapa de compilação. A pré-visualização não é uma publicação definitiva.

## Funcionalidades

Navegação por âncoras com cabeçalho fixo, menu móvel com estado acessível, perguntas frequentes com elementos `details`, diálogos nativos, validação HTML do formulário, estados de contacto transparentes, link para saltar para o conteúdo e respeito por preferências de movimento reduzido. Fontes guardadas localmente para evitar pedidos externos ao Google Fonts.

## Cópia de segurança independente

Esta pasta contém o website atual e os recursos necessários para o restaurar num servidor HTTP estático, sem credenciais da Manus. Consulte também `RESTAURO.md` na raiz do repositório. Não há base de dados ou mensagens de pacientes para exportar. A configuração de contactos está vazia de propósito.

Testes: `node tests/interactions.cjs` e, com o servidor HTTP local ativo na porta 3000, `python3 tests/structure.py`.
