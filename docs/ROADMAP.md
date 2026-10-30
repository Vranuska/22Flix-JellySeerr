# Plano técnico de execução — 22Flix

## Regras
- Desenvolvimento isolado na branch `feature/pt-br-discovery-foundation`.
- Não modificar o Jellyfin instalado nem guardar API keys no repositório.
- Basear mudanças no código-fonte real do upstream [ThuGie/JellySeerr](https://github.com/ThuGie/JellySeerr), licença MIT.
- Validar a compilação e os testes antes de criar um pacote instalável.
- Não prometer idioma de áudio/legenda com base apenas no idioma original do título.

## Fase 0 — Auditoria (em andamento)
- [x] Identificar upstream, licença e requisitos (Jellyfin 10.11.9+, File Transformation e Seerr).
- [x] Identificar comandos de build upstream: `dotnet build JellySeerr.sln -c Release`.
- [ ] Inspecionar arquivos C#, JavaScript e CSS reais: endpoints, injeção, navegação e strings.
- [ ] Confirmar a causa de cliques inativos e carrosséis vazios com logs do navegador/servidor.
- [ ] Registrar versão exata instalada e critérios de compatibilidade.

## Fase 1 — Tradução
- [x] Criar catálogo inicial `locales/pt-BR.json`.
- [x] Criar validação automatizada de chaves e strings.
- [ ] Localizar no código original os pontos de renderização dos textos.
- [ ] Integrar tradução respeitando idioma/preferência do usuário.
- [ ] Cobrir mensagens dinâmicas, estados vazios, detalhes e pedidos.
- [ ] Testar carregamento em conta comum e conta administradora.

## Fase 2 — Correção funcional
- [ ] Reproduzir clique inativo em gêneros/estúdios/plataformas.
- [ ] Verificar interceptação de links, tratamento de erros e renderização de estados vazios.
- [ ] Testar com dados reais da API Seerr e títulos existentes/não existentes.

## Fase 3 — Filtros
- [ ] Origem, ano, gênero, plataforma, áudio, legenda.
- [ ] Explicitar quando informações de dublagem e legendas são desconhecidas.
- [ ] Não confundir disponibilidade no serviço com a disponibilidade em uma cópia solicitada.

## Fase 4 — TV ao Vivo e visual
- [ ] M3U/XMLTV de fontes verificadas e permitidas.
- [ ] Interface 22Flix acessível por controle remoto; preservar cliente LG/Fire TV.
- [ ] Teste local, pacote versionado e procedimento de restauração.

## Diagnóstico de aceitação
1. Três perfis domésticos mantêm permissões corretas.
2. Nenhuma alteração em Sonarr/Radarr/Seerr ao apenas atualizar a UI.
3. Clique em cada categoria navega ou mostra uma mensagem de erro útil.
4. Tradução pt-BR não altera IDs, rotas, campos de API ou chaves secretas.
5. Nenhum deploy antes da compilação e dos testes.
