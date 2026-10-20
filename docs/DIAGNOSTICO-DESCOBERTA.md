# Diagnóstico: descobertas vazias e navegação inativa

## Sintomas observados (20/10/2026)
- Seerr em localhost:5055 funciona e recebe solicitações.
- JellySeerr aparece no Jellyfin, com Seerr/Radarr/Sonarr/File Transformation conectados.
- Categorias do catálogo Jellyfin aparecem em inglês.
- Algumas fileiras mostram `No items to show`, outras exibem cartões cinza e filtros como plataformas não navegam.
- Nenhuma evidência ainda de que os pedidos via JellySeerr cheguem ao Seerr; não confundir essa falha com os pedidos feitos diretamente no Seerr.

## Distinções necessárias
1. **API Seerr funcionando** não implica que o JavaScript da interface injetada esteja funcionando.
2. **Cartão cinza** pode indicar carregamento, imagem bloqueada ou erro de renderização.
3. **Fileira vazia** pode ser resultado sem títulos, erro de rede, erro de permissão ou exceção JS.
4. **Clique inativo** pode ser evento não registrado, camada sobreposta, rota não tratada ou erro JS — causa ainda não confirmada.

## Teste controlado, sem fornecer chaves de API
1. Abrir Jellyfin no Chrome e entrar em aba Filmes/Séries no menu superior direito.
2. Pressionar F12 → Console; limpar mensagens antigas.
3. Clicar em uma categoria de streaming ou gênero que não responde.
4. Anotar apenas mensagem de erro, hora e ação realizada; ocultar tokens, cookies, API keys e URLs com parâmetros privados.
5. Na aba Network, filtrar por `JellySeerr` e `discover` e conferir códigos HTTP (200, 401, 403, 404, 500), sem exportar cabeçalhos de autenticação.
6. Repetir o título via Seerr diretamente para comparar; registrar se o pedido é recebido no Sonarr/Radarr.

## Hipóteses a validar na implementação
- Eventos dos cartões conectados às rotas de descoberta.
- Links de provedores compatíveis com o roteador do Jellyfin.
- Estados vazios e mensagens de erro expostos em vez de falha silenciosa.
- Tratamento de localização pt-BR no código do plugin, sem confundir com idioma do Seerr.

## Fonte upstream
https://github.com/ThuGie/JellySeerr

A implementação deve partir dos arquivos JavaScript e C# reais. Nenhuma causa está confirmada e nenhum pacote corrigido foi compilado ainda.
