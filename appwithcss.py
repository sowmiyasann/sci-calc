import streamlit as st
import math

st.set_page_config(page_title="🍓 sowmiyasan Calculator", page_icon="🍓", layout="centered")

st.markdown("""<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">""", unsafe_allow_html=True)

st.markdown("""
<style>
#MainMenu, footer, header { visibility: hidden; }
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: #fce4ec !important;
}
[data-testid="stAppViewContainer"]::before {
    content: "🍓";
    display: none;
}
[data-testid="stMain"] { background: transparent !important; }
[data-testid="stMainBlockContainer"] { padding-top: 1rem !important; }
.calc-card {
    background: linear-gradient(160deg, #fff0f5 0%, #ffd6e4 100%);
    border: 3px solid #f9a8c9;
    border-radius: 28px;
    box-shadow: 0 8px 32px #f7b5cc88;
    padding: 24px 20px 20px;
    max-width: 400px;
    margin: 0 auto;
}
.calc-title {
    font-family: 'Press Start 2P', monospace;
    font-size: 0.7rem;
    color: #d4607a;
    text-align: center;
    margin-bottom: 16px;
    letter-spacing: 2px;
}
.display-box {
    background: #c8e6c9;
    border: 2px solid #81c784;
    border-radius: 10px;
    padding: 10px 14px 8px;
    margin-bottom: 16px;
    box-shadow: inset 0 2px 6px #00000018;
}
.display-history {
    font-family: 'Press Start 2P', monospace;
    font-size: 0.38rem;
    color: #2e7d32;
    min-height: 14px;
    text-align: right;
}
.display-main {
    font-family: 'Press Start 2P', monospace;
    font-size: 1.2rem;
    color: #1a1a1a;
    text-align: right;
    word-break: break-all;
    min-height: 34px;
    margin-top: 4px;
}
div[data-testid="stButton"] button {
    width: 100% !important;
    height: 48px !important;
    border-radius: 10px !important;
    font-family: 'Press Start 2P', monospace !important;
    font-size: 0.55rem !important;
    font-weight: bold !important;
    color: #1a1a1a !important;
    border: none !important;
    cursor: pointer !important;
    transition: transform .07s, filter .07s !important;
}
div[data-testid="stButton"] button:hover {
    transform: translateY(-2px) !important;
    filter: brightness(1.07) !important;
}
div[data-testid="stButton"] button:active {
    transform: translateY(1px) !important;
    filter: brightness(.92) !important;
}
div[data-testid="stButton"] button[kind="secondary"] {
    background: linear-gradient(160deg, #fce4ec, #f8bbd0) !important;
    box-shadow: 0 3px 0 #c2185b44 !important;
    color: #1a1a1a !important;
}
div[data-testid="stButton"] button[kind="primary"] {
    background: linear-gradient(160deg, #f48fb1, #e91e8c99) !important;
    box-shadow: 0 3px 0 #880e4f55 !important;
    color: #1a1a1a !important;
}
.eq-btn div[data-testid="stButton"] button {
    background: linear-gradient(160deg, #e91e63, #c2185b) !important;
    box-shadow: 0 3px 0 #880e4f !important;
    color: #fff !important;
}
.clr-btn div[data-testid="stButton"] button {
    background: linear-gradient(160deg, #ffcdd2, #ef9a9a) !important;
    box-shadow: 0 3px 0 #c6282888 !important;
    color: #b71c1c !important;
}
[data-testid="column"] { padding: 2px !important; }
</style>
""", unsafe_allow_html=True)

# ── strawberry background via JS ──────────────────────────────────────────────
st.markdown("""
<script>
document.addEventListener('DOMContentLoaded', function() {
    var app = document.querySelector('[data-testid="stAppViewContainer"]');
    if (app) {
        app.style.backgroundImage = "url('data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2280%22 height=%2280%22%3E%3Ctext x=%228%22 y=%2255%22 font-size=%2238%22%3E%F0%9F%8D%93%3C/text%3E%3C/svg%3E'), url('data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%22110%22 height=%22110%22%3E%3Ctext x=%2230%22 y=%2280%22 font-size=%2234%22%3E%F0%9F%8D%93%3C/text%3E%3C/svg%3E')";
        app.style.backgroundSize = "160px 160px, 220px 220px";
        app.style.backgroundPosition = "0 0, 90px 90px";
        app.style.backgroundRepeat = "repeat";
    }
});
</script>
""", unsafe_allow_html=True)

# ── State ─────────────────────────────────────────────────────────────────────
for k, v in {"expr": "", "display": "0", "history": "", "just_evaluated": False}.items():
    if k not in st.session_state:
        st.session_state[k] = v

def push(char):
    if st.session_state.just_evaluated:
        if char in "0123456789.":
            st.session_state.expr = ""
            st.session_state.history = ""
        st.session_state.just_evaluated = False
    st.session_state.expr += char
    st.session_state.display = st.session_state.expr

def evaluate():
    expr = st.session_state.expr
    if not expr:
        return
    try:
        safe = (expr
            .replace("π", str(math.pi))
            .replace("^", "**")
            .replace("√(", "math.sqrt(")
            .replace("∛(", "math.cbrt(")
            .replace("sin(", "math.sin(math.radians(")
            .replace("cos(", "math.cos(math.radians(")
            .replace("tan(", "math.tan(math.radians(")
            .replace("log(", "math.log10(")
            .replace("ln(", "math.log(")
        )
        open_p = safe.count("(")
        close_p = safe.count(")")
        safe += ")" * (open_p - close_p)
        result = eval(safe, {"__builtins__": {}}, {"math": math, "abs": abs})
        if isinstance(result, float):
            result = round(result, 10)
            if result == int(result):
                result = int(result)
        st.session_state.history = expr + " ="
        st.session_state.display = str(result)
        st.session_state.expr = str(result)
        st.session_state.just_evaluated = True
    except Exception:
        st.session_state.display = "Error"
        st.session_state.expr = ""
        st.session_state.just_evaluated = True

def clear_all():
    st.session_state.expr = ""
    st.session_state.display = "0"
    st.session_state.history = ""
    st.session_state.just_evaluated = False

def backspace():
    if st.session_state.just_evaluated:
        clear_all(); return
    st.session_state.expr = st.session_state.expr[:-1] or ""
    st.session_state.display = st.session_state.expr or "0"

def toggle_sign():
    try:
        val = float(st.session_state.expr)
        result = int(-val) if (-val) == int(-val) else -val
        st.session_state.expr = str(result)
        st.session_state.display = str(result)
    except Exception:
        pass

def percent():
    try:
        val = float(st.session_state.expr)
        result = val / 100
        st.session_state.expr = str(result)
        st.session_state.display = str(result)
    except Exception:
        pass

# ── Layout ────────────────────────────────────────────────────────────────────
st.markdown('<div class="calc-card">', unsafe_allow_html=True)
st.markdown('<div class="calc-title">🍓 sowmiyasan 🍓</div>', unsafe_allow_html=True)
st.markdown(
    f'<div class="display-box">'
    f'<div class="display-history">{st.session_state.history or "&nbsp;"}</div>'
    f'<div class="display-main">{st.session_state.display}</div>'
    f'</div>',
    unsafe_allow_html=True,
)

rows = [
    [("sin(","sin(","op"),("cos(","cos(","op"),("tan(","tan(","op"),("π","π","op")],
    [("log(","log(","op"),("ln(","ln(","op"),("√(","√(","op"),("x²","^2","op")],
    [("(","(","op"),(")",")","op"),("%","%","clr"),("AC","ac","clr")],
    [("+/-","+/-","op"),("e","2.71828","op"),("^","^","op"),("⌫","bs","clr")],
    [("7","7","num"),("8","8","num"),("9","9","num"),("÷","/","op")],
    [("4","4","num"),("5","5","num"),("6","6","num"),("×","*","op")],
    [("1","1","num"),("2","2","num"),("3","3","num"),("−","-","op")],
    [("0","0","num"),(".",".", "num"),("ANS","ans","op"),("+","+","op")],
    [("=","=","eq"),("","","none"),("","","none"),("","","none")],
]

for row in rows:
    cols = st.columns(len(row))
    for col, (label, key, btype) in zip(cols, row):
        if not label:
            continue
        with col:
            if btype == "eq":
                st.markdown('<div class="eq-btn">', unsafe_allow_html=True)
                if st.button(label, key=f"b_{label}_{key}", use_container_width=True):
                    evaluate()
                st.markdown('</div>', unsafe_allow_html=True)
            elif btype == "clr":
                st.markdown('<div class="clr-btn">', unsafe_allow_html=True)
                if st.button(label, key=f"b_{label}_{key}", use_container_width=True):
                    if key == "ac": clear_all()
                    elif key == "bs": backspace()
                    elif key == "%": percent()
                st.markdown('</div>', unsafe_allow_html=True)
            elif btype == "op":
                if st.button(label, key=f"b_{label}_{key}", use_container_width=True, type="primary"):
                    if key == "+/-": toggle_sign()
                    elif key == "ans": push(st.session_state.display)
                    else: push(key)
            elif btype == "num":
                if st.button(label, key=f"b_{label}_{key}", use_container_width=True, type="secondary"):
                    push(key)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;font-family:Arial;font-size:0.6rem;color:#e082a0;margin-top:12px;">🍓 made with love & strawberries 🍓</p>', unsafe_allow_html=True)
