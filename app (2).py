import streamlit as st

st.set_page_config(page_title="🍓 sowmiyasan Calculator", page_icon="🍓", layout="centered")

# Hide Streamlit chrome
st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
[data-testid="stAppViewContainer"] {background: #fce4ec;}
[data-testid="stMain"] {background: transparent;}
[data-testid="stMainBlockContainer"] {padding: 0 !important; max-width: 100% !important;}
</style>
""", unsafe_allow_html=True)

CALCULATOR_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #fce4ec;
  font-family: Arial, sans-serif;
  position: relative;
  overflow: hidden;
}
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image:
    url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='60'%3E%3Ctext x='10' y='40' font-size='32'%3E%F0%9F%8D%93%3C/text%3E%3C/svg%3E"),
    url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='90' height='90'%3E%3Ctext x='30' y='65' font-size='28'%3E%F0%9F%8D%93%3C/text%3E%3C/svg%3E"),
    url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='75' height='75'%3E%3Ctext x='5' y='55' font-size='30'%3E%F0%9F%8D%93%3C/text%3E%3C/svg%3E");
  background-size: 160px 160px, 210px 210px, 185px 185px;
  background-position: 0 0, 80px 80px, 30px 130px;
  opacity: 0.18;
  pointer-events: none;
  z-index: 0;
}
.calc-shell {
  position: relative;
  z-index: 1;
  width: 300px;
  background: linear-gradient(170deg, #f8bbd0 0%, #f48fb1 60%, #e91e8c22 100%);
  border-radius: 12px 12px 18px 18px;
  padding: 14px 12px 18px;
  box-shadow: 0 8px 32px #c2185b55, 0 2px 0 #f48fb1 inset, 0 -3px 0 #ad1457 inset, 4px 0 0 #e91e8c33 inset, -4px 0 0 #e91e8c33 inset;
  border: 1.5px solid #e91e8c44;
}
.brand {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
  padding: 0 2px;
}
.brand-name {
  font-size: 7px;
  font-weight: bold;
  color: #880e4f;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}
.brand-model {
  font-size: 6px;
  color: #ad1457;
  letter-spacing: 0.5px;
}
.display-outer {
  background: #c8e6c9;
  border-radius: 4px;
  padding: 6px 8px 5px;
  margin-bottom: 10px;
  border: 1.5px solid #81c784;
  box-shadow: inset 0 2px 6px #00000022;
}
.display-indicators { display: flex; gap: 5px; margin-bottom: 3px; flex-wrap: wrap; }
.ind { font-size: 5.5px; color: #1b5e20; font-family: Arial, sans-serif; opacity: 0.7; }
.display-screen {
  font-family: 'Share Tech Mono', monospace;
  font-size: 22px;
  color: #1a1a1a;
  text-align: right;
  min-height: 30px;
  word-break: break-all;
  line-height: 1.1;
}
.display-history {
  font-family: 'Share Tech Mono', monospace;
  font-size: 9px;
  color: #2e7d32;
  text-align: right;
  min-height: 12px;
  opacity: 0.8;
}
.btn-section { display: flex; flex-direction: column; gap: 4px; }
.btn-row { display: grid; gap: 4px; }
.row-5 { grid-template-columns: repeat(5, 1fr); }
button {
  height: 28px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  font-size: 8.5px;
  font-weight: bold;
  color: #1a1a1a;
  transition: transform .07s, filter .07s, box-shadow .07s;
  outline: none;
  line-height: 1;
  padding: 0 1px;
  font-family: Arial, sans-serif;
}
button:hover  { filter: brightness(1.08); transform: translateY(-1px); }
button:active { filter: brightness(.9);  transform: translateY(1px); box-shadow: none !important; }
.btn-num { background: linear-gradient(170deg, #fce4ec, #f8bbd0); box-shadow: 0 3px 0 #c2185b55, 0 1px 3px #00000022; color: #1a1a1a; }
.btn-op  { background: linear-gradient(170deg, #f48fb1, #e91e8c99); box-shadow: 0 3px 0 #880e4f66, 0 1px 3px #00000022; color: #1a1a1a; }
.btn-fn  { background: linear-gradient(170deg, #f8bbd0cc, #f48fb188); box-shadow: 0 3px 0 #ad145744, 0 1px 3px #00000022; color: #1a1a1a; font-size: 7.5px; }
.btn-clear { background: linear-gradient(170deg, #ffcdd2, #ef9a9a); box-shadow: 0 3px 0 #c62828aa, 0 1px 3px #00000033; color: #b71c1c; }
.btn-eq { background: linear-gradient(170deg, #e91e63, #c2185b); box-shadow: 0 3px 0 #880e4f, 0 1px 3px #00000044; color: #fff; font-size: 13px; }
.btn-zero { grid-column: span 2; }
.footer { text-align: center; font-size: 6px; color: #880e4f; margin-top: 10px; letter-spacing: 0.5px; opacity: 0.8; }
</style>
</head>
<body>
<div class="calc-shell">
  <div class="brand">
    <span class="brand-name">✦ sowmiyasan</span>
    <span class="brand-model">Scientific Calculator</span>
  </div>
  <div class="display-outer">
    <div class="display-indicators">
      <span class="ind" id="ind-deg">DEG</span>
      <span class="ind" id="ind-rad" style="opacity:.25">RAD</span>
      <span class="ind">FIX</span>
      <span class="ind" id="ind-2nd" style="opacity:.25">2nd</span>
    </div>
    <div class="display-history" id="history">&nbsp;</div>
    <div class="display-screen" id="display">0</div>
  </div>
  <div class="btn-section">
    <div class="btn-row row-5">
      <button class="btn-fn" onclick="toggle2nd()">2nd</button>
      <button class="btn-fn" onclick="pressKey('mode')">MODE</button>
      <button class="btn-fn" onclick="pressKey('shift')">SHIFT</button>
      <button class="btn-fn" onclick="toggleDeg()">DEG</button>
      <button class="btn-clear" onclick="pressKey('AC')">AC</button>
    </div>
    <div class="btn-row row-5">
      <button class="btn-fn" onclick="pressKey('sq')">x²</button>
      <button class="btn-fn" onclick="pressKey('cube')">x³</button>
      <button class="btn-fn" onclick="pressKey('sqrt')">√</button>
      <button class="btn-fn" onclick="pressKey('cbrt')">∛</button>
      <button class="btn-clear" onclick="pressKey('DEL')">DEL</button>
    </div>
    <div class="btn-row row-5">
      <button class="btn-fn" onclick="pressKey('sin')">sin</button>
      <button class="btn-fn" onclick="pressKey('cos')">cos</button>
      <button class="btn-fn" onclick="pressKey('tan')">tan</button>
      <button class="btn-fn" onclick="pressKey('log')">log</button>
      <button class="btn-fn" onclick="pressKey('ln')">ln</button>
    </div>
    <div class="btn-row row-5">
      <button class="btn-fn" onclick="pressKey('(')">(</button>
      <button class="btn-fn" onclick="pressKey(')')">)</button>
      <button class="btn-fn" onclick="pressKey('%')">%</button>
      <button class="btn-fn" onclick="pressKey('^')">xʸ</button>
      <button class="btn-fn" onclick="pressKey('pi')">π</button>
    </div>
    <div class="btn-row row-5">
      <button class="btn-num" onclick="pressKey('7')">7</button>
      <button class="btn-num" onclick="pressKey('8')">8</button>
      <button class="btn-num" onclick="pressKey('9')">9</button>
      <button class="btn-op"  onclick="pressKey('/')">÷</button>
      <button class="btn-op"  onclick="pressKey('*')">×</button>
    </div>
    <div class="btn-row row-5">
      <button class="btn-num" onclick="pressKey('4')">4</button>
      <button class="btn-num" onclick="pressKey('5')">5</button>
      <button class="btn-num" onclick="pressKey('6')">6</button>
      <button class="btn-op"  onclick="pressKey('-')">−</button>
      <button class="btn-fn"  onclick="pressKey('+/-')">+/−</button>
    </div>
    <div class="btn-row row-5">
      <button class="btn-num" onclick="pressKey('1')">1</button>
      <button class="btn-num" onclick="pressKey('2')">2</button>
      <button class="btn-num" onclick="pressKey('3')">3</button>
      <button class="btn-op"  onclick="pressKey('+')">+</button>
      <button class="btn-fn"  onclick="pressKey('e_const')">e</button>
    </div>
    <div class="btn-row row-5">
      <button class="btn-num btn-zero" onclick="pressKey('0')">0</button>
      <button class="btn-num" onclick="pressKey('.')">.</button>
      <button class="btn-fn"  onclick="pressKey('ans')">ANS</button>
      <button class="btn-eq"  onclick="pressKey('=')">=</button>
    </div>
  </div>
  <div class="footer">🍓 made with love by sowmiya 🍓</div>
</div>
<script>
let useDeg = true, expr = '', lastResult = '0', justEvaled = false, is2nd = false;
const disp = document.getElementById('display');
const hist = document.getElementById('history');
const ind2nd = document.getElementById('ind-2nd');
const indDeg = document.getElementById('ind-deg');
const indRad = document.getElementById('ind-rad');
function setDisplay(v) { disp.textContent = String(v); }
function toggle2nd() { is2nd=!is2nd; ind2nd.style.opacity=is2nd?'1':'.25'; }
function toggleDeg() { useDeg=!useDeg; indDeg.style.opacity=useDeg?'1':'.25'; indRad.style.opacity=useDeg?'.25':'1'; }
function pressKey(k) {
  const digits='0123456789.';
  if(k==='AC'){ expr=''; setDisplay('0'); hist.innerHTML='&nbsp;'; justEvaled=false; return; }
  if(k==='DEL'){ if(justEvaled){expr='';setDisplay('0');justEvaled=false;return;} expr=expr.slice(0,-1); setDisplay(expr||'0'); return; }
  if(k==='mode'||k==='shift') return;
  if(justEvaled){ if(digits.includes(k)){expr='';hist.innerHTML='&nbsp;';} justEvaled=false; }
  if(k==='='){evaluate();return;}
  if(k==='+/-'){try{const v=parseFloat(expr);if(!isNaN(v)){expr=String(-v);setDisplay(expr);}}catch(e){} return;}
  if(k==='%'){try{const v=parseFloat(expr);if(!isNaN(v)){expr=String(v/100);setDisplay(expr);}}catch(e){} return;}
  if(k==='ans'){expr+=lastResult;setDisplay(expr);return;}
  if(k==='pi'){expr+='π';setDisplay(expr);return;}
  if(k==='e_const'){expr+='ℯ';setDisplay(expr);return;}
  const fnMap={sin:'sin(',cos:'cos(',tan:'tan(',log:'log(',ln:'ln(',sqrt:'√(',cbrt:'∛(',sq:'^2',cube:'^3'};
  if(fnMap[k]){expr+=fnMap[k];setDisplay(expr);return;}
  expr+=k; setDisplay(expr);
}
function toRad(d){return d*Math.PI/180;}
function evaluate(){
  if(!expr)return;
  try{
    let s=expr.replace(/π/g,'(Math.PI)').replace(/ℯ/g,'(Math.E)').replace(/\^/g,'**').replace(/√\(/g,'Math.sqrt(').replace(/∛\(/g,'Math.cbrt(');
    if(useDeg){s=s.replace(/sin\(/g,'_sin(').replace(/cos\(/g,'_cos(').replace(/tan\(/g,'_tan(');}
    s=s.replace(/log\(/g,'Math.log10(').replace(/ln\(/g,'Math.log(');
    if(!useDeg){s=s.replace(/sin\(/g,'Math.sin(').replace(/cos\(/g,'Math.cos(').replace(/tan\(/g,'Math.tan(');}
    const open=(s.match(/\(/g)||[]).length, close=(s.match(/\)/g)||[]).length;
    s+=')'.repeat(Math.max(0,open-close));
    const fn=new Function('_sin','_cos','_tan','Math',`"use strict";return(${s});`);
    let r=fn(x=>Math.sin(toRad(x)),x=>Math.cos(toRad(x)),x=>Math.tan(toRad(x)),Math);
    if(typeof r==='number'){r=parseFloat(r.toPrecision(12));if(isNaN(r)||!isFinite(r))throw new Error();r=r%1===0?r.toFixed(0):String(r);}
    hist.textContent=expr+' ='; lastResult=String(r); expr=String(r); setDisplay(r); justEvaled=true;
  }catch(e){setDisplay('Error');hist.textContent=expr;expr='';justEvaled=true;}
}
document.addEventListener('keydown',e=>{
  const map={'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','.':'.', '+':'+','-':'-','*':'*','/':'/','Enter':'=','=':'=','Backspace':'DEL','Escape':'AC','^':'^','(':'(',')':")'",'%':'%'};
  if(map[e.key]){e.preventDefault();pressKey(map[e.key]);}
});
</script>
</body>
</html>
"""

st.components.v1.html(CALCULATOR_HTML, height=620, scrolling=False)
