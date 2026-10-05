# Leitura simulada — aulas 17–24

Data: 2026-10-05. Método: leitura integral dos HTML e inspeção visual das oito capturas `verificacao/capturas/aula-N-celular-papel.png`. Simulação feita por agente; **não é teste humano real**. Não executa nem certifica segurança de aplicação compartilhada.

Personas alternadas por blocos: aulas 17–19, professora de 55 anos; aulas 20–22, prestador de serviço de 34 anos; aulas 23–24, professora de 55 anos. Ambos usam WhatsApp/e-mail e ocasionalmente chat de IA, nunca programaram, estudam no celular com 15 minutos.

Nas capturas, os exemplos estão dentro de cartões de texto, com contraste e separação reconhecíveis. A ilustração inicial repetida não explica o assunto específico da aula. O teste dos 5 segundos depende principalmente da leitura do título/rótulo; não presumimos que a pessoa compreendeu só pela imagem. A trilha visual é consistente, mas o conjunto é longo no celular. A densidade maior aparece nos prompts; o botão copiar ajuda.

## Aula 17 — professora, 55 anos

| Step | Em 5 segundos: ideia visual | Trava concreta | O que pularia |
|---|---|---|---|
| 1 | Campos propostos versus campos que ficam; entendi escolher menos dados. | Nenhuma relevante: os campos estão nomeados. | Legenda que repete o resultado. |
| 2 | Pedido e duas tarefas fictícias; entendi inventar exemplos. | Nenhuma relevante. | Exemplo profissional, se já compreendeu pelo cartão. |
| 3 | Lista do que conferir antes de enviar uma captura; entendi revisar tudo. | A prática pede revisar uma captura fictícia, mas não indica uma fornecida. | Repetição entre resposta e cola. |

Prática: executável nas notas para campos e exemplos; revisão da captura exige inventá-la. Promessa: cumprida quanto à retirada de dados. Nota **9/10**. Uma melhoria: fornecer uma captura fictícia com três itens a marcar, ou autorizar explicitamente desenhar essa captura no papel. A referência final deveria responder também aos campos, não só à captura.

## Aula 18 — professora, 55 anos

| Step | Em 5 segundos: ideia visual | Trava concreta | O que pularia |
|---|---|---|---|
| 1 | Conta A usa A e conta B usa B; reconheci a separação. | Nenhuma relevante: autenticação/autorização são explicadas. | A legenda após o cartão. |
| 2 | Visitante, responsável, outra pessoa; entendi três perfis. | O exemplo é uma lista, não a matriz prometida; preciso imaginar as colunas. | Nada antes de descobrir como preencher. |
| 3 | Esconder na tela não basta; compreendi a ideia. | “Parte confiável”/“operação” não mostra onde está a regra, embora o objetivo seja análise. | Pularia discussão técnica posterior, se houvesse. |

Prática: executável na folha vinculada; a promessa de montar a matriz é adequada, sem prometer implementar contas. Nota **8,5/10**. Correção prioritária: apresentar matriz preenchida (pessoa × ler × alterar) no gabarito, substituindo respostas soltas. Acrescentar “no serviço que entrega os dados, fora da tela do visitante” à parte confiável. Não precisa introduzir configuração de serviço.

## Aula 19 — professora, 55 anos

| Step | Em 5 segundos: ideia visual | Trava concreta | O que pularia |
|---|---|---|---|
| 1 | Pedido de senha versus valor fictício; entendi não entregar senha. | “Chave privilegiada” é abstrata; falta exemplo de poder que concede. | Nenhum passo, assunto parece importante. |
| 2 | Variável segredo não protege senha; ideia compreendida. | Nenhuma relevante: conteúdo do navegador é explicado. | Legenda repetida. |
| 3 | Endereço do site não protege todas as chamadas; só entendi parcialmente. | Endereço/origem/arquitetura/restrição de rede entram juntos. | Pularia esse cartão por não saber o que fazer com ele. |

Prática: cenário claro, mas a referência aberta fala de redes e uma variável; não enumera os três problemas pedidos. Promessa de reconhecer segredos: cumprida no básico. Nota **8/10**. Uma melhoria: gabarito direto: senha na página → retirar e usar exemplo fictício; botão oculto → não prova permissão; falta de conferência → testar recusa no serviço que entrega/altera dados. Definir chave privilegiada como “chave que pode ler ou alterar dados de muitas pessoas”. Na parte de redes, dar analogia concreta: visitante usa a própria conexão de casa/celular.

## Aula 20 — prestador de serviço, 34 anos

| Step | Em 5 segundos: ideia visual | Trava concreta | O que pularia |
|---|---|---|---|
| 1 | A com A, B com B; entendi preparar casos diferentes. | O título parece pedir duas contas reais; só no step 3 descubro que vou analisar no papel. | Nada enquanto procurar botão de contas. |
| 2 | B tenta alterar A e deve falhar; entendi rejeitar e conferir registro. | Nenhuma relevante após entender que é simulado. | Legenda repetida. |
| 3 | Leitura cruzada reprova; entendi que a análise não certifica o produto. | “Matriz da aula anterior” aponta à 19, mas a matriz foi ensinada na 18. | Nada. |

Prática: executável e correta como simulação. Promessa: planejar testes, sem garantir proteção real, está calibrada. Nota **8,5/10**. Uma melhoria: avisar na abertura “Nesta aula analisaremos resultados simulados, sem criar contas” e corrigir a referência para “matriz da aula 18”.

## Aula 21 — prestador de serviço, 34 anos

| Step | Em 5 segundos: ideia visual | Trava concreta | O que pularia |
|---|---|---|---|
| 1 | Demonstração pessoal/dados locais; compreendi o aviso. | Nenhuma relevante. | Legenda repetida. |
| 2 | Lista de etapas para publicar; ideia geral compreendida. | Não sei executar habilitar publicação; aprofundamento posterior resolve apenas em nível geral. | Detalhe técnico se puder fazer só análise. |
| 3 | Página/cadastro/filtro/atualizar; entendi conferir no endereço público. | “Janela limpa” não indica se outra aba basta. | Nada. |

Prática: funciona como inspeção da demo e preparação, não como publicação efetiva. Promessa escrita é preparar uma versão e conferência, portanto é mais precisa que o título imperativo. Nota **8/10**. Uma melhoria: trocar “demonstração publicada indicada abaixo” por “toque em Abrir o aplicativo de treino, acima”; explicar janela limpa como “janela privada/anônima ou outro navegador, não apenas outra aba”; gabarito com checklist de arquivos, aviso e testes, em vez de respostas soltas.

## Aula 22 — prestador de serviço, 34 anos

| Step | Em 5 segundos: ideia visual | Trava concreta | O que pularia |
|---|---|---|---|
| 1 | Horário/ação/erro/versão; reconheci um registro de problema. | Nenhuma relevante. | Frase depois do resultado. |
| 2 | Três tentativas antes/depois; entendi comparar igual. | “Variação” sem exemplo deixa dúvida se exige cálculo. | Medição se não houver mudança para comparar. |
| 3 | Gastos separados; entendi definir teto antes de ampliar. | A ficha final não traz exemplo preenchido; resposta aberta fala de integração e dados, não dos sinais. | Campos de custo que não se aplicam agora. |

Prática: possível em papel, nenhuma API necessária. Promessa de ficha: alcançável. Nota **8,5/10**. Uma melhoria: gabarito com três linhas preenchidas (abrir/cadastrar/restaurar; sinal esperado; ação se falhar) e custo atual sem integração, expansão pendente de consulta/autorização. Explicar variação apenas como maior/menor tempo das tentativas, sem exigir estatística.

## Aula 23 — professora, 55 anos

| Step | Em 5 segundos: ideia visual | Trava concreta | O que pularia |
|---|---|---|---|
| 1 | Investigar antes de apagar; ideia clara. | “Referências” pode significar fontes bibliográficas, em vez de trechos que chamam uma função. | Diagnóstico longo devolvido pelo agente. |
| 2 | Mapa de responsabilidades; entendi separar tarefas. | “Conservação/desenho” é abstrato; o resultado mostra só uma explicação, não um mapa. | Conversa sobre número de pastas. |
| 3 | Repetir testes após remover; entendi preservar funcionamento. | “Os cinco testes” sem listar/link específico exige voltar pela trilha. | Nenhum teste se souber onde está a lista. |

Prática: depende do agente analisar arquivo; isso é apropriado, mas “confira se cita funções reais” não oferece modo de conferir para iniciante. Promessa de planejar limpeza está correta. Nota **8/10**. Uma melhoria: pedir “nome da função, arquivo e trecho exato; onde é usada; teste que protegeria a mudança”; orientar abrir arquivo e buscar nome com localizar. Aceitar diagnóstico “não encontrei sobra segura” como resultado válido. Trocar referência final por exemplo desse mapa; dizer explicitamente que não precisa apagar nada.

## Aula 24 — professora, 55 anos

| Step | Em 5 segundos: ideia visual | Trava concreta | O que pularia |
|---|---|---|---|
| 1 | Sequência completa na tela; entendi demonstrar uma tarefa. | Nenhuma relevante. | Legenda se já executei o roteiro. |
| 2 | Cópia e limites; entendi provar recuperação. | “Outra janela” na prática é ambíguo: janela normal do mesmo navegador pode compartilhar os registros. | Nada: é requisito claro da entrega. |
| 3 | Editar título como mudança pequena; entendi seguir evoluindo. | Nenhuma relevante. | Nenhum passo. |

Prática: executável no computador, com alternativa de análise móvel explícita. Promessa: cumprida se registrar pendências honestamente. Nota **8,5/10**. Uma melhoria: usar “outra janela privada/anônima ou outro navegador, inicialmente sem registros” na prática, não apenas no exemplo. Incluir lembrete de fechar a janela privada após conferir; ela serve de ambiente separado, não de conservação permanente.

## Ajustes transversais

1. Os gabaritos de análise das aulas 18, 19, 21, 22 e 23 contêm frases corretas isoladas, mas algumas respondem a perguntas não exibidas junto da prática. Fazer cada um responder aos três itens locais.
2. Evitar exigir uma “pasta de treino” nos exercícios inteiramente no papel: explicitar que ela se aplica apenas quando manipular arquivos.
3. Em todos os steps, os cartões de conversa favorecem leitura, mas não substituem diagramas. As melhores oportunidades visuais são matriz real na aula 18 e um mapa nome da função → responsabilidade na 23.
4. As aulas de permissões distinguem análise de proteção real. Manter esse limite na apresentação e no portal; o laboratório não ganhou contas nem isolamento multiusuário.

Esta rodada registra pontos de ajuste, não aprovação final. As notas inferiores a 9 exigem correção antes de fechamento segundo TESTE-HUMANO.md. Releitura após correções pode verificar o desaparecimento das ambiguidades, mas nunca equivale a teste com alunos reais.

## Segunda rodada — releitura após ajustes

Data: 2026-10-05. Reabertos os HTML das aulas 18–24 e novamente inspecionadas suas sete capturas móveis atualizadas. As avaliações acima documentam a primeira versão; esta seção registra a situação final. Não houve execução de contas reais nem teste humano.

| Aula | Verificação dos ajustes | Nota final |
|---|---|---|
| 17 | Mantida a avaliação inicial: prática simples em papel, sem bloqueio para atingir a promessa. | **9/10** |
| 18 | Matriz visível por pessoa, com leitura/alteração; gabarito agora responde à matriz pedida. A parte confiável permanece abstrata, mas a regra de conferir onde os dados são entregues permite completar a análise. | **9/10** |
| 19 | Chave privilegiada explicada pelo acesso administrativo; conexão de casa/trabalho/celular esclarece origem das chamadas. Gabarito enumera os três problemas do cenário. | **9/10** |
| 20 | Abertura informa simulação; matriz está visível; referência aponta corretamente à aula 18 e ao material. Gabarito identifica a leitura indevida sem sugerir certificação de sistema real. | **9,5/10** |
| 21 | Link nomeado corretamente; janela limpa definida como privada sem sessões privadas anteriores; gabarito cobre arquivos, limites e testes. Promessa continua restrita à preparação/conferência. | **9/10** |
| 22 | Referência final fornece três sinais, ação diante de falha e campos de custo. A palavra variação poderia ter um exemplo, mas não impede a ficha de operação exigida. | **9/10** |
| 23 | Prática exige nome/trecho e explica localizar no editor. Cinco comportamentos estão nomeados, e ausência de sobra comprovada é aceita. Gabarito cita save, render e submit/taskForm. Na pausa pelo celular, a persona consegue planejar; a busca no arquivo fica para quando puder abrir o kit no editor. | **9/10** |
| 24 | Recuperação pede sessão privada de treino, eliminando ambiguidade de janela comum. Cartão visual mostra organizador e limites. Prática de computador permanece declarada. | **9/10** |

Resultado: as sete aulas inicialmente abaixo de 9 receberam ajustes que permitem atingir suas promessas didáticas. Não há bloqueio adicional de compreensão para o fechamento desta rodada. Permanecem oportunidades de acabamento, sem impedir a prática: exemplo numérico de variação (22), ilustração específica por tema e distinção explícita entre exercícios de papel e manipulação de arquivos no aviso genérico.

**Aprovação desta revisão é apenas editorial e simulada.** O laboratório continua pessoal; matrizes e acessos cruzados são análise de resultados fictícios. As notas não demonstram aprendizagem de pessoas reais e não validam proteção de produção.
