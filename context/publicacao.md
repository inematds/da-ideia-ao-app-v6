# Publicação concluída

Curso público: https://inematds.github.io/da-ideia-ao-app-v6/
Repositório: https://github.com/inematds/da-ideia-ao-app-v6
Ficha do portal: https://www.inema.club/cursos/318-da-ideia-ao-app-v6-desenvolva-com-ia-passo-a-passo/

GitHub Pages usa main e raiz. Todas as URLs verificadas estão em verificacao/publicado.json, com HTTP 200 e igualdade de bytes. Pushes dos catálogos:
- portal: c9951c6a8464bb2e6999a06226137fb179ad5bce
- inemabuscas: e06cce6883601a4bca03d0b1e30d57a0fce0c41d
- inemapro-mono: dceb2d14d0fe0ab38e699cce5f6621e8b6e5505b

Portal usa origin (NeiMaldaner/portal); buscas usa inemabuscas (inematds/inemabuscas), não o origin legado; PRO usa origin (inematds/inemapro). Os catálogos incluem todas as atualizações concorrentes encontradas antes de publicar. Testes e build passaram; Vercel não foi consultado.

A API GitHub tem autorização permanente nas regras globais desde 2026-10-05. Na preparação sem autorização, a lista de repos foi preservada de um snapshot. Após a autorização, a geração final usou o script oficial. Nenhuma API de modelos foi usada.

A fonte da página do curso é scripts/construir.py + scripts/conteudo*.py. O construtor lê context/publicacao.json para manter a ficha do portal após remontar.
