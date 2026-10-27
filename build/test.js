global.window=global; global.navigator={userAgent:'node'};
require('/workspace/skulpt.min.js'); require('/workspace/skulpt-stdlib.js');
const fs=require('fs'), Sk=global.Sk, real=JSON.parse(fs.readFileSync('realpy.json'));
const expect={starter:false,solution:true,wrong:false}; const exp1={"l1-sample-program|starter":true};
function getCheck(id){const h=fs.readFileSync('../activities/'+id+'.html','utf8');const m=h.match(/function CHECK[\s\S]*?\n}\n(?=var ta)/);return eval('('+m[0]+')');}
async function sk(code){let out='';Sk.configure({__future__:Sk.python2,output:t=>out+=t,read:f=>Sk.builtinFiles.files[f]});
 const m=await Sk.misceval.asyncToPromise(()=>Sk.importMainWithBody('<stdin>',false,code,true));const v={};
 for(const k of Object.keys(m.$d)){if(k.startsWith('__'))continue;const j=Sk.ffi.remapToJs(m.$d[k]);if(typeof j=='number'||typeof j=='string')v[k.replace(/_\$rw\$$/,'')]=j}return{out,v};}
(async()=>{let fail=0;for(const key of Object.keys(real)){const [id,kind]=key.split('|');const C=getCheck(id);const r=real[key];
 const want=key in exp1?exp1[key]:expect[kind];
 const a=C(r.out,r.v,r.code); const s=await sk(r.code); const b=C(s.out,s.v,r.code);
 const good=a.ok===want&&b.ok===want; if(!good)fail++;
 console.log((good?'PASS':'FAIL'),key,'| python3:',a.ok,'| skulpt:',b.ok,'|',b.msg);}
 console.log('failures',fail)})();
