import streamlit as st
import tamilrulepy
import importlib.util
import os

# 1. பக்க வடிவமைப்பு மற்றும் தலைப்பு அமைத்தல்
st.set_page_config(page_title="தொல்காபை ஆய்வி", layout="wide")

# --- நவீன CSS வடிவமைப்பு ---
st.markdown("""
    <style>
    /* தமிழ் எழுத்துரு இறக்குமதி */
    @import url('https://fonts.googleapis.com/css2?family=Mukta+Malar:wght@400;700&display=swap');

    /* ஒட்டுமொத்த உடல் பகுதி */
    .stApp {
        background-color: #f9f7f2;
        font-family: 'Mukta Malar', sans-serif;
    }

    /* பிரதான தலைப்பு (Tolkapy) */
    .main-title {
        background: linear-gradient(90deg, #2c3e50, #4a69bd);
        color: white;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }

    /* Tabs (தாவல்கள்) வடிவமைப்பு */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #ffffff;
        padding: 10px;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }

    .stTabs [data-baseweb="tab"] {
        background-color: #f1f2f6;
        border-radius: 8px;
        padding: 12px 25px;
        font-weight: bold;
        color: #57606f;
    }

    .stTabs [aria-selected="true"] {
        background-color: #e67e22 !important;
        color: white !important;
    }

    /* பொத்தான்கள் (Buttons) */
    div.stButton > button {
        background-color: #2c3e50;
        color: white;
        border-radius: 8px;
        width: 100%;
        border: none;
        padding: 10px;
        font-weight: bold;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #e67e22;
        color: white;
        transform: translateY(-2px);
    }

    /* உள்ளீட்டு பெட்டிகள் */
    .stTextInput input {
        border-radius: 8px !important;
        border: 1px solid #dcdde1 !important;
    }

    /* முடிவுகள் (Success/Info) */
    .stAlert {
        border-radius: 12px;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }

    /* அடிக்குறிப்பு (Footer) */
    .footer {
        text-align: center;
        padding: 20px;
        color: #57606f;
        border-radius: 8px !important;
        border: 1px solid #dcdde1 !important;        
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- தலைப்புப் பகுதி ---
st.markdown('<div class="main-title"><h1>📜 தொல்காபை ஆய்வி (Tolkapy Research Tool)</h1><p>தமிழ் இலக்கண ஆய்வுக் கருவி</p></div>', unsafe_allow_html=True)

# 2. vidhikal.py கோப்பைத் தேடி இறக்குதல் (Dynamic Loading)
def load_tolkapy_rules():
    try:
        base_path = os.path.dirname(tamilrulepy.__file__)
        vidhikal_path = os.path.join(base_path, "vidhikal.py")
        spec = importlib.util.spec_from_file_location("vidhikal", vidhikal_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    except:
        return None

rules = load_tolkapy_rules()

# 3. தாவல்கள் (Tabs) அமைத்தல்
tab1, tab2, tab3, tab4 = st.tabs(["🧩 மெய்ம்மயக்கம்", "🏁 மொழிமுதல்", "🔚 மொழியிறுதி", "🔗 புணர்ச்சி"])

# --- TAB 1: மெய்ம்மயக்கம் ---
with tab1:
    st.subheader("மெய்ம்மயக்கம் ஆய்வு")
    word_m = st.text_input("சொல்லை உள்ளிடவும்:", key="m1", placeholder="எ.கா: கற்க")
    if st.button("ஆராய்க", key="b1"):
        if rules and hasattr(rules, 'meymayakkam_checker'):
            res = rules.meymayakkam_checker(word_m)
            st.success(f"**முடிவு:** {res}")
        else:
            st.error("விதித் தொகுப்பு (Rules) கண்டறியப்படவில்லை.")

# --- TAB 2: மொழிமுதல் ---
with tab2:
    st.subheader("மொழிமுதல் ஆய்வு")
    word_f = st.text_input("சொல்லை உள்ளிடவும்:", key="f1", placeholder="எ.கா: தந்தை")
    if st.button("சரிபார்", key="b2"):
        if rules and hasattr(rules, 'mozhi_muthal_checker'):
            res = rules.mozhi_muthal_checker(word_f)
            st.info(f"**ஆய்வு முடிவு:** {res}")
        else:
            st.warning("மொழிமுதல் விதிச் செயல்பாடுகள் கண்டறியப்படவில்லை.")

# --- TAB 3: மொழியிறுதி ---
with tab3:
    st.header("மொழியிறுதி ஆய்வு")
    word_e = st.text_input("சொல்லை உள்ளிடவும்:", key="e1", placeholder="எ.கா: மரம்")
    if st.button("சரிபார்", key="b3"):
        if rules and hasattr(rules, 'mozhi_iruthi_checker'):
            res = rules.mozhi_iruthi_checker(word_e)
            st.info(f"**ஆய்வு முடிவு:** {res}")
        else:
            st.warning("மொழியிறுதி விதிச் செயல்பாடுகள் கண்டறியப்படவில்லை.")

# --- TAB 4: புணர்ச்சி ---
with tab4:
    st.header("புணர்ச்சி ஆய்வு")
    col1, col2 = st.columns(2)
    with col1: 
        n_mozhi = st.text_input("நிலைமொழி:", key="n1", placeholder="எ.கா: பனை")
    with col2: 
        v_mozhi = st.text_input("வருமொழி:", key="v1", placeholder="எ.கா: காய்")
    
    if st.button("புணர்க்க", key="b4"):
        if rules and hasattr(rules, 'punarchi_checker'):
            res = rules.punarchi_checker(n_mozhi, v_mozhi)
            st.success(f"**புணர்ச்சி முடிவு:** {res}")
        else:
            st.code(f"{n_mozhi} + {v_mozhi}")
            st.write("குறிப்பு: நூலகத்தில் புணர்ச்சி விதிகள் மேம்படுத்தப்படுகின்றன.")

# --- அடிக்குறிப்பு ---
st.markdown("""
    <div class="footer">
        <hr>
        முனைவர் சத்தியராசு தங்கச்சாமி, பூபாலன் & குழுவினர் | தமிழ் இலக்கணத் தரவுத் தளம்
    </div>
    """, unsafe_allow_html=True)
