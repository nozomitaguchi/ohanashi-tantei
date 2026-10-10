// Expected readings are independent fixtures, including contextual homographs.
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const source=fs.readFileSync('app.js','utf8'),context={};vm.createContext(context);
vm.runInContext(fs.readFileSync('questions.js','utf8')+source.slice(0,source.indexOf('function mini'))+source.slice(source.indexOf('const readings='),source.indexOf('function addRuby'))+'globalThis.questionsForAudit=questions;globalThis.readingsForAudit=readings',context);
const readings=context.readingsForAudit,pattern=new RegExp(Object.keys(readings).sort((a,b)=>b.length-a.length).join('|'),'g');
const read=text=>text.replace(pattern,key=>readings[key]);
const cases={
'街の人':'まちのひと','店の人':'みせのひと','７人':'ななにん','何人':'なんにん','何を 答えれば':'なにを こたえれば',
'少しずつ':'すこしずつ','少ない':'すくない','出来事':'できごと','日よう日':'にちようび','数を 数えます':'かずを かぞえます','今回は':'こんかいは',
'含まれています':'ふくまれています','差を 見つけます':'さを みつけます','お花見':'おはなみ','花びら':'はなびら','雪だるま':'ゆきだるま','何本':'なんぼん',
'１人':'ひとり','２人':'ふたり','４人':'よにん','14人':'じゅうよにん',
'1本':'いっぽん','2本':'にほん','3本':'さんぼん','4本':'よんほん','5本':'ごほん','6本':'ろっぽん','7本':'ななほん','8本':'はっぽん','9本':'きゅうほん','10本':'じゅっぽん',
'11本':'じゅういっぽん','16本':'じゅうろっぽん','18本':'じゅうはっぽん','20本':'にじゅっぽん','本を かります':'ほんを かります',
'1回':'いっかい','3回':'さんかい','6回':'ろっかい','8回':'はっかい','10回':'じゅっかい','11回':'じゅういっかい','16回':'じゅうろっかい','18回':'じゅうはっかい','20回':'にじゅっかい',
'何度でも':'なんどでも','もう一度':'もういちど','準備中':'じゅんびちゅう'};
for(const [text,expected]of Object.entries(cases))assert.strictEqual(read(text),expected,text);
let fields=0;const missing=[];
for(const [i,q]of context.questionsForAudit.entries())for(const text of [q.t,q.why,q.ex,...q.ask]){fields++;const remaining=read(text).match(/[一-龯]+/g);if(remaining)missing.push({question:i+1,text,remaining})}
assert.deepStrictEqual(missing,[],'Missing furigana');
console.log(`${context.questionsForAudit.length}問・${fields}文の未対応漢字なし。独立した期待値${Object.keys(cases).length}件が一致。`);
