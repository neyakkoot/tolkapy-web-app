import streamlit as st
import tamilrulepy
import importlib.util
import os

# 1. பக்க வடிவமைப்பு
st.set_page_config(page_title="தொல்காப்பி ஆய்வி", layout="wide")

# --- Tholkaappiyam App போன்ற வடிவமைப்பு (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Mukta+Malar:wght@400;700&display=swap');

    /* ஒட்டுமொத்த பின்னணி */
    .stApp {
        background: #fdf2f8; /* மென்மையான இளஞ்சிவப்பு பின்னணி */
        font-family: 'Mukta Malar', sans-serif;
    }

    /* பிரதான தலைப்பு அட்டை */
    .main-title {
        background: #ec4899; /* Pink color as per the reference */
        color: white;
        padding: 40px 20px;
        border-radius: 0px 0px 30px 30px; /* கீழ்நோக்கிய வளைவு */
        text-align: center;
        margin: -60px -20px 30px -20px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }

    /* Tabs (தாவல்கள்) - App Bar போல */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        background-color: white;
        padding: 10px;
        border-radius: 15px;
        justify-content: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }

    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 10px;
        padding: 10px 20px;
        color: #ec4899;
        font-weight: bold;
        border: none;
    }

    .stTabs [aria-selected="true"] {
        background-color: #fbcfe8 !important;
        border-bottom: 3px solid #ec4899 !important;
    }

    /* உள்ளீட்டுப் பெட்டிகள் மற்றும் அட்டைகள் */
    .stTextInput input {
        border-radius: 15px !important;
        border: 2px solid #f9a8d4 !important;
        padding: 12px !important;
        background: white;
    }

    /* அழகான பொத்தான்கள் */
    div.stButton > button {
        background: linear-gradient(135deg, #ec4899 0%, #be185d 100%);
        color: white;
        border-radius: 15px;
        width: 100%;
        border: none;
        padding: 12px;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(236, 72, 153, 0.3);
        transition: 0.3s;
    }

    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 15px rgba(236, 72, 153, 0.4);
        color: white;
    }

    /* ஆய்வு முடிவுகள் தோற்றம் */
    .stAlert {
        border-radius: 20px;
        background-color: white !important;
        border: 1px solid #fbcfe8 !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }

    /* அடிக்குறிப்பு */
    .footer {
        text-align: center;
        padding: 25px;
        background: white;
        border-radius: 20px 20px 0 0;
        margin-top: 50px;
        color: #9d174d;
        font-weight: bold;
        box-shadow: 0 -5px 10px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- தலைப்புப் பகுதி ---
st.markdown('<div class="main-title"><h1>📜 தொல்காப்பி ஆய்வி</h1><p>Tholkaappiyam Research Tool</p></div>', unsafe_allow_html=True)

# 2. விதிகள் ஏற்றம்
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

# 3. உள்ளடக்க அமைப்பு (Container)
with st.container():
    tab1, tab2, tab3, tab4 = st.tabs(["🧩 மெய்ம்மயக்கம்", "🏁 மொழிமுதல்", "🔚 மொழியிறுதி", "🔗 புணர்ச்சி"])

    with tab1:
        st.markdown("### மெய்ம்மயக்கம் ஆய்வு")
        word_m = st.text_input("சொல்லை உள்ளிடவும்:", key="m1", placeholder="எ.கா: கற்க")
        if st.button("ஆராய்க", key="b1"):
            if rules and hasattr(rules, 'meymayakkam_checker'):
                res = rules.meymayakkam_checker(word_m)
                st.success(f"**முடிவு:** {res}")
            else:
                st.error("விதித் தொகுப்பு கண்டறியப்படவில்லை.")

    with tab2:
        st.markdown("### மொழிமுதல் ஆய்வு")
        word_f = st.text_input("சொல்லை உள்ளிடவும்:", key="f1", placeholder="எ.கா: தந்தை")
        if st.button("சரிபார்", key="b2"):
            if rules and hasattr(rules, 'mozhi_muthal_checker'):
                res = rules.mozhi_muthal_checker(word_f)
                st.info(f"**ஆய்வு முடிவு:** {res}")
            else:
                st.warning("மொழிமுதல் விதிச் செயல்பாடுகள் இல்லை.")

    with tab3:
        st.markdown("### மொழியிறுதி ஆய்வு")
        word_e = st.text_input("சொல்லை உள்ளிடவும்:", key="e1", placeholder="எ.கா: மரம்")
        if st.button("சரிபார்", key="b3"):
            if rules and hasattr(rules, 'mozhi_iruthi_checker'):
                res = rules.mozhi_iruthi_checker(word_e)
                st.info(f"**ஆய்வு முடிவு:** {res}")
            else:
                st.warning("மொழியிறுதி விதிச் செயல்பாடுகள் இல்லை.")

    with tab4:
        st.markdown("### புணர்ச்சி ஆய்வு")
        col1, col2 = st.columns(2)
        with col1: n_mozhi = st.text_input("நிலைமொழி:", key="n1")
        with col2: v_mozhi = st.text_input("வருமொழி:", key="v1")
        if st.button("புணர்க்க", key="b4"):
            if rules and hasattr(rules, 'punarchi_checker'):
                res = rules.punarchi_checker(n_mozhi, v_mozhi)
                st.success(f"**முடிவு:** {res}")
            else:
                st.code(f"{n_mozhi} + {v_mozhi}")

# --- அடிக்குறிப்பு ---
st.markdown("""
    <div class="footer">
        முனைவர் சத்தியராசு தங்கச்சாமி, பூபாலன் & குழுவினர்<br>
        <span style="font-size: 0.8rem; font-weight: normal;">தமிழ் இலக்கணத் தரவுத் தளம் | 2025</span>
    </div>
    """, unsafe_allow_html=True)
