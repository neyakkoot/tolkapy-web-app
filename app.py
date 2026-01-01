import streamlit as st
import tamilrulepy
import importlib.util
import os

# 1. பக்க வடிவமைப்பு
st.set_page_config(page_title="தொல்காப்பி ஆய்வி", layout="wide")

# --- பின்னணிப் படம் மற்றும் அழகியல் வடிவமைப்பு (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Mukta+Malar:wght@400;700&display=swap');

    /* பின்னணிப் படத்தை முழுமையாக இணைத்தல் */
    .stApp {
        background: url("https://generated-image-url.com/your-image.png"); /* இங்கே உங்கள் படத்தின் URL-ஐ இடவும் */
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Mukta Malar', sans-serif;
    }

    /* பிரதான தலைப்பு அட்டை - கண்ணாடி போன்ற தோற்றம் */
    .main-title {
        background: rgba(236, 72, 153, 0.85); /* லேசான வெளிப்படைத்தன்மையுடன் கூடிய இளஞ்சிவப்பு */
        color: white;
        padding: 40px 20px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 30px;
        backdrop-filter: blur(10px); /* பின்னணியை மங்கலாக்கும் விளைவு */
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
    }

    /* Tabs (தாவல்கள்) வடிவமைப்பு */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        background-color: rgba(255, 255, 255, 0.9);
        padding: 10px;
        border-radius: 15px;
        justify-content: center;
    }

    .stTabs [data-baseweb="tab"] {
        color: #ec4899;
        font-weight: bold;
    }

    .stTabs [aria-selected="true"] {
        background-color: #fbcfe8 !important;
        border-radius: 10px;
    }

    /* உள்ளடக்கப் பகுதி (Cards) */
    .stMarkdown, .stTextInput, .stButton {
        background: rgba(255, 255, 255, 0.8);
        padding: 10px;
        border-radius: 15px;
    }

    /* பொத்தான்கள் */
    div.stButton > button {
        background: linear-gradient(135deg, #ec4899 0%, #be185d 100%);
        color: white;
        border-radius: 15px;
        border: none;
        font-weight: bold;
        transition: 0.3s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        color: white;
    }

    /* அடிக்குறிப்பு */
    .footer {
        text-align: center;
        padding: 20px;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        margin-top: 50px;
        color: #9d174d;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- தலைப்புப் பகுதி ---
st.markdown('<div class="main-title"><h1>📜 தொல்காப்பி ஆய்வி</h1><p>தமிழ் இலக்கண ஆய்வுத் தளம்</p></div>', unsafe_allow_html=True)

# 2. விதிகள் ஏற்றம் (Dynamic Loading)
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

# 3. உள்ளடக்க அமைப்பு
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
                st.success(f"**புணர்ச்சி முடிவு:** {res}")
            else:
                st.code(f"{n_mozhi} + {v_mozhi}")

# --- அடிக்குறிப்பு ---
st.markdown("""
    <div class="footer">
        मुனைவர் சத்தியராசு தங்கச்சாமி, பூபாலன் & குழுவினர்<br>
        <span style="font-size: 0.8rem; font-weight: normal;">தமிழ் இலக்கணத் தரவுத் தளம் | 2026</span>
    </div>
    """, unsafe_allow_html=True)
