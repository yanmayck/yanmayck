# Portfólio interativo / Interactive portfolio

O site fica em `index.html`, com estilos em `portfolio.css` e comportamento em `portfolio.js`. Não usa frameworks, serviços externos, analytics ou formulários de coleta. As imagens são as mesmas do README.

## Publicação no GitHub Pages

No repositório `yanmayck/yanmayck`:

1. Abra **Settings → Pages**.
2. Em **Build and deployment**, selecione **Deploy from a branch**.
3. Selecione **main**, pasta **/(root)**, e clique em **Save**.
4. Aguarde o deploy do GitHub. Confirme o endereço exibido na própria página de configurações antes de divulgar o site.

Esta sessão conseguiu enviar arquivos por Git, mas a consulta à API de configuração do Pages retornou `Forbidden`. A publicação do site não foi confirmada. Depois de ativado, use o endereço informado pelo GitHub para ligar o README ao portfólio.

## Desenvolvimento

Na raiz do checkout existente, execute `python -m http.server 8765 --bind 127.0.0.1`. O site não tem dependências de instalação. O terminal é uma simulação local: só aceita os comandos documentados e não executa shell, faz requisições ou envia entradas a servidores.

## Interface

A página tem apenas o header e o terminal. Projetos, tecnologias e links aparecem dentro do histórico. O visitante pode digitar ou clicar nos comandos sugeridos.

- `help`, `sobre` / `about`, `projetos` / `projects`, `stack`, `contato` / `contact`.
- `ia`, `ai`, `stack ia` ou `cat ai.txt` mostram frameworks, SDKs, embeddings, pgvector, RAG, busca híbrida, memória, ferramentas e orquestração. Logos locais com origem documentada em `assets/ai/README.md`.
- `ls`, `pwd`, `cd elloai`, `cd cepi`, `cd ..`, `cd ~`.
- `cat about.txt`, `cat stack.txt`, `cat README.md`.
- Histórico com ↑/↓, sugestões ao digitar e autocomplete que alterna opções com Tab.
- `tree` mostra os arquivos; `history` lista os comandos da sessão.
- `theme green`, `theme amber`, `theme light` e `theme default` trocam as cores.
- Abas para início, projetos e stack; botão de tela cheia.
- Limpeza com `clear` ou Ctrl+L; Ctrl+C cancela a entrada.
- `cat stack.txt` dentro de um projeto mostra a stack específica dele.
- Alternância PT/EN, inclusive dentro de um projeto.
- Sem dependências, execução de shell, requisições feitas pelo terminal ou coleta de dados.
- Layout responsivo e animações que respeitam `prefers-reduced-motion`.

## Validação realizada

Chromium/Playwright: navegação clicável, diretórios e prompt, conteúdo dos dois projetos, comandos e aliases, histórico, autocomplete, troca de idioma dentro de um projeto, limpeza por comando e Ctrl+L, entrada de texto sem execução de HTML, largura de 390 px sem rolagem horizontal e preferência de movimento reduzido. Nenhum erro JavaScript observado. Os testes de navegador foram executados nesta sessão; o deploy público ainda precisa ser confirmado.

Validação adicional: sugestões clicáveis, autocomplete cíclico, temas e tratamento de tema inválido, árvore de arquivos, histórico, Ctrl+C, tela cheia e retorno, abas, `pwd` no diretório de projetos e leitura da stack local de cada projeto. Resultados extensos abrem no começo da resposta.
