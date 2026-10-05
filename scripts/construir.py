from pathlib import Path
import sys, json, html, re, shutil, subprocess, zipfile, math
from PIL import Image, ImageDraw
from conteudo import LESSONS
import conteudo2, conteudo3
B=Path(__file__).resolve().parents[1]
SK=Path('/home/nmaldaner/.claude/skills/formato-curso-v6')
H=html.escape
assert len(LESSONS)==24
MODS=[('Uma ideia que cabe na primeira versão','Defina público, problema e critérios de pronto.'),('Da conversa para uma tela utilizável','Prepare o treino, construa e preserve uma versão.'),('Entenda como seu aplicativo funciona','Conecte tela, regras, dados e contexto do projeto.'),('Teste antes de confiar','Verifique funções, limites, correções e melhorias.'),('Prepare a passagem para outras pessoas','Entenda dados, identidade, permissões e testes de acesso.'),('Demonstre e evolua com controle','Prepare publicação, operação e uma próxima versão pequena.')]
DEFS={'agente de programação':'Programa de IA que pode ler arquivos, propor alterações e usar ferramentas no ambiente permitido.', 'critério de pronto':'Condição observável que você confere para aceitar uma entrega.', 'contexto':'Informações e materiais que ajudam o agente a entender seu pedido.', 'regressão':'Uma função que já funcionava e parou depois de uma alteração.', 'interface':'Parte do aplicativo que você vê e usa: campos, botões e mensagens.', 'armazenamento':'Lugar onde o aplicativo conserva informações para uso posterior.', 'localStorage':'Espaço do navegador que conserva pequenos registros entre visitas ao mesmo endereço.', 'autenticação':'Verificação de quem está acessando o sistema.', 'autorização':'Regra que decide o que cada pessoa pode ver ou fazer.', 'credenciais':'Informações que concedem acesso, como senhas e chaves.', 'Git':'Ferramenta que registra versões dos arquivos e ajuda a comparar mudanças.', 'GitHub':'Serviço que hospeda projetos e o histórico de seus arquivos.', 'repositório':'Conjunto de arquivos de um projeto, acompanhado de seu histórico de versões.', 'branch':'Linha de trabalho separada dentro do histórico de versões.', 'API':'Forma pela qual um programa solicita informações ou ações a outro.', 'servidor':'Computador ou programa que atende solicitações de outros programas.', 'backup':'Cópia de dados que você pode usar para recuperação.', 'variável de ambiente':'Valor fornecido ao programa pelo ambiente em que ele executa.'}
# Cada primeira aparição na aula recebe uma definição. As telas permanecem exemplos identificados.
def define_terms(body):
    for term in sorted(DEFS,key=len,reverse=True):
        parts=re.split(r'(<[^>]+>)',body);done=False;inside=False;pre=False
        for i,p in enumerate(parts):
            if p.startswith('<'):
                if p.startswith('<pre'):pre=True
                if p.startswith('</pre'):pre=False
                if 'class="gterm"' in p:inside=True
                if p=='</span>':inside=False
                continue
            if done or inside or pre:continue
            pat=re.compile(r'(?<![\w])'+re.escape(term)+r'(?![\w])',re.I)
            if pat.search(p):
                parts[i]=pat.sub(lambda m:f'<span class="gterm" data-def="{H(DEFS[term],quote=True)}">{m[0]}</span>',p,count=1);done=True
        body=''.join(parts)
    return body

def scene(n):
    # Ilustração editorial vetorial autoral, renderizada localmente; nenhum serviço de imagem.
    im=Image.new('RGB',(1280,720),'#eee7da');d=ImageDraw.Draw(im)
    palette=['#356d63','#647d9b','#b87948','#666d96','#558076','#8d6654'];accent=palette[(n-1)//4 if n else 0]
    d.rectangle((0,0,1280,480),fill='#f4f0e8');d.rectangle((0,480,1280,720),fill='#e2d9c7')
    d.rounded_rectangle((870,55,1180,360),20,fill='#d5e3df');d.line((1025,55,1025,360),fill='#f8f4eb',width=12);d.line((870,200,1180,200),fill='#f8f4eb',width=12)
    d.ellipse((890,270,1130,390),fill='#bccfc2');d.rectangle((85,80,375,265),fill='#e3dac8')
    # tableau change par groupe: cartes, liste, flux, contrôle, accès, présentation.
    module=(n-1)//4 if n else 0
    for j in range(3):
        x=110+j*82;y=110+(j%2)*12
        d.rounded_rectangle((x,y,x+60,y+95),6,fill=['#f7f3ea','#d8e5de',accent][j]);d.line((x+10,y+20,x+45,y+20),fill='#c7bdab',width=5)
    def person(x,y,skin,shirt,variant=0):
        d.rounded_rectangle((x-85,y+115,x+100,y+330),48,fill=shirt)
        d.ellipse((x-57,y-15,x+58,y+115),fill=skin)
        d.pieslice((x-65,y-30,x+60,y+90),180,350,fill='#403d39' if variant else '#605c56')
        if variant:d.ellipse((x-77,y+10,x-35,y+73),fill='#403d39')
        d.rectangle((x-12,y+94,x+21,y+135),fill=skin)
        d.line((x+32,y+157,x+147,y+254),fill=shirt,width=39)
        d.ellipse((x+118,y+224,x+165,y+266),fill=skin)
        d.line((x-43,y+160,x-135,y+247),fill=shirt,width=37)
        d.ellipse((x-157,y+226,x-113,y+269),fill=skin)
    person(455,220,'#b47d5e',accent,n%2)
    if n==0 or module in [4,5]:person(870,245,'#e0b692','#aa7659',1)
    d.rounded_rectangle((185,513,1085,548),12,fill='#bd9065');d.rectangle((225,548,248,720),fill='#997550');d.rectangle((1030,548,1052,720),fill='#997550')
    d.polygon([(470,361),(743,361),(785,511),(512,511)],fill='#323e42');d.polygon([(486,375),(730,375),(764,496),(523,496)],fill='#d5e3de')
    for j in range(3):
        d.rounded_rectangle((535,393+j*29,707,414+j*29),4,fill='#f8f6ef');d.ellipse((544,399+j*29,553,408+j*29),fill=accent)
    d.polygon([(506,511),(788,511),(819,526),(471,526)],fill='#889698')
    # Objects particularisés par leçon: livres, copie, cartes de tests, enveloppe.
    x=270+(n%4)*13
    for j in range(1+n%3):d.rounded_rectangle((x-35,488-j*14,x+65,501-j*14),3,fill=['#829b8e','#d7bd93','#a58b76'][j])
    d.rounded_rectangle((900,466,948,511),8,fill='#f8f4e9');d.arc((932,470,970,503),270,90,fill='#f8f4e9',width=8)
    if module==2:d.line((160,314,260,314,260,368,360,368),fill=accent,width=5)
    if module==3:
        for j in range(3):d.line((135,325+j*32,147,337+j*32,170,306+j*32),fill=accent,width=6)
    if module==4:d.rounded_rectangle((156,310,220,377),8,fill=accent);d.arc((164,276,211,343),180,360,fill=accent,width=8)
    if module==5:d.polygon([(145,382),(180,335),(217,350),(265,292),(265,305),(278,281),(249,291),(263,292),(215,343),(178,326),(139,378)],fill=accent)
    file=B/'assets/img'/('trilha.webp' if n==0 else f'aula-{n}.webp');im.save(file,'WEBP',quality=85)
    if n==0: im.save(B/'assets/img/trilha.png')

for n in range(25):scene(n)
for n,a in enumerate(LESSONS,1):
    module=(n-1)//4
    alt=f'Ilustração editorial de uma pessoa preparando e conferindo demandas no computador, na etapa {MODS[module][0].lower()}.'
    steps=[]
    for j,st in enumerate(a['steps'],1):
        if (n+j)%3==0 and n!=1:
            visual=f'<div class="lado"><div class="neutro"><span class="rot">Situação de treino</span><p>{H(st["request"])}</p></div><div class="bom"><span class="rot">Referência para conferir</span><p>{H(st["result"])}</p></div></div>'
        else:
            cases=f'<div class="tela-body"><p class="msg eu"><span class="quem">Pedido ou ação</span>{H(st["request"])}</p><p class="msg ia"><span class="quem">Resposta ilustrativa / resultado esperado</span>{H(st["result"])}</p></div>'
            if n==1 and j==1:
                cases='<div class="tela-caso" data-rotulo="Pedido vago"><div class="tela-body"><p class="msg eu"><span class="quem">Você</span>Faça um aplicativo bom.</p><p class="msg ia"><span class="quem">Dúvida que permanece</span>Qual tarefa? Para quem? Como conferir?</p></div></div><div class="tela-caso" data-rotulo="Pedido delimitado">'+cases+'</div>'
            visual=f'<div class="tela"><div class="tela-top"><i></i><i></i><i></i><span>Exemplo didático</span></div>{cases}</div>'
        if n in [6,7,11,13,14,15,24] and j==2:
            visual='<div class="janela"><div class="tela-top"><i></i><i></i><i></i><span>Organizador · exemplo visual</span></div><div class="janela-body"><div class="item"><b>Demanda de treino</b></div><div class="item">Prazo: sem prazo</div><div class="item">Situação: Pendente</div><div class="item botao">Concluir</div></div></div><p>'+H(st['request'])+'</p><p><b>O que conferir:</b> '+H(st['result'])+'</p>'
        if n==9 and j==3:
            visual='<div class="janela"><div class="tela-top"><span>Caminho de uma demanda</span></div><div class="janela-body"><div class="item"><span class="pin">1</span> Tela: você digita Preparar atividade</div><div class="item"><span class="pin">2</span> Regra: rejeitar texto vazio e criar registro</div><div class="item"><span class="pin">3</span> Armazenamento: conservar registro neste navegador</div></div></div>'
        if n in [18,20] and j==2:
            visual='<div class="janela"><div class="tela-top"><span>Matriz de acesso · registro da conta A</span></div><div class="janela-body"><div class="item"><b>Conta A</b> · ler: permitido · alterar: permitido</div><div class="item"><b>Conta B</b> · ler: negado · alterar: negado</div><div class="item"><b>Visitante</b> · ler: negado · alterar: negado</div></div></div>'
        extra=''
        if j==3:
            q,*opts=a['quiz']
            feedback=['Essa escolha não verifica a condição importante deste caso.','Correto. Esta opção aplica o critério apresentado na aula.','Essa escolha deixa o problema principal sem verificação.']
            extra=f'<div class="quiz" data-answer="b"><p class="qk">Teste-se</p><p class="q">{H(q)}</p>'+''.join(f'<button class="opt" data-k="{k}" data-fb="{fb}">{H(opt)}</button>' for k,opt,fb in zip('abc',opts,feedback))+'<p class="qfb" aria-live="polite"></p></div>'+f'<div class="calma"><p><span class="k">Se travou aqui, é normal</span>{H(a["tip"])}</p></div>'
            # Alterne a posição da resposta correta sem trocar seu vínculo com o feedback.
            buttons=re.findall(r'<button class="opt".*?</button>',extra)
            rotated=buttons[n%3:]+buttons[:n%3]
            extra=re.sub(r'(?:<button class="opt".*?</button>){3}',lambda _:''.join(rotated),extra)
        steps.append(f'<section class="step" data-kind="fundamento"><h2><span class="n">{j}</span>{H(st["title"])}</h2><p>{H(st["text"])}</p><p data-ex="{H(st["profession"])}">{H(st["example"])}</p><figure class="largo">{visual}<figcaption>{H(st["caption"])}</figcaption></figure>{extra}</section>')
    links='<p><a href="pratica/index.html" target="_blank" rel="noopener">Abrir o aplicativo de treino</a> · <a href="materiais/kit-organizador.zip" download>Baixar o kit editável</a> · <a href="materiais/folha-de-testes.html" target="_blank" rel="noopener">Folha de testes e matriz de acesso</a></p>'
    if n==14:links+='<p><a href="materiais/invalido.txt" download>Baixar arquivo inválido para o teste</a></p>'
    mode='analise' if n in [2,3,4,9,10,16,17,18,19,20,21,22,23] else 'tarefa'
    pgoal='Cerca de 10 minutos, no computador. No celular, faça a análise nas notas e retome a edição depois.'
    if mode=='analise':pgoal='Cerca de 8 minutos. Anote suas respostas no papel ou nas notas do celular.'
    minutes=15 if mode!='analise' else 13
    nexttitle=LESSONS[n]['title'] if n<24 else 'Escolha uma nova demanda e repita o ciclo com os mesmos cuidados.'
    complement=f'<details class="complementar"><summary>Material complementar<small>Aprofundamento opcional, fora do tempo da aula.</small></summary><section class="comp-sec"><h3>Para ampliar o raciocínio</h3><p>{H(a["extra"])}</p></section></details>' if a['extra'] else ''
    modelanswer=f'<details class="gabarito"><summary>Conferir a referência da análise</summary><p>{H(a["steps"][-1]["result"])}</p><p>{H(a["cards"][0][1])}</p></details>' if mode=='analise' else ''
    answers={
      2:'Degrau atual: uso pessoal com dados fictícios. Risco: perder registros. Antes de convidar alguém, decidir o que será compartilhado e como limitar o acesso.',
      3:'Usuário: uma pessoa. Funções: cadastrar, listar e concluir. Exclusões: contas, mensagens, pagamentos e integrações. Teste: criar uma demanda, vê-la na lista e concluí-la.',
      4:'O pedido precisa rejeitar título vazio, conservar registros após atualizar e mostrar a mudança de situação. Confirme onde os dados ficarão antes de construir.',
      9:'Fluxo: campo Título recebe o texto; regra verifica e cria a demanda; armazenamento conserva. Se aparecer e sumir após atualizar, investigue a gravação e a leitura dos registros.',
      10:'Para um usuário sem compartilhamento, a solução local atende ao treino. A solução compartilhada exige permissões e operação. Reconsidere quando precisar sincronizar ou colaborar.',
      16:'Exemplo: contar ações para encontrar pendentes. Proteção: prazos e registros continuam intactos. Parada: duas tentativas, qualquer regressão ou ausência de melhora observada.',
      17:'Mantenha título, prazo opcional e situação. Retire nome completo, telefone e documento. Exemplos: preparar atividade de treino; conferir ferramenta fictícia. Revise o entorno de qualquer captura.',
      18:'Visitante: nenhuma leitura ou alteração. Responsável: lê e altera o próprio registro. Outra pessoa: não lê nem altera aquele registro. Confira a tabela no material de apoio.',
      19:'Senha na página: fica acessível ao visitante. Botão escondido: não bloqueia uma solicitação direta. Ausência de autorização: permite operações indevidas. Exigir proteção de credenciais e testar recusa de leitura e alteração.',
      20:'Reprovado: B leu o registro de A. Os outros três resultados correspondem às regras. Bloquear edição não impede o vazamento por leitura. São dados simulados, não testes de um sistema real.',
      21:'Publicar apenas os arquivos da demonstração; excluir credenciais e cópias privadas. Informar dados locais e ausência de colaboração. No endereço publicado, conferir abertura, cadastro, filtro, conservação e recuperação.',
      22:'Sinais: página abre, cadastro permanece, cópia restaura. Se falhar, registrar ação, mensagem e versão sem dados pessoais. Antes de ampliar, conferir hospedagem, armazenamento e serviços, com limite mensal e responsável.',
      23:'No kit fornecido, save grava e render monta a lista. O cadastro está no evento submit de taskForm. Antes de remover algo, localizar quem o utiliza, copiar arquivos e repetir os testes. Não é necessário encontrar uma sobra se nenhuma for comprovada.'}
    if mode=='analise':
        modelanswer='<details class="gabarito"><summary>Conferir a referência da análise</summary><p>'+H(answers[n])+'</p></details>'
    safe='Use somente dados fictícios e uma pasta de treino. Se o resultado divergir, preserve a cópia e registre o erro antes de continuar.'
    body=f'''<section class="view" id="v-aula-{n}" data-aula="{n}" data-tempo="{minutes}min"><div class="aula">
+<header class="a-hero"><p class="kicker">Aula {n} de 24 · Da Ideia ao App v6</p><h1>{H(a['title'])}</h1><figure class="cena"><img src="assets/img/aula-{n}.webp" width="1280" height="720" alt="{H(alt)}"></figure><p class="promise">Você consegue {H(a['promise'])}</p><p class="why">{H(a['why'])}</p><div class="em1min"><p class="k">Em 1 minuto</p><ol>{''.join('<li>'+H(x)+'</li>' for x in a['summary'])}</ol></div></header>
+{''.join(steps)}
+<section class="practice" data-mode="{mode}"><p class="pk">Pratique agora <span class="pcount">0/3</span></p><h3 class="ph">{H(a['title'])}: seu exercício</h3><p class="pgoal">{pgoal} Pronto quando os três passos abaixo estiverem conferidos.</p><p class="psafe">{safe}</p>{links}<div class="pcodewrap"><button class="pcopy" type="button">copiar</button><pre class="pcode">{H(a['prompt'])}</pre></div><ol class="psteps">{''.join(f'<li><label><input type="checkbox" data-ptask="{i}"> <span>{H(t)}</span></label></li>' for i,t in enumerate(a['checks'],1))}</ol>{modelanswer}<p class="pdone">Ao concluir os passos, você consegue {H(a['promise'])}</p></section>
+<div class="fecho"><div class="cola"><p class="k">Cola da aula</p><h3>O que levar para seu projeto</h3><ol>{''.join('<li><span>'+H(x)+'</span></li>' for x in a['summary'])}</ol></div><div class="next-action"><p class="nak">Seu próximo passo</p><p class="na-win">Você praticou como {H(a['promise'])}</p><p class="na-action">Guarde nas notas o resultado do exercício e uma dúvida que ainda precisa verificar.</p><p class="na-hook">Próxima etapa: {H(nexttitle)}</p></div></div>{complement}<nav class="lnav"><a href="#trilha">← trilha</a><a class="next" href="{'#aula-'+str(n+1) if n<24 else '#trilha'}">{'próxima aula →' if n<24 else 'voltar à trilha →'}</a></nav><p class="aula-pe">Aula {n} · Da Ideia ao App v6 · INEMA.CLUB · Curso aberto e gratuito</p></div><script type="application/json" id="cards-{n}">{json.dumps([{'front':q,'back':r} for q,r in a['cards']],ensure_ascii=False)}</script></section>'''.replace('\n+','\n')
    prose, cards_script = body.split('<script type="application/json"', 1)
    body=define_terms(prose)+'<script type="application/json"'+cards_script
    (B/'aulas'/f'aula-{n}.html').write_text(body)
mods=[dict(titulo=f'{i+1}. {m[0]}',resumo=m[1],aulas=list(range(i*4+1,i*4+5))) for i,m in enumerate(MODS)]
cfg=dict(id='inema-da-ideia-ao-app-v6',titulo='Da Ideia ao App v6 — Desenvolva com IA, passo a passo',titulo_html='Da ideia ao <em>app</em> <small>v6</small>',curso_curto='Da Ideia ao App v6',kicker='Da Ideia ao App v6 · Desenvolvimento com IA',lead='Aprenda a orientar a IA, construir uma aplicação pessoal e conferir o resultado. 24 aulas, um organizador de demandas e práticas com dados fictícios.',rodape='Da Ideia ao App v6 · INEMA.CLUB · Curso aberto e gratuito',landing='index.html',imagem_trilha='assets/img/trilha.webp',alt_trilha='Duas pessoas conferem uma lista de demandas no computador, com anotações e materiais de trabalho na mesa.',perfil='tecnico',glossario=True,modulos=mods)
(B/'curso.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2))
landing=(SK/'assets/landing-template.html').read_text()
replacements={'[Nome do curso]':cfg['titulo'],'[1 frase: o que a pessoa sai fazendo]':'Aprenda a orientar a IA, criar um aplicativo pessoal, testar resultados e preparar uma demonstração com limites claros.','[Nome curto]':cfg['curso_curto'],'[Categoria — ex.: IA no seu trabalho]':'Da Ideia ao App v6 · Curso aberto e gratuito','[Promessa em <em>poucas palavras</em>]':'Sua ideia.<br>Um app que você<br><em>sabe conferir.</em>','[O que a pessoa sai fazendo, em 1–2 frases. Sem vídeo, no seu tempo.]':'A IA escreve o código. Você aprende a conduzir o projeto, testar o resultado e decidir o próximo passo. Um organizador de demandas acompanha as 24 aulas.','[N] aulas de ~15 minutos · sem instalar nada · funciona no celular e no computador':'24 aulas · cerca de 6 horas · leitura no celular · práticas de edição no computador','[alt da trilha]':cfg['alt_trilha'],'[Resultado 1]':'Orientar a construção','[em uma linha, concreto]':'Transformar uma necessidade em funções pequenas e critérios verificáveis.','[Resultado 2]':'Testar o que foi entregue','[Resultado 3]':'Evoluir com controle','[profissão-alvo 1] e quer [resultado].':'É professor ou prestador de serviço e quer organizar uma tarefa recorrente.'}
for k,v in replacements.items():landing=landing.replace(k,v)
landing=landing.replace('[…]','Conferir funções, recuperar cópias e registrar os limites antes de ampliar o uso.',1).replace('[…]','Preservar versões, entender dados e preparar uma demonstração.',1)
landing=landing.replace('Já domina o assunto e busca algo técnico.','Busca formação avançada em engenharia ou certificação de segurança.').replace('Quer videoaula tradicional.','Precisa de um sistema multiusuário pronto para produção.')
landing=landing.replace('<div class="aulas">\n<!--AULAS-->','<div>\n<!--AULAS-->')
landing=landing.replace('<h2>As aulas</h2>','<h2>Seis etapas, uma construção</h2><p>Cada aula traz exemplos visuais, uma prática, uma referência para conferir e cartões de revisão.</p>')
landing=landing.replace('</main>','''<section class="l-sec"><h2>Comece com uma referência utilizável</h2><p>O laboratório funciona no navegador, com dados locais e fictícios. Ele não oferece contas ou colaboração. Você pode usá-lo antes de configurar um agente.</p><p><a class="big" href="pratica/index.html">abrir o organizador de treino →</a></p><p><a href="materiais/kit-organizador.zip" download>Baixar o kit editável</a> · <a href="materiais/folha-de-testes.html">Folha de testes</a></p></section><section class="l-sec"><h2>O que você precisa</h2><p>Um navegador para estudar e experimentar. Para editar o projeto com IA, use seu ambiente de programação já contratado. Assinaturas de ferramentas não estão incluídas. A configuração inicial e os aprofundamentos podem exigir tempo adicional.</p><p>As conversas ilustradas são exemplos didáticos. As expectativas de teste devem ser comparadas com o que você observar. O curso se inspira na entrevista fornecida sobre desenvolvimento com IA; as aulas e os exercícios são autorais.</p></section></main>''')
publication=B/'context/publicacao.json'
if publication.exists():
    pub=json.loads(publication.read_text())
    landing=landing.replace('</head>',f'<link rel="canonical" href="{pub["url"]}"><meta property="og:title" content="{H(cfg["titulo"],quote=True)}"><meta property="og:description" content="Aprenda a orientar a IA, construir e conferir seu aplicativo pessoal."><meta property="og:image" content="{pub["url"]}capa/capa.png"></head>')
    landing=re.sub(r'<!-- inema-backlink:v1.*?<!-- /inema-backlink:v1 -->',f'<!-- inema-backlink:v1 --><p><a href="{pub["ficha"]}">Ficha completa deste curso no INEMA.CLUB</a> · <a href="https://www.inema.club/aprender-inteligencia-artificial/">Guia: como aprender inteligência artificial</a></p><!-- /inema-backlink:v1 -->',landing,flags=re.S)
(B/'index.html').write_text(landing)
(B/'landing.html').write_text('<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=index.html"><title>Da Ideia ao App v6</title><a href="index.html">Abrir o curso</a></html>')
subprocess.run([sys.executable,str(SK/'scripts/montar-curso.py'),str(B)],check=True)
# Kit autônomo: nenhum segredo, registro pessoal ou dependência externa.
readme='MEU ORGANIZADOR — TREINO\n\n1. Extraia o arquivo compactado.\n2. Abra index.html no navegador.\n3. Use somente demandas fictícias.\n4. Exporte uma cópia dos registros antes de experimentar.\n5. A conservação em arquivo local depende do navegador. Prefira a demonstração publicada para comparar.\n6. Para editar, abra esta pasta no seu agente de programação.\n\nNão há contas, compartilhamento ou segurança multiusuário. O arquivo exportado é separado do código.\n'
ficha='Objetivo: organizar demandas pessoais fictícias.\nFunções: cadastrar, filtrar, concluir, exportar e importar.\nLimites: dados locais; sem colaboração; sem credenciais.\nEstado observado: preencher depois de testar.\nTestes realizados: preencher.\nPróxima ação: preencher.\n'
app=(B/'pratica/index.html').read_text().replace('../curso.html#aula-5','https://inematds.github.io/da-ideia-ao-app-v6/curso.html#aula-5').replace('../materiais/kit-organizador.zip','https://inematds.github.io/da-ideia-ao-app-v6/materiais/kit-organizador.zip')
with zipfile.ZipFile(B/'materiais/kit-organizador.zip','w',zipfile.ZIP_DEFLATED) as z:
    z.writestr('meu-organizador/index.html',app);z.writestr('meu-organizador/LEIA-ME.txt',readme);z.writestr('meu-organizador/ficha-projeto.txt',ficha)
(B/'materiais/invalido.txt').write_text('Este arquivo não é uma cópia válida de demandas. O aplicativo deve recusá-lo e preservar os registros.\n')
(B/'materiais/copia-exemplo.json').write_text(json.dumps({'version':1,'tasks':[{'id':'treino-a','title':'Preparar atividade fictícia','due':'','done':False},{'id':'treino-b','title':'Conferir ferramenta de treino','due':'','done':True}]},ensure_ascii=False,indent=2))
(B/'.nojekyll').touch()
(B/'context/curriculo.md').write_text('# Currículo — Da Ideia ao App v6\n\nPúblico editorial adotado após o pedido de execução: iniciantes adultos; professores e pequenos prestadores de serviço. Familiaridade: navegador, arquivos e chat de IA; programação não presumida. Sessões de 13–15 minutos. Resultado: conduzir, testar e demonstrar um aplicativo pessoal. Projeto: organizador de demandas. Estas escolhas são premissas editoriais explícitas, não respostas atribuídas ao usuário.\n\nFormato v6 com perfil técnico introdutório e glossário. 24 aulas, 6 módulos. Principal em português; traduções não solicitadas.\n\n'+''.join(f'## {i}. {a["title"]}\nPromessa: {a["promise"]}\nTipo: fundamento com prática. Gancho: {LESSONS[i]["title"] if i<24 else "Próxima versão delimitada"}.\n\n' for i,a in enumerate(LESSONS,1)))
print('24 aulas, landing, 25 ilustrações locais e kit gerados.')
