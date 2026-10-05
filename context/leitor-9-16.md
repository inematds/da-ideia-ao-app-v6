# Revisão de leitor simulado — aulas 9–16

Data: 2026-10-05. **Simulação por agente, não teste com pessoas reais.** Persona: Rafael, 34 anos, prestador de manutenção, usa navegador e chat, nunca programou; leitura no celular em intervalo de 15 minutos.

Evidência: texto integral dos HTML e capturas `verificacao/capturas/aula-{9..16}-celular-papel.png`, inspecionadas com ferramenta de imagem. Blocos de revisão: 9–11, 12–14, 15–16. Não houve execução das práticas nesta revisão; executabilidade é avaliação de leitura, não comprovação funcional.

## Observação visual comum

Os cartões de pedido e resultado mostram conteúdo didático, mas são predominantemente texto. A ilustração de abertura se repete e não explica a função específica. A coluna e os contrastes na captura são consistentes; não vi sobreposição. Para o teste de 5 segundos, o título do step e o trecho destacado permitem identificar a ideia; a operação exata ainda depende de leitura. Um pequeno diagrama na aula 9 e uma tabela preenchida na 13 ensinariam mais rapidamente que cartões de texto.

## Bloco 9–11

| Aula / step | Ideia percebida em 5 segundos | Onde Rafael trava | O que pularia |
|---|---|---|---|
| 9 / 1 | Campo vazio precisa de aviso; corresponde ao objetivo. | “Serviços compartilhados” surge antes de exemplo concreto. Pode ser explicado como sistema usado por várias pessoas. | Frase sobre proteção nesta etapa, se permanecer abstrata. |
| 9 / 2 | Concluir muda a situação e mantém título; correto. | “Parte confiável” não diz quem verifica. Acrescentar “o servidor, que confere a permissão fora do navegador”. | Repetição de que regra difere da aparência do botão. |
| 9 / 3 | Lista do computador não aparece automaticamente no celular; correto. | Nenhuma trava relevante no step. | Segunda formulação da ausência de compartilhamento, se estiver com pressa. |
| 10 / 1 | Escolher o que atende ao uso individual; correto. | “Conservação e cópia” fica pouco concreto: dizer salvar e exportar uma cópia. | A pergunta sobre recursos do dispositivo sem exemplo. |
| 10 / 2 | Local separa listas; compartilhado reúne listas; correto. | “Operação” é vago: manutenção do serviço, por exemplo. | Nenhum trecho imprescindível. |
| 10 / 3 | Registrar escolha e quando rever; correto. | Nenhuma trava relevante. | Repetição de que não precisa mudar semanalmente. |
| 11 / 1 | Atualizar a página e conferir se ficou salvo; correto. | Nenhuma, localStorage é explicado no texto. | Nome técnico após entender o conceito. |
| 11 / 2 | Janela privada começa com outra lista; correto. | Não ensina a abrir janela privada, mas isso não bloqueia a prática obrigatória. | Comparação adicional se não conseguir abrir a janela. |
| 11 / 3 | Falhou em salvar, deve avisar; correto. | “Exporte” deve apontar o botão visível “Exportar cópia” (ou rótulo exato do app). | Discussão de recusa do navegador se não houver forma de simular. |

- **Aula 9:** prática executável com papel e aplicativo. Promessa parcialmente atendida: aluno pode desenhar o fluxo, mas a referência da análise responde sobre sincronização, não sobre a falha após atualizar. A última frase “Não. Uma recebe ações; o outro conserva informações” parece resposta a pergunta ausente. **Nota inicial 8/10.** Uma mudança: substituir a referência por três partes nomeadas e a investigação de gravação/armazenamento quando o registro some.
- **Aula 10:** prática executável nas notas; comparação e decisão são claras. Promessa atendida. **Nota inicial 9/10.** Uma melhoria: referência deve mostrar uma decisão completa e sua condição de revisão, removendo a resposta isolada “Quando o uso exigir...”.
- **Aula 11:** prática executável no computador; alternativa móvel explicitada. Promessa atendida. **Nota inicial 9/10.** Uma melhoria: escrever a ação exata de exportação e pedir para conferir onde o arquivo foi baixado; “saiba onde está sua cópia” merece essa evidência.

## Bloco 12–14

| Aula / step | Ideia percebida em 5 segundos | Onde Rafael trava | O que pularia |
|---|---|---|---|
| 12 / 1 | Registrar o que existe e o que não existe; correto. | Nenhuma trava relevante. | Lista de arquivos se trabalhar só pelo navegador. |
| 12 / 2 | Digitar sinais deve mostrá-los como texto; correto. | “Marcação” é técnico, mas o exemplo literal explica. | Primeira formulação abstrata depois de ler o exemplo. |
| 12 / 3 | Anotar testes e próxima tarefa; correto. | “Janela separada” pode significar outra aba, que usa o mesmo armazenamento. Deve especificar janela privada/perfil separado para testar recuperação sem substituir a lista original. | Nenhum. |
| 13 / 1 | Um cadastro precisa produzir uma demanda pendente; correto. | Nenhuma. | Nenhum. |
| 13 / 2 | Espaços não são título válido; correto. | Nenhuma. | Definição “teste negativo”, se precisar correr. |
| 13 / 3 | Comparar o previsto com o que aconteceu; correto. | Cartão descreve colunas, mas não mostra uma linha preenchida. | Frase “documento de intenção” é dispensável. |
| 14 / 1 | Título vazio/longuíssimo precisa ser tratado; correto. | Como conseguir texto >120 sem contar? Fornecer texto pronto copiável ou explicar que repetir frase basta. | Nenhum. |
| 14 / 2 | Arquivo inválido deve ser recusado sem apagar lista; correto. | Material está depois do step, mas o link na prática permite executar. | Nenhum. |
| 14 / 3 | Filtro vazio não significa lista apagada; correto. | Abertura fala de cliques repetidos, mas visual só demonstra filtro. Não é bloqueador, porém gera expectativa sem exemplo. | Frase sobre repetição se não houver caso correspondente. |

- **Aula 12:** prática de ficha executável; promessa atendida, com ressalva sobre recuperação no exemplo. **Nota inicial 8/10.** Uma mudança: substituir “janela separada” por “janela privada, com lista vazia, mantendo a janela original aberta”, explicando que outra aba comum pode compartilhar os mesmos dados.
- **Aula 13:** links e passos permitem executar; cinco casos cabem no exercício. Promessa atendida. **Nota inicial 9/10.** Uma melhoria: colocar uma linha visual com preparação, ação, esperado e observado, explicitando que o observado do aluno fica vazio até o teste.
- **Aula 14:** prática é viável com kit, mas “execute os três tipos de limite” deixa a seleção ao aluno enquanto o prompt lista cinco casos. **Nota inicial 8/10.** Uma mudança: enumerar os casos na checklist (“espaços, título longo, filtro sem resultados e arquivo inválido”) e oferecer uma cadeia longa copiável. A promessa fica atendida após isso.

## Bloco 15–16

| Aula / step | Ideia percebida em 5 segundos | Onde Rafael trava | O que pularia |
|---|---|---|---|
| 15 / 1 | Relatar sequência, expectativa e resultado; correto. | Nenhuma. | Nenhum. |
| 15 / 2 | Investigar gravação antes de refazer aplicativo; correto. | “Hipótese” explicável como suspeita a testar; contexto é suficiente. | Nenhum. |
| 15 / 3 | Repetir defeito e testar função próxima; correto. | “Regressões” aparece sem definição imediata. Acrescentar “algo que funcionava e parou depois da mudança”. | Nenhum. |
| 16 / 1 | Contar ações antes da mudança; correto. | Nenhuma. | Nenhum. |
| 16 / 2 | Melhorar aparência preservando dados; correto. | “Casos separados” poderia receber exemplo de entrada nova, fora dos casos usados para ajustar. | Frase final repete a proteção. |
| 16 / 3 | Limitar tentativas e parar se piorar; correto. | “Prova independente absoluta” aumenta abstração sem ajudar o exercício inicial. | Ressalva sobre outro modelo; cabe no complemento. |

- **Aula 15:** prática explicitamente simulada pode ser feita sem encontrar defeito real. Promessa de relato é atendida, mas “evidência” não deve ser confundida com o observado inventado do caso. **Nota inicial 8/10.** Uma mudança: pedir no passo obrigatório “Se usar o caso didático, escreva SIMULAÇÃO; não apresente o resultado como observado no seu app”. Definir regressão na primeira ocorrência.
- **Aula 16:** prática de definir medida, proteção e parada é executável no celular e atende à promessa. **Nota inicial 9/10.** Uma melhoria: referência mostrar plano completo (contagem inicial a medir, cadastro e prazos protegidos, duas tentativas, parar se piorar). A frase “Faltam uma medida verificável e uma regra de parada” responde a pergunta ausente e deve sair.

## Ajustes prioritários enviados ao responsável

1. Trocar referências soltas das aulas 9, 10 e 16 por respostas ligadas à prática.
2. Especificar isolamento real na recuperação da aula 12.
3. Tornar a lista de limites da aula 14 inequívoca e fornecer texto longo.
4. Rotular a evidência simulada da aula 15 e explicar regressão.
5. Aplicar pequenos esclarecimentos por step acima; não são testes funcionais nem auditoria de segurança.

Notas <9 pedem ajuste antes da aprovação da rodada. Este relatório registra a primeira leitura e não afirma que correções já foram feitas.

## Reinspeção após correções — notas finais

Releitura dos HTML e das quatro capturas móveis atualizadas das aulas inicialmente abaixo de 9, em 2026-10-05. Continua sendo revisão simulada, sem alegação de execução funcional das práticas.

| Aula | Evidência da correção conferida | Nota final |
|---|---|---|
| 9 | Visual agora mostra Tela → Regra → Armazenamento; referência explica investigar gravação/leitura se o registro some após atualizar, alinhada à prática. | 9/10 |
| 12 | Exemplo agora manda importar numa **janela privada de treino**, eliminando a ambiguidade de outra aba que compartilha registros. | 9/10 |
| 14 | Texto longo pronto fornecido; checklist enumera espaços, título longo, filtro Concluídas e arquivo inválido; visual mostra o registro a preservar. | 9/10 |
| 15 | Checklist exige rotular o observado didático como **simulado** e não afirmar execução. A linguagem distingue hipótese, teste e evidência. | 9/10 |

As quatro práticas ficaram compreensíveis para Rafael sem as ambiguidades apontadas. Aulas 10, 11, 13 e 16 já tinham nota 9/10 na leitura inicial. Notas finais desta faixa: **9/10 em todas as oito aulas**. As sugestões de enriquecimento visual/explicações curtas permanecem opcionais e não representam bloqueio de compreensão das práticas. O termo regressão possui apoio de glossário no curso, conforme confirmado pelo responsável; não exige repetir a definição no corpo de todos os steps.
