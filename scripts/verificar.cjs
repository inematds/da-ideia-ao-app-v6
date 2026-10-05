const fs=require('fs'),path=require('path'),http=require('http'),assert=require('assert/strict');
const {chromium}=require('/home/nmaldaner/projetos/agent-browser/node_modules/playwright');
const ROOT=path.resolve(__dirname,'..'),OUT=path.join(ROOT,'verificacao'),CAP=path.join(OUT,'capturas');fs.mkdirSync(CAP,{recursive:true});
const types={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.webp':'image/webp','.json':'application/json','.zip':'application/zip','.txt':'text/plain; charset=utf-8'};
const server=http.createServer((req,res)=>{let rel=decodeURIComponent(req.url.split('?')[0]);if(rel.endsWith('/'))rel+='index.html';const file=path.resolve(ROOT,'.'+rel);if(!file.startsWith(ROOT+path.sep)){res.writeHead(403).end();return}fs.readFile(file,(err,data)=>{if(err){res.writeHead(404).end();return}res.setHeader('Content-Type',types[path.extname(file)]||'application/octet-stream');res.end(data)})});
(async()=>{await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));const url='http://127.0.0.1:'+server.address().port;const browser=await chromium.launch({args:['--disable-gpu']});const results=[],errors=[];const check=(name,condition)=>{assert.ok(condition,name);results.push(name)};
try{
const ctx=await browser.newContext({viewport:{width:1280,height:900},reducedMotion:'reduce'});const page=await ctx.newPage();page.on('pageerror',e=>errors.push(e.message));
await page.goto(url+'/pratica/');
await page.locator('#title').fill('   ');await page.locator('button[type=submit]').click();check('título vazio recusado',await page.locator('.item').count()===0&&await page.locator('#status').getAttribute('data-error')==='true');
await page.locator('#title').fill('<b>Atividade</b>');await page.locator('#due').fill('2026-10-20');await page.locator('button[type=submit]').click();check('texto tratado literalmente',await page.locator('.item h3').textContent()==='<b>Atividade</b>'&&await page.locator('.item h3 b').count()===0);
await page.locator('#title').fill('Preparar material');await page.locator('button[type=submit]').click();check('cadastro adiciona dois registros',await page.locator('.item').count()===2);
await page.locator('.item button').first().click();await page.locator('#filter').selectOption('pending');check('filtro exclui concluída',await page.locator('.item').count()===1);await page.reload();check('conservação após atualizar',await page.locator('.item').count()===2&&(await page.locator('.item .meta').first().textContent()).includes('Concluída'));
await page.locator('#search').fill('material');check('busca por título',await page.locator('.item').count()===1);await page.locator('#search').fill('');
const [download]=await Promise.all([page.waitForEvent('download'),page.locator('#exportBtn').click()]);const saved=path.join(OUT,'copia-teste.json');await download.saveAs(saved);const exported=JSON.parse(fs.readFileSync(saved));check('exportação contém dois registros',exported.tasks.length===2);
await page.locator('#importFile').setInputFiles(path.join(ROOT,'materiais/invalido.txt'));await page.waitForFunction(()=>document.getElementById('importFile').value==='');check('cópia inválida não apaga registros',await page.locator('.item').count()===2&&(await page.locator('#status').textContent()).includes('inválido'));
page.once('dialog',d=>d.dismiss());await page.locator('#importFile').setInputFiles(path.join(ROOT,'materiais/copia-exemplo.json'));await page.waitForFunction(()=>document.getElementById('importFile').value==='');check('cancelamento preserva registros',(await page.locator('.item h3').first().textContent())==='<b>Atividade</b>');
const restoreCtx=await browser.newContext();const restored=await restoreCtx.newPage();await restored.goto(url+'/pratica/');restored.once('dialog',d=>d.accept());await restored.locator('#importFile').setInputFiles(saved);await restored.waitForFunction(()=>document.querySelectorAll('.item').length===2);check('recuperação em contexto separado',await restored.locator('.item h3').first().textContent()==='<b>Atividade</b>');await restoreCtx.close();
await page.evaluate(()=>{window.originalSet=Storage.prototype.setItem;Storage.prototype.setItem=function(){throw new DOMException('blocked','QuotaExceededError')}});await page.locator('#title').fill('Não deve entrar');await page.locator('button[type=submit]').click();check('falha de gravação não informa sucesso',await page.locator('.item').count()===2&&(await page.locator('#status').textContent()).includes('Não foi possível salvar'));await page.evaluate(()=>{Storage.prototype.setItem=window.originalSet});
const bad=JSON.stringify({version:1,tasks:[{id:'x',title:'X',due:'2026-02-31',done:false}]});await page.locator('#importFile').setInputFiles({name:'invalid-date.json',mimeType:'application/json',buffer:Buffer.from(bad)});await page.waitForFunction(()=>document.getElementById('importFile').value==='');check('data inválida na cópia recusada',(await page.locator('#status').textContent()).includes('inválido')&&await page.locator('.item').count()===2);
await page.locator('#importFile').setInputFiles({name:'large.json',mimeType:'application/json',buffer:Buffer.alloc(1024*1024+1,32)});await page.waitForFunction(()=>document.getElementById('importFile').value==='');check('arquivo acima de 1 MB recusado',(await page.locator('#status').textContent()).includes('inválido'));
await page.screenshot({path:path.join(CAP,'aplicativo-desktop.png'),fullPage:true});
await page.goto(url+'/curso.html#trilha');await page.waitForTimeout(200);check('24 aulas e seis módulos',await page.locator('.view[data-aula]').count()===24&&await page.locator('#v-trilha .modulo').count()===6);
const links=await page.locator('a[href]').evaluateAll(as=>[...new Set(as.map(a=>a.getAttribute('href')).filter(x=>x&&!x.startsWith('#')&&!/^(https?:|mailto:)/.test(x)))]);
for(const link of links){const pathname=link.split('#')[0];check('link local '+pathname,fs.existsSync(path.join(ROOT,pathname)))}
const brokenImgs=await page.locator('img').evaluateAll(imgs=>imgs.filter(x=>!x.complete||x.naturalWidth===0).map(x=>x.src));check('todas as imagens carregam',brokenImgs.length===0);
const notes=[];
for(const [width,label] of [[390,'celular'],[1280,'desktop']]){
 await page.setViewportSize({width,height:900});
 for(const theme of ['papel','escuro','sepia']){
  await page.evaluate(t=>document.documentElement.dataset.theme=t,theme);
  for(let n=1;n<=24;n++){
   await page.evaluate(n=>location.hash='aula-'+n,n);await page.waitForTimeout(40);
   const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1);check(`sem overflow ${label} ${theme} aula ${n}`,!overflow);
   if(theme==='papel'||n%4===1)await page.screenshot({path:path.join(CAP,`aula-${n}-${label}-${theme}.png`),fullPage:true});
  }
 }
}
await page.setViewportSize({width:390,height:844});await page.goto(url+'/index.html');await page.screenshot({path:path.join(CAP,'landing-celular.png'),fullPage:true});await page.setViewportSize({width:1280,height:900});await page.screenshot({path:path.join(CAP,'landing-desktop.png'),fullPage:true});
check('zero erro JavaScript',errors.length===0);fs.writeFileSync(path.join(OUT,'funcional.json'),JSON.stringify({passed:results.length,checks:results,errors,date:new Date().toISOString()},null,2));console.log(`${results.length} verificações passaram; zero erro JavaScript. Capturas em verificacao/capturas.`);
}finally{await browser.close();server.close()}
})().catch(e=>{console.error(e);server.close();process.exitCode=1});
