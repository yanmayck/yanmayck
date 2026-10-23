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

## Recursos

- Filtros por tipo de projeto.
- Painéis modais de engenharia com foco e fechamento por Escape.
- Especialidades em abas acessíveis por teclado.
- Terminal com comandos `help`, `whoami`, `projects`, `stack`, `focus`, `clear` e histórico com setas.
- Alternância PT/EN.
- Animações de órbita, flutuação, faixa contínua e brilho que acompanha o ponteiro.
- Layout responsivo e respeito a `prefers-reduced-motion`.

## Validação realizada

Chromium/Playwright: filtros, abertura e fechamento dos dois projetos, Escape, navegação por teclado nas abas, comandos e histórico do terminal, inserção segura de texto, troca de idioma, largura de 390 px sem rolagem horizontal e preferência de movimento reduzido. Nenhum erro JavaScript observado. Os testes de navegador foram executados nesta sessão; o deploy público ainda precisa ser confirmado.
