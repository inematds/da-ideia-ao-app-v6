# Da Ideia ao App v6

**Desenvolva com IA, passo a passo.** Curso aberto e gratuito do INEMA, em português: 24 aulas, seis módulos, aplicativo pessoal de treino e kit editável.

Abra `index.html` para a apresentação e `curso.html` para estudar. O laboratório fica em `pratica/index.html`. Os registros do laboratório ficam no navegador; não há contas, colaboração, sincronização ou proteção multiusuário. Use somente dados fictícios.

## Percurso

1. Definir uma ideia e seus critérios.
2. Construir e preservar a primeira versão.
3. Entender tela, regras e armazenamento.
4. Testar funções, limites e correções.
5. Analisar dados e permissões para uma expansão futura.
6. Preparar publicação, operação e próxima versão.

Leitura no celular; edição no computador. A configuração inicial de um agente de programação é separada do tempo das aulas. Quem ainda não tem agente pode estudar e experimentar o aplicativo pronto; para construir sua própria versão, precisa de um ambiente com acesso aos arquivos.

## Reprodução local

```bash
python3 scripts/construir.py
node ~/.claude/skills/formato-curso-v6/scripts/auditar-curso.cjs curso.html --json verificacao/auditoria.json
node ~/.claude/skills/formato-curso-v6/scripts/testar-motor.cjs curso.html
node scripts/verificar.cjs
```

A montagem usa a skill v6 local e Python com Pillow. A verificação de navegador usa Playwright instalado neste ambiente. O site publicado funciona com arquivos estáticos, sem essas ferramentas de construção.

Fontes editáveis: `scripts/conteudo.py`, `scripts/conteudo2.py`, `scripts/conteudo3.py`. O construtor gera aulas, curso, landing, ilustrações vetoriais locais e kit. Não altera os assets do motor v6. Ilustrações criadas localmente por código, sem serviços de geração ou créditos. Telas de conversa são exemplos didáticos, não respostas capturadas de um modelo. A entrevista fornecida pelo usuário orientou os temas; não foram adotadas suas promessas de produtividade ou segurança.

Relatórios em `verificacao/` e `context/`. Revisão simulada não equivale a teste com pessoas reais.

## Publicação

Destino solicitado: `inematds/da-ideia-ao-app-v6`, GitHub Pages na raiz de `main`; depois catálogo e feed do portal, buscas e PRO. Publicação externa pendente da criação do remoto e habilitação de Pages. A regra global exige autorização expressa antes de usar a API do GitHub para essas duas operações.

## Mais no INEMA.CLUB

Destino da ficha após publicação: https://www.inema.club/cursos/316-da-ideia-ao-app-v6-desenvolva-com-ia-passo-a-passo/

Guia: https://www.inema.club/aprender-inteligencia-artificial/

Catálogo: https://www.inema.club/cursos/
