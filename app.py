import streamlit as st
import tamilrulepy
import importlib.util
import os

# 1. vidhikal.py கோப்பைத் தேடி இறக்குதல் (Dynamic Loading)
def load_tolkapy_rules():
    try:
        base_path = os.path.dirname(tamilrulepy.__file__)
        vidhikal_path = os.path.join(base_path, "vidhikal.py")
        
        if not os.path.exists(vidhikal_path):
            return None, f"கோப்பு காணப்படவில்லை: {vidhikal_path}"
            
        spec = importlib.util.spec_from_file_location("vidhikal", vidhikal_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod, "வெற்றி"
    except Exception as e:
        return None, str(e)

rules, status = load_tolkapy_rules()

# 2. பக்க வடிவமைப்பு
st.set_page_config(page_title="தொல்காபை ஆய்வி", layout="wide")
st.title("📜 Tolkapy (தொல்காபை)🖋️")

# --- CSS வடிவமைப்பு தொடக்கம் ---
st.markdown("""
    <style>
    /* கூகுள் தமிழ் எழுத்துரு */
    @import url('https://fonts.googleapis.com/css2?family=Mukta+Malar:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Mukta Malar', sans-serif;
    }

    /* பிரதான பின்னணி */
    .main {
        background-color: #fcfaf5;
    }

    /* தலைப்புப் பகுதி */
    .stTitle {
        color: #2c3e50;
        text-align: center;
        background: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-bottom: 5px solid #e67e22;
    }

    /* Tabs (தாவல்கள்) வடிவமைப்பு */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #f1f2f6;
        border-radius: 10px 10px 0px 0px;
        padding: 10px 20px;
        font-weight: bold;
    }

    .stTabs [aria-selected="true"] {
        background-color: #e67e22 !important;
        color: white !important;
    }

    /* உள்ளீடு மற்றும் பொத்தான்கள் */
    .stButton button {
        background-color: #2c3e50 !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        transition: 0.3s ease;
    }

    .stButton button:hover {
        background-color: #e67e22 !important;
        transform: scale(1.02);
    }

    /* முடிவு காட்டும் பெட்டிகள் */
    .stSuccess, .stInfo {
        border-radius: 10px;
        border-left: 5px solid #27ae60;
    }
    
    </style>
    """, unsafe_allow_html=True)
# --- CSS வடிவமைப்பு முடிவு ---

# மீதமுள்ள உங்கள் குறியீட்டை இங்கே தொடரவும்...
def load_tolkapy_rules():
    # (உங்கள் பழைய குறியீடு அப்படியே இருக்கட்டும்)
    
# நூலகம் லோட் ஆகவில்லை என்றால் எச்சரிக்கை காட்டும்
if rules is None:
    st.error(f"நூலகத்தை ஏற்றுவதில் சிக்கல்: {status}")

tab1, tab2, tab3, tab4 = st.tabs(["மெய்ம்மயக்கம்", "மொழிமுதல்", "மொழியிறுதி", "புணர்ச்சி"])

# --- TAB 1: மெய்ம்மயக்கம் ---
with tab1:
    st.header("மெய்ம்மயக்கம் ஆய்வு")
    word_m = st.text_input("சொல்லை உள்ளிடவும்:", key="m1")
    if st.button("ஆராய்க", key="b1"):
        if rules and hasattr(rules, 'meymayakkam_checker'):
            res = rules.meymayakkam_checker(word_m)
            st.success(f"முடிவு: {res}")
        else:
            st.warning("மெய்ம்மயக்கம் விதிச் செயல்பாடுகள் (meymayakkam_checker) கண்டறியப்படவில்லை.")

# --- TAB 2: மொழிமுதல் ---
with tab2:
    st.header("மொழிமுதல் ஆய்வு")
    word_f = st.text_input("சொல்லை உள்ளிடவும்:", key="f1")
    if st.button("சரிபார்", key="b2"):
        if rules and hasattr(rules, 'mozhi_muthal_checker'):
            res = rules.mozhi_muthal_checker(word_f)
            st.info(f"ஆய்வு முடிவு: {res}")
        else:
            st.warning("மொழிமுதல் விதிச் செயல்பாடுகள் கண்டறியப்படவில்லை.")

# --- TAB 3: மொழியிறுதி ---
with tab3:
    st.header("மொழியிறுதி ஆய்வு")
    word_e = st.text_input("சொல்லை உள்ளிடவும்:", key="e1")
    if st.button("சரிபார்", key="b3"):
        if rules and hasattr(rules, 'mozhi_iruthi_checker'):
            res = rules.mozhi_iruthi_checker(word_e)
            st.info(f"ஆய்வு முடிவு: {res}")
        else:
            st.warning("மொழியிறுதி விதிச் செயல்பாடுகள் கண்டறியப்படவில்லை.")

# --- TAB 4: புணர்ச்சி ---
with tab4:
    st.header("புணர்ச்சி ஆய்வு")
    c1, c2 = st.columns(2)
    with c1: n_mozhi = st.text_input("நிலைமொழி:", key="n1")
    with c2: v_mozhi = st.text_input("வருமொழி:", key="v1")
    if st.button("புணர்க்க", key="b4"):
        if rules and hasattr(rules, 'punarchi_checker'):
            res = rules.punarchi_checker(n_mozhi, v_mozhi)
            st.success(f"புணர்ச்சி முடிவு: {res}")
        else:
            st.code(f"{n_mozhi} + {v_mozhi}")
            st.info("குறிப்பு: நூலகத்தில் புணர்ச்சி விதிகள் (punarchi_checker) இன்னும் இணைக்கப்படவில்லை.")

st.divider()
st.caption("முனைவர் சத்தியராசு தங்கச்சாமி & குழுவினர் | ")
