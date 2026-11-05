# 22Flix JellySeerr

Projeto de personalização e extensão da experiência Jellyfin + Seerr para um servidor doméstico 22Flix.

## Skin

A identidade visual planejada para a interface é **22Flix Cinema**: uma experiência cinematográfica inspirada na organização visual de serviços de streaming como a Netflix, com identidade própria, foco em Android/Google TV, navegação por controle remoto e tipografia acessível à distância.

Especificação visual e funcional: [design/22flix-cinema-skin-spec.md](design/22flix-cinema-skin-spec.md).

## Objetivos

1. Traduzir a interface JellySeerr para português brasileiro.
2. Diagnosticar cliques que não abrem categorias e carrosséis de descoberta vazios.
3. Adicionar filtros por país, ano, plataforma e idiomas de áudio/legenda quando houver dados confiáveis.
4. Integrar TV ao vivo via fontes públicas/oficiais compatíveis com M3U e EPG.
5. Desenvolver identidade visual cinematográfica própria e acessível em desktop e TV.

## Cuidados

- Preservar a instalação atual do Jellyfin, Sonarr, Radarr, Bazarr e Seerr.
- Não publicar chaves API, credenciais ou endereços internos.
- Não assumir que uma faixa de áudio ou legenda está disponível sem dados de fonte verificável.
- Não armazenar links privados de transmissão ou mídias protegidas sem autorização.
- Código de terceiros deve respeitar suas licenças; a investigação do APK é apenas referência técnica.

## Estado

Planejamento inicial. A especificação da skin 22Flix Cinema foi registrada em `design/22flix-cinema-skin-spec.md`. Ainda não há código-fonte da interface neste repositório; a implementação depende de identificar a fonte real do frontend/plugin e seu processo de build.

## Próxima etapa

Identificar os arquivos e o sistema de internacionalização do plugin upstream antes de implementar ou empacotar correções.
