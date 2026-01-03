import streamlit as st
from tolkapy import meymayakkam
import importlib.util
import os

# 1. பக்க வடிவமைப்பு
st.set_page_config(
    page_title="தொல்காபை ஆய்வி", 
    page_icon="📜",
    layout="wide"
)

# --- நவீன வடிவமைப்பு (Custom CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Mukta+Malar:wght@400;700&display=swap');

    /* ஒட்டுமொத்த பின்னணி மற்றும் எழுத்துரு */
    .stApp {
        background: linear-gradient(to bottom, #fdf2f8, #ffffff);
        font-family: 'Mukta Malar', sans-serif;
    }

    /* தலைப்புப் பகுதி */
    .main-title-container {
        background: linear-gradient(135deg, #ec4899 0%, #be185d 100%);
        color: white;
        padding: 40px 20px;
        border-radius: 0px 0px 50px 50px;
        text-align: center;
        margin: -65px -20px 40px -20px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
    }

    .thol-image {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        border: 4px solid rgba(255, 255, 255, 0.8);
        object-fit: cover;
        margin-bottom: 15px;
        transition: transform 0.3s ease;
    }
    
    .thol-image:hover {
        transform: scale(1.05);
    }

    /* Tabs ஸ்டைல் */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 10px 20px;
        border-radius: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        border-radius: 10px;
        font-weight: bold;
    }

    /* இன்புட் மற்றும் பட்டன் வடிவமைப்பு */
    div.stButton > button {
        background: linear-gradient(135deg, #ec4899 0%, #be185d 100%);
        color: white;
        border-radius: 12px;
        border: none;
        padding: 10px 25px;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    div.stButton > button:hover {
        box-shadow: 0 5px 15px rgba(190, 24, 93, 0.4);
        transform: translateY(-2px);
    }

    /* கார்டு வடிவமைப்பு */
    .result-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ec4899;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-top: 20px;
    }

    .footer {
        text-align: center;
        padding: 30px;
        background: #fff;
        border-radius: 30px 30px 0 0;
        margin-top: 60px;
        color: #9d174d;
        border-top: 1px solid #fce7f3;
    }
    </style>
    """, unsafe_allow_html=True)

# --- தலைப்பு மற்றும் படம் (GitHub Raw Link) ---
image_url = "https://raw.githubusercontent.com/neyakkoot/tolkapy-web-app/main/images/%E0%AE%A4%E0%AF%8A%E0%AE%B2%E0%AF%8D%E0%AE%95%E0%AE%BE%E0%AE%AA%E0%AF%8D%E0%AE%AA%E0%AE%BF%E0%AE%AF%E0%AE%B0%E0%AF%8D.jpg"

st.markdown(f"""
    <div class="main-title-container">
        <img src="{image_url}" class="thol-image">
        <h1 style="margin: 0; font-size: 2.5rem;">📜 தொல்காபை ஆய்வி</h1>
        <p style="opacity: 0.9; font-size: 1.1rem;">Tolkapy Grammar Analysis Tool</p>
    </div>
    """, unsafe_allow_html=True)
res = meymayakkam.meymayakkam1(word_m)
# 3. பிரதான உள்ளடக்கப் பகுதி
tab1, tab2, tab3, tab4 = st.tabs([
    "🧩 மெய்ம்மயக்கம்", 
    "🏁 மொழிமுதல்", 
    "🔚 மொழியிறுதி", 
    "🔗 புணர்ச்சி"
])

def display_result(res, title="ஆய்வு முடிவு"):
    if res:
        st.markdown(f"""<div class="result-card"><strong>{title}:</strong><br>{res}</div>""", unsafe_allow_html=True)

with tab1:
    st.subheader("மெய்ம்மயக்கம் ஆய்வு")
    col1, col2 = st.columns([2, 1])
    with col1:
        word_m = st.text_input("சொல்லை உள்ளிடவும்:", key="m1", placeholder="எ.கா: கற்க")
    with col2:
        st.write("##")
        btn1 = st.button("ஆராய்க", key="b1", use_container_width=True)
        
    if btn1:
        display_result(res)
    else:
        st.error("இலக்கண விதியகம் (vidhikal.py) கண்டறியப்படவில்லை.")

with tab2:
    st.subheader("மொழிமுதல் எழுத்து ஆய்வு")
    word_f = st.text_input("சொல்லை உள்ளிடவும்:", key="f1", placeholder="எ.கா: தந்தை")
    if st.button("சரிபார்", key="b2"):
        if rules and hasattr(rules, 'mozhi_muthal_checker'):
            res = rules.mozhi_muthal_checker(word_f)
            display_result(res)
        else:
            st.warning("மொழிமுதல் ஆய்வுச் செயல்பாடு இன்னும் இணைக்கப்படவில்லை.")

with tab3:
    st.subheader("மொழியிறுதி எழுத்து ஆய்வு")
    word_e = st.text_input("சொல்லை உள்ளிடவும்:", key="e1", placeholder="எ.கா: மரம்")
    if st.button("சரிபார்", key="b3"):
        if rules and hasattr(rules, 'mozhi_iruthi_checker'):
            res = rules.mozhi_iruthi_checker(word_e)
            display_result(res)
        else:
            st.warning("மொழியிறுதி ஆய்வுச் செயல்பாடு இன்னும் இணைக்கப்படவில்லை.")

with tab4:
    st.subheader("புணர்ச்சி ஆய்வு (Sandhi Analysis)")
    c1, c2 = st.columns(2)
    with c1:
        n_mozhi = st.text_input("நிலைமொழி:", key="n1", placeholder="எ.கா: பனை")
    with c2:
        v_mozhi = st.text_input("வருமொழி:", key="v1", placeholder="எ.கா: காய்")
    
    if st.button("புணர்க்க", key="b4"):
        if rules and hasattr(rules, 'punarchi_checker'):
            res = rules.punarchi_checker(n_mozhi, v_mozhi)
            display_result(res, "புணர்ந்த வடிவம்")
        else:
            st.info(f"விதிகள் கிடைக்கவில்லை: {n_mozhi} + {v_mozhi}")

# --- அடிக்குறிப்பு ---
st.markdown("""
    <div class="footer">
        <strong>முனைவர் சத்தியராசு தங்கச்சாமி, பூபாலன் & குழுவினர்</strong><br>
        <p style="margin-top:5px;">தமிழ் இலக்கணத் தரவுத் தளம் | 2026</p>
    </div>
    """, unsafe_allow_html=True)
