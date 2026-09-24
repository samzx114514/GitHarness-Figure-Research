const {chromium}=require('C:/Users/25779/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs');const path=require('path');
(async()=>{const browser=await chromium.launch({channel:'msedge',headless:true});
const page=await browser.newPage({viewport:{width:1200,height:720},deviceScaleFactor:1});
for(const f of fs.readdirSync(__dirname).filter(n=>n.endsWith('.svg'))){
 await page.setContent('<html><body style="margin:0">'+fs.readFileSync(path.join(__dirname,f),'utf8')+'</body></html>');
 await page.screenshot({path:path.join(__dirname,f.replace('.svg','.png'))});
 const overflow=await page.locator('svg text').evaluateAll(ns=>ns.filter(n=>{let b=n.getBBox();return b.x<0||b.y<0||b.x+b.width>1200||b.y+b.height>720}).map(n=>n.textContent));
 console.log(f,JSON.stringify({overflow}));
}
await browser.close();})();
