# Publicação preparada

- Curso: /home/nmaldaner/projetos/da-ideia-ao-app-v6 — main.
- Portal: /home/nmaldaner/projetos/output/da-ideia-ao-app-v6/publicacao/portal — codex/da-ideia-ao-app-v6; commit 6cdd910; destino origin/main (NeiMaldaner/portal).
- Buscas: pasta irmã inemabuscas; commit 0fee7ae; destino remoto inemabuscas/main (inematds/inemabuscas), não origin legado.
- PRO: pasta irmã inemapro-mono; commit a16c466; destino origin/main (inematds/inemapro).

API GitHub: autorização expressa solicitada nesta conversa, ainda pendente, somente para criar repo público e habilitar Pages. Não usar API de modelos. Não dar push nos catálogos antes de conferir o curso publicado.

Antes de integrar, conferir commits novos nos originais e remotos; não sobrescrever mudanças de outras sessões. Portal original tem tsconfig.tsbuildinfo modificado por outra sessão; PRO original tem apps/pro/data/atualizacao.json modificado por outra sessão. Usar push dos branches isolados para main, sem forçar. Se divergir, rebase e regenerar os derivados com todas as entradas preservadas.

A geração do catálogo PRO normalmente chama gh api para atualizar repos. Nesta preparação, um script temporário copiou o gerador e substituiu apenas essa consulta pelo array repos já existente em apps/pro/data/catalog.json do original. O temporário foi removido após gerar. Não usar publica.sh sem revisar essa chamada diante da regra de APIs. As demais gerações usaram PORTAL_DIR e os caminhos locais de wiki/prompts. Metadados novos em publicacao.json.

Publicação do curso: git push para origin; GitHub Pages por main e raiz; conferir HTTP e conteúdo de index.html, curso.html, pratica/index.html, materiais/kit-organizador.zip e capa/capa.png. Portal: push suficiente, sem consultar Vercel.
