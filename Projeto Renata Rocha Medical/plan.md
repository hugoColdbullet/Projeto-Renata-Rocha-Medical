# Renata Rocha — plano aprovado

## Objetivo e âmbito
Website institucional HTML, de página única, para **Renata Rocha — Médica Especialista em Anestesiologia**. Estilo inspirado na profissão médica. Outras páginas apenas posteriormente. Blueprint confirmado: cabeçalho e navegação por âncoras; apresentação e chamada à ação; área Sobre (biografia, formação, abordagem clínica); especialidade e contextos de atuação; contactos e formulário; rodapé; responsividade; HTML semântico e organizado.

## Implementação
HTML estático, CSS e JavaScript vanilla, sem framework, base de dados ou backend. Sem dependências de compilação. Conteúdo visível no HTML inicial. `public/` é a raiz de publicação; Preview na porta 3000 com servidor estático. Formulário valida os campos, não guarda dados e prepara email apenas quando existir um email profissional configurado; enquanto faltar, informa inequivocamente que não há envio. Não pedir informação clínica sensível. Nenhuma integração de marcação ou promessa de envio será simulada.

Informação confirmada: nome e especialidade fornecidos pelo utilizador. Biografia, formação, cédula profissional, fotografia, instituições, telefone, email e morada não fornecidos: não inventar. Identificar os campos pendentes. Textos da especialidade são informativos, não declarações de serviços efetivamente prestados. Não criar testemunhos, números de experiência ou resultados clínicos fictícios. Imagem conceptual de ambiente clínico, sem pessoas, identificada como ilustrativa. Conteúdo médico genérico apoiado em https://www.guysandstthomas.nhs.uk/health-information/anaesthetic; sem orientações individuais.

## Identidade visual
- **Movimento:** minimalismo editorial clínico, com equilíbrio entre precisão médica e proximidade humana.
- **Princípios:** clareza; serenidade; hierarquia forte; honestidade dos dados.
- **Cores:** verde-petróleo transmite rigor; sálvia suaviza o ambiente hospitalar; marfim acrescenta calor sem perder a limpeza visual. Cor de assinatura: verde-petróleo `#234f47`.
- **Layout:** abertura assimétrica com texto editorial à esquerda e ambiente clínico vertical à direita; secções alternam listas, faixas e colunas amplas, com espaço negativo e numeração discreta.
- **Elementos de assinatura:** monograma RR entrelaçado tipográfico; linha de monitorização estilizada; pequenos rótulos em versais e números de secção.
- **Interações:** navegação direta, links descritivos, acordeões nativos, menu móvel com estado acessível e formulário transparente.
- **Animações:** transições de 180–240 ms, deslocação suave por âncoras; sem movimentos incessantes; respeitar `prefers-reduced-motion`.
- **Tipografia:** Cormorant Garamond nos títulos (fallback Georgia), Manrope no corpo (fallback sistema). Display editorial de 56–78 px; títulos de 34–52 px; corpo de 16–18 px.
- **Essência:** apresentação médica clara de Renata Rocha e da anestesiologia, dirigida a quem procura informação e contacto profissional. Personalidade: serena, rigorosa, próxima.
- **Voz:** clara, acolhedora, sem superlativos ou garantias. Exemplos: «Cuidar começa por escutar.»; «Conheça o papel da anestesiologia.»
- **Marca:** logótipo tipográfico com monograma RR, nome em serifa e especialidade em versais espaçadas; sem usar símbolos oficiais de organizações médicas.

## Estrutura
- `public/index.html`: única página com secções Início, Sobre, Anestesiologia, O percurso, Perguntas frequentes e Contactos; diálogos de privacidade/informação editorial.
- `public/assets/styles.css`: tokens, estilos e breakpoints.
- `public/assets/site-config.js`: contactos e dados profissionais configuráveis.
- `public/assets/main.js`: menu, realce de navegação e formulário.
- `public/assets/favicon.svg`: monograma da marca.
- `public/manus-routes.json`: única rota `/`.
- `app.config.ts`: identificação visual do projeto.
- `README.md`: instruções para edição, configuração de contactos e expansão.
- `TODO.md`: resultados e respetivo estado.

## Expansão futura
Manter secções independentes, assets partilhados e navegação facilmente adaptável a novas páginas. Não criar agora páginas vazias ou ligações sem destino. O formulário é um ponto de entrada configurável, não um sistema de gestão clínica. Publicação não solicitada: entregar Preview e checkpoint, com projeto HTML transferível.
