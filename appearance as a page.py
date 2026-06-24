import streamlit as st
import math

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="🍓 sowmiyasan Calculator",
    page_icon="🍓",
    layout="centered",
)

# ── Google Font (Press Start 2P = pixel font) + custom CSS ───────────────────
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <style>
    /* ── background & global ── */
    html, body, [data-testid="stAppViewContainer"] {
        background: #fce4ec !important;
    }
    [data-testid="stAppViewContainer"] {
        background-color: #fce4ec !important;
        background-image:
            url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='80' height='80'%3E%3Ctext x='8' y='55' font-size='38'%3E%F0%9F%8D%93%3C/text%3E%3C/svg%3E"),
            url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='110' height='110'%3E%3Ctext x='30' y='80' font-size='34'%3E%F0%9F%8D%93%3C/text%3E%3C/svg%3E"),
            url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='95' height='95'%3E%3Ctext x='5' y='70' font-size='40'%3E%F0%9F%8D%93%3C/text%3E%3C/svg%3E"),
            url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='70' height='70'%3E%3Ctext x='15' y='50' font-size='30'%3E%F0%9F%8D%93%3C/text%3E%3C/svg%3E") !important;
        background-size: 160px 160px, 220px 220px, 190px 190px, 140px 140px !important;
        background-position: 0 0, 90px 90px, 40px 140px, 130px 30px !important;
        background-repeat: repeat !important;
    }
    [data-testid="stHeader"] { background: transparent !important; }
    [data-testid="stMainBlockContainer"] { padding-top: 1.5rem !important; }

    /* hide streamlit chrome */
    #MainMenu, footer, header { visibility: hidden; }

    /* ── calculator card ── */
    .calc-card {
        background: linear-gradient(160deg, #fff0f5 0%, #ffd6e4 100%);
        border: 3px solid #f9a8c9;
        border-radius: 28px;
        box-shadow: 0 8px 32px #f7b5cc88, 0 2px 8px #e8839755;
        padding: 28px 24px 24px;
        max-width: 420px;
        margin: 0 auto;
        position: relative;
        overflow: visible;
    }

    /* ── title ── */
    .calc-title {
        font-family: 'Press Start 2P', monospace;
        font-size: 0.75rem;
        color: #d4607a;
        text-align: center;
        margin-bottom: 18px;
        letter-spacing: 2px;
        text-shadow: 1px 1px 0 #ffc4d8;
    }

    /* ── display ── */
    .display-box {
        background: #fff0f5;
        border: 2.5px solid #f9a8c9;
        border-radius: 16px;
        padding: 14px 18px 10px;
        margin-bottom: 18px;
        box-shadow: inset 0 2px 8px #ffd6e488;
        position: relative;
    }
    .display-history {
        font-family: 'Press Start 2P', monospace;
        font-size: 0.45rem;
        color: #e082a0;
        min-height: 16px;
        word-break: break-all;
    }
    .display-main {
        font-family: 'Press Start 2P', monospace;
        font-size: 1.35rem;
        color: #c43a65;
        text-align: right;
        word-break: break-all;
        min-height: 38px;
        margin-top: 4px;
        text-shadow: 1px 1px 0 #ffc4d8;
    }

    /* ── buttons ── */
    div[data-testid="stButton"] button {
        width: 100% !important;
        height: 54px !important;
        border-radius: 14px !important;
        font-family: 'Press Start 2P', monospace !important;
        font-size: 0.6rem !important;
        cursor: pointer !important;
        transition: transform .08s, box-shadow .08s, filter .08s !important;
        line-height: 1 !important;
        border: none !important;
    }
    div[data-testid="stButton"] button:hover {
        transform: translateY(-2px) scale(1.04) !important;
        filter: brightness(1.06) !important;
    }
    div[data-testid="stButton"] button:active {
        transform: translateY(1px) scale(.97) !important;
        filter: brightness(.94) !important;
    }

    /* number buttons */
    div[data-testid="stButton"] button[kind="secondary"] {
        background: linear-gradient(160deg, #fff0f5 0%, #ffd6e4 100%) !important;
        color: #c43a65 !important;
        box-shadow: 0 4px 0 #f9a8c9, 0 2px 8px #f9a8c955 !important;
    }

    /* operator / sci buttons – pink */
    div[data-testid="stButton"] button[kind="primary"] {
        background: linear-gradient(160deg, #ffb3cc 0%, #f97eab 100%) !important;
        color: #fff !important;
        box-shadow: 0 4px 0 #d4607a, 0 2px 8px #f97eab55 !important;
        text-shadow: 0 1px 2px #c43a6588 !important;
    }

    /* equals button – hot pink */
    .eq-btn div[data-testid="stButton"] button {
        background: linear-gradient(160deg, #ff80aa 0%, #e8305a 100%) !important;
        color: #fff !important;
        box-shadow: 0 4px 0 #b8234a, 0 2px 10px #e8305a77 !important;
        text-shadow: 0 1px 3px #b8234a99 !important;
        height: 54px !important;
    }

    /* clear button – soft red */
    .clr-btn div[data-testid="stButton"] button {
        background: linear-gradient(160deg, #ffccd5 0%, #ff7096 100%) !important;
        color: #7a0025 !important;
        box-shadow: 0 4px 0 #c95070, 0 2px 8px #ff709666 !important;
    }

    /* ── strawberry decorations ── */
    .strawberries {
        position: absolute;
        top: -22px;
        right: 18px;
        font-size: 2.2rem;
        letter-spacing: 4px;
        pointer-events: none;
        filter: drop-shadow(0 2px 4px #f9a8c988);
    }

    /* column gap tightening */
    [data-testid="column"] { padding: 2px !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── State ─────────────────────────────────────────────────────────────────────
def init():
    defaults = {
        "expr": "",       # what user is building
        "display": "0",   # shown in main display
        "history": "",    # small top line
        "just_evaluated": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init()

# ── Helpers ───────────────────────────────────────────────────────────────────
def push(char):
    if st.session_state.just_evaluated:
        # after = , continue building unless it's a digit/dot (new number)
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
        # safe eval: replace tokens
        safe = (expr
            .replace("π", str(math.pi))
            .replace("e", str(math.e))
            .replace("^", "**")
            .replace("√(", "math.sqrt(")
            .replace("sin(", "math.sin(math.radians(")
            .replace("cos(", "math.cos(math.radians(")
            .replace("tan(", "math.tan(math.radians(")
            .replace("log(", "math.log10(")
            .replace("ln(", "math.log(")
            .replace("abs(", "abs(")
        )
        # close extra parens from trig replacements
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
        st.session_state.display = "Error 🍓"
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
        result = -val
        if result == int(result): result = int(result)
        st.session_state.expr = str(result)
        st.session_state.display = st.session_state.expr
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
st.markdown('<div class="strawberries">🍓🍓🍓</div>', unsafe_allow_html=True)
st.markdown('<div class="calc-title">🍓 sowmiyasan 🍓</div>', unsafe_allow_html=True)

# Display
st.markdown(
    f"""
    <div class="display-box">
        <div class="display-history">{st.session_state.history or "&nbsp;"}</div>
        <div class="display-main">{st.session_state.display}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Button grid ───────────────────────────────────────────────────────────────
# Each row: (label, action_key, type)  type: "num" | "op" | "eq" | "clr"
rows = [
    [("sin(", "sin(", "op"), ("cos(", "cos(", "op"), ("tan(", "tan(", "op"), ("π",    "π",   "op")],
    [("log(", "log(", "op"), ("ln(",  "ln(",  "op"), ("√(",   "√(",   "op"), ("x²",   "^2",  "op")],
    [("(",    "(",    "op"), (")",    ")",    "op"), ("%",    "%",   "clr"), ("AC",   "ac",  "clr")],
    [("+/-",  "+/-",  "op"), ("e",    "e",   "op"),  ("^",    "^",   "op"), ("⌫",    "bs",  "clr")],
    [("7",    "7",    "num"), ("8",   "8",   "num"), ("9",    "9",   "num"), ("÷",    "/",   "op")],
    [("4",    "4",    "num"), ("5",   "5",   "num"), ("6",    "6",   "num"), ("×",    "*",   "op")],
    [("1",    "1",    "num"), ("2",   "2",   "num"), ("3",    "3",   "num"), ("−",    "-",   "op")],
    [("0",    "0",    "num"), (".",   ".",   "num"), ("abs(", "abs(","op"), ("+",    "+",   "op")],
    [("=",    "=",    "eq"),  ("",    "",    "none"), ("",    "",    "none"), ("",    "",    "none")],
]

for row in rows:
    cols = st.columns(len(row))
    for col, (label, key, btype) in zip(cols, row):
        if not label:
            continue
        with col:
            if btype == "eq":
                st.markdown('<div class="eq-btn">', unsafe_allow_html=True)
                if st.button(label, key=f"btn_{label}_{key}", use_container_width=True):
                    evaluate()
                st.markdown('</div>', unsafe_allow_html=True)
            elif btype == "clr":
                st.markdown('<div class="clr-btn">', unsafe_allow_html=True)
                btn_type = "secondary"
                if st.button(label, key=f"btn_{label}_{key}", use_container_width=True):
                    if key == "ac":  clear_all()
                    elif key == "bs": backspace()
                    elif key == "%":  percent()
                st.markdown('</div>', unsafe_allow_html=True)
            elif btype == "op":
                if st.button(label, key=f"btn_{label}_{key}", use_container_width=True, type="primary"):
                    if key == "+/-": toggle_sign()
                    else: push(key)
            elif btype == "num":
                if st.button(label, key=f"btn_{label}_{key}", use_container_width=True, type="secondary"):
                    push(key)

st.markdown('</div>', unsafe_allow_html=True)  # close calc-card

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <p style="text-align:center;font-family:'Press Start 2P',monospace;
    font-size:0.4rem;color:#e082a0;margin-top:18px;">
    🍓 made with love & strawberries 🍓
    </p>
    """,
    unsafe_allow_html=True,
)
