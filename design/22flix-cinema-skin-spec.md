# 22Flix Cinema — Skin specification

## Identity

**Skin name:** 22Flix Cinema  
**Product:** 22Flix  
**Design direction:** a high-quality streaming experience inspired by Netflix's information hierarchy and interaction patterns, with original 22Flix branding and assets. Do not copy Netflix logos, proprietary artwork, or exact branded assets.

The interface must feel cinematic, fluid, quiet, and immediately understandable from a sofa. Accessibility at viewing distance is a first-class requirement.

## Visual system

- Default canvas: near-black charcoal (#08090D); surfaces: #12141B and #1B1E27.
- Primary text: warm white (#F5F5F7); secondary text: cool light gray (#B9BEC9).
- Accent: restrained 22Flix crimson (#E50920) for primary actions and active navigation only.
- Use large artwork, generous spacing, soft gradients behind text, and minimal borders.
- Avoid tiny metadata, thin type, dense grids, excessive badges, and low-contrast gray text.
- Use a clean sans-serif system font stack. Titles should be bold and highly legible.

## Home screen

1. Persistent top navigation with 22Flix mark, Início, Filmes, Séries, Minha lista, and a prominent search action.
2. Large cinematic hero banner (approximately 45–55% of the first viewport height on TV), with backdrop, gradient scrim, title, concise synopsis, metadata, and clear actions: Assistir, Mais informações, and Minha lista.
3. **Destaques:** a prominent curated showcase near the top. It should feel like a streaming-service premiere carousel: large cinematic backdrop/poster, strong title typography, short synopsis, optional restrained tags (Novo, Em alta, Estreia) only when supported by real metadata, and obvious Assistir / Mais informações actions. Allow remote users to move between featured titles with left/right navigation and clear position indicators. Auto-rotation, if used, must be slow, subtle, pausable, and disabled when reduced motion is enabled.
4. **Top 10 — Filmes:** a dedicated horizontal rail with oversized ranking numerals (1–10) partially behind or beside large posters, evoking the recognizable streaming Top 10 treatment. Numerals must remain legible and not obscure artwork or titles. Each card opens the real detail page.
5. **Top 10 — Séries:** a separate ranked rail using the same visual language, not mixed with films.
6. Additional horizontal content rails with large poster cards:
   - Continue assistindo
   - Minha lista
   - Em alta agora
   - Adicionados recentemente
   - Recomendados para você
   - Mais populares por gênero, when useful
7. Keep rail headings large and visually distinct. Cards must have consistent aspect ratios and clear selected/focused states.
8. Continue-watching cards show progress only when reliable playback progress is available.
9. **Ranking integrity:** never invent popularity or viewing counts. Prefer real Jellyfin play statistics when available, or a configured and clearly identified metadata/trending provider. If no trustworthy ranking source is available, label the row accurately (for example, “Destaques do 22Flix” or “Mais recentes”) instead of presenting a fabricated Top 10. Define the ranking period/source in the UI where practical.

## Core screens and behavior

### Search
- Search available from every main screen.
- Large, high-contrast search field and on-screen keyboard support.
- Results grouped or filterable by Filmes and Séries.
- Search must query existing Jellyfin/Seerr capabilities; do not create a fake local catalogue.
- Empty, loading, offline, and no-results states must be designed.

### Favorites / Minha lista
- A persistent saved list with add/remove actions from cards and detail pages.
- Use the existing backend's supported favorites/watchlist capability where available.
- If Jellyfin and Seerr expose different list semantics, keep them explicit rather than silently duplicating data.

### Detail page
- Large backdrop and title artwork, readable synopsis, year, runtime, genres, and available audio/subtitle metadata only when supplied by the server.
- Primary actions: Assistir / Retomar, Adicionar ou remover da Minha lista, Solicitar (when supported by Seerr).
- For series, show seasons and episodes in a clear, large-text layout.

### Movies and series browsing
- Dedicated catalogues with visible filters and sort controls.
- Filters may include year, genre, country, audio language, and subtitle language only when the underlying data is trustworthy.
- Do not claim a language, provider, or availability that the server has not reported.

### Settings
- Text size: Padrão / Grande / Extra grande.
- Contrast: Padrão / Alto contraste.
- Reduce motion option.
- Preserve settings between sessions.

## Accessibility and TV-first interaction

- Design for 10-foot viewing distance and 1920x1080 first; scale cleanly to 4K and smaller screens.
- Minimum TV body text target: 24–28 px; important metadata should not fall below 20 px. Hero title should be substantially larger (48–64 px where layout permits).
- Provide scalable typography and spacing without clipping or hiding actions.
- Maintain strong text/background contrast; never rely on color alone to communicate state.
- Remote navigation must work with D-pad arrows, OK/Enter, Back/Escape, and predictable focus order.
- Focus ring must be unmistakable: thick accent outline plus subtle glow and a small scale/elevation change. Never make focus visible only through color.
- No hover-only actions. Every action must be reachable by remote and keyboard.
- Support mouse, touch, keyboard, and Android/Google TV remote navigation.
- Respect reduced-motion preferences; transitions should be smooth but brief.

## Responsive behavior

- **TV:** landscape-first, D-pad navigation, wide hero, horizontal rails, large type.
- **Desktop:** same visual language with a wider content area and pointer/keyboard support.
- **Mobile:** compact navigation and responsive card layout without reducing accessibility.

## Integration and non-regression requirements

- Preserve existing Jellyfin, Seerr, Sonarr, Radarr, Bazarr, and Docker configuration.
- Do not replace or fork backend services merely to implement the skin.
- Search, playback, request, watchlist, and progress actions must use real existing APIs and report errors honestly.
- Keep API keys, tokens, credentials, and internal host details out of source control.
- No destructive database migrations. Add changes incrementally and keep a rollback path.
- First inspect the actual application/plugin source and its upstream version before implementing UI code. This repository currently contains planning documentation only; do not pretend a working skin has been installed until the implementation is built and tested.

## Implementation sequence

1. Identify the exact frontend/plugin source, upstream version, build process, and current Seerr/Jellyfin integration points.
2. Create a separate feature branch and a visual prototype of the home screen.
3. Implement shared design tokens, typography, navigation, focus handling, and reusable poster/hero components.
4. Wire featured content, trustworthy Top 10 ranking sources, search, favorites/watchlist, details, and playback/request actions to the real backend.
5. Test keyboard, mouse, touch, and Android TV remote navigation; verify no regressions in existing services.
6. Package and deploy only after a successful build and a reversible test.

## Acceptance criteria

- The home screen has a cinematic featured showcase and clearly separated horizontal rails.
- Separate Top 10 films and Top 10 series rails use real, explainable ranking data.
- Search returns real catalogue results.
- Minha lista persists and correctly adds/removes items.
- Details and playback/request actions work against the existing services.
- Every screen is navigable without a mouse.
- Typography and focus remain clearly visible from a sofa.
- Existing Jellyfin/Seerr automation and download services remain untouched.
