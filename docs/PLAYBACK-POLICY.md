# Política de reprodução leve — 22Flix

## Decisão

Não incorporar um segundo motor de detecção de aberturas/créditos ao plugin 22Flix-JellySeerr. Priorizar compatibilidade com **Media Segments** nativos do Jellyfin e com o provedor de segmentos já configurado pelo administrador.

## Comportamento desejado

- Exibir **Pular abertura** quando existir segmento `Intro` reconhecido pelo cliente.
- Exibir **Pular créditos** quando existir segmento `Outro` reconhecido pelo cliente.
- Não pular automaticamente os créditos por padrão (preservar cenas pós-créditos).
- Não realizar análise de áudio, vídeo ou varredura de biblioteca ao abrir a página de reprodução.
- Não ativar análises adicionais em paralelo ao plugin atual.
- Respeitar as opções do usuário e os recursos dos clientes (web, TV LG e Fire TV podem variar).

## Critérios de aceite

1. Nenhum novo processamento de mídia introduzido pelo JellySeerr.
2. Quando não houver marcador, reprodução normal sem erro.
3. Testar separadamente pular abertura e créditos com episódio que já possua marcadores.
4. Verificar suporte em cada cliente; não prometer comportamento idêntico em aplicativos de TV.

## Referência

- https://jellyfin.org/docs/general/server/metadata/media-segments/

## Estado

Decisão documentada; nenhuma alteração de reprodução instalada ou testada.
