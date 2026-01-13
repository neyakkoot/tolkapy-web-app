import streamlit as st
import importlib.util
import os

from tamilrulepy.meymayakkam import meymayakkam1,meymayakkam2,meymayakkam3,meymayakkam4,meymayakkam5,meymayakkam6,meymayakkam7,meymayakkam8,meymayakkam9,meymayakkam10,meymayakkam11,meymayakkam12,meymayakkam13,meymayakkam14,meymayakkam15,meymayakkam16,meymayakkam17,meymayakkam18

from tamilrulepy.mozhimarabu.word_starting import (
    uyirezhuthu_check,
    uyirmei_ka_check,
    uyirmei_ma_check,
    uyirmei_na_check,
    uyirmei_nga_check,
    uyirmei_pa_check,
    uyirmei_sa_check,
    uyirmei_ta_check,
    uyirmei_va_check,
    uyirmei_ya_check,
)


from tamilrulepy.mozhimarabu.word_ending import (
    uyir_check,
    mellinam_check,
    idaiyinam_check,
    alapedai_check,
    oorezhuthoorumozhi_check,
    suttu_check,
    vinaa_check,
)

from tamilrulepy.euphonic import get

# 1. பக்க வடிவமைப்பு
st.set_page_config(
    page_title="தொல்காபை ஆய்வி", 
    page_icon="📜",
    layout="wide"
    
)

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .block-container {
    padding-top: 0rem;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Mukta+Malar:wght@400;700&display=swap');
      
    /* ஒட்டுமொத்த பின்னணி மற்றும் எழுத்துரு */
    .stApp {
        background: linear-gradient(to bottom, #fdf2f8, #ffffff);
        font-family: 'Anek Tamil', sans-serif;
        font-weight: semibold;
    }

    /* தலைப்புப் பகுதி */
    .main-title-container {
        background: linear-gradient(135deg, #ec4899 0%, #be185d 100%);
        color: white !important;
        padding: 40px 30px;
        border-radius: 50px 50px 50px 50px;
        text-align: center;
        margin: 20px -20px 50px -20px;
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
        color: black !important;
    }

    /* All text elements to black */
    .stMarkdown, .stMarkdown p, .stMarkdown div, .stMarkdown span {
        color: black !important;
    }
            
    .stMarkdown h3 {
        color: black !important;
    }
    
    /* Subheader styling */
    h2, h3, h4, h5, h6 {
        color: black !important;
    }
    
    /* Text input labels */
    label, .stTextInput label {
        color: black !important;
    }
    
    /* Selectbox labels */
    .stSelectbox label {
        color: black !important;
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
    
    /* Center align button */
    div.stButton {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* கார்டு வடிவமைப்பு */
    .result-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ec4899;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-top: 20px;
        color: black !important;
    }

    .footer {
        text-align: center;
        padding: 30px;
        background: #fff;
        border-radius: 30px 30px 0 0;
        margin-top: 60px;
        color: black !important;
        border-top: 1px solid #fce7f3;
    }
    </style>
    """, unsafe_allow_html=True)

# --- தலைப்பு மற்றும் படம் (GitHub Raw Link) ---
image_url = "https://raw.githubusercontent.com/neyakkoot/tolkapy-web-app/main/images/%E0%AE%A4%E0%AF%8A%E0%AE%B2%E0%AF%8D%E0%AE%95%E0%AE%BE%E0%AE%AA%E0%AF%8D%E0%AE%AA%E0%AE%BF%E0%AE%AF%E0%AE%B0%E0%AF%8D.jpg"

st.markdown(f"""
    <div class="main-title-container">
        <img src="{image_url}" class="thol-image">
        <h1 style="margin: 0; font-size: 2.5rem; color: #FFFFFF">📜 தொல்காபை ஆய்வி</h1>
        <p style="opacity: 0.9; font-size: 1.1rem; color:#FFFFFF !important;">Tolkapy Grammar Analysis Tool</p>
    </div>
    """, unsafe_allow_html=True)


def rule1(option,word_m):
    all_rules = {
    "மெய்ம்மயக்கம்1 : 'க்+க'":  meymayakkam1,
    "மெய்ம்மயக்கம்2 : 'ங்+கங'":  meymayakkam2,
    "மெய்ம்மயக்கம்3 : 'ச்+ச'":  meymayakkam3,
    "மெய்ம்மயக்கம்4 : 'ஞ்+சஞய'":  meymayakkam4,
    "மெய்ம்மயக்கம்5 : 'ட்+கசடப'":  meymayakkam5,
    "மெய்ம்மயக்கம்6 : 'ண்+கசஞடணபமயவ'":  meymayakkam6,
    "மெய்ம்மயக்கம்7 : 'த்+த'":  meymayakkam7,
    "மெய்ம்மயக்கம்8 : 'ந்+தநய'":  meymayakkam8,
    "மெய்ம்மயக்கம்9 : 'ப்+ப'":  meymayakkam9, 
    "மெய்ம்மயக்கம்10 : 'ம்+பமயவ'":  meymayakkam10,
    "மெய்ம்மயக்கம்11 : 'ய்+கசதபஞநமயவங'":  meymayakkam11,
    "மெய்ம்மயக்கம்12 : 'ர்+கசதபஞநமயவங'":  meymayakkam12,
    "மெய்ம்மயக்கம்13 : 'ழ்+கசதபஞநமயவங'":  meymayakkam13,
    "மெய்ம்மயக்கம்14 : 'வ்+வ'":  meymayakkam14,
    "மெய்ம்மயக்கம்15 : 'ல்+கசபலயவ'":  meymayakkam15,
    "மெய்ம்மயக்கம்16 : 'ள்+கசபளயவ'":  meymayakkam16,
    "மெய்ம்மயக்கம்17 : 'ற்+கசபற'":  meymayakkam17,
    "மெய்ம்மயக்கம்18 : 'ன்+கசஞபமயவறன'":  meymayakkam18 
    }
    return all_rules[option](word_m)




def word_starting_checker(option,word):
    all_rules = {
        "உயிர் வரிசை" :uyirezhuthu_check,
        "க வரிசை" : uyirmei_ka_check,
        "ச வரிசை" : uyirmei_sa_check,
        "ஞ வரிசை" : uyirmei_nga_check,
        "த வரிசை" : uyirmei_ta_check,
        "ந வரிசை" : uyirmei_na_check,
        "ப வரிசை" : uyirmei_pa_check,
        "ம வரிசை" : uyirmei_ma_check,
        "ய வரிசை" : uyirmei_ya_check,
        "வ வரிசை" : uyirmei_va_check
    }
    return all_rules[option](word)



def word_ending_checker(option,word):
    all_rules = {
    "உயிர் சரிபார்ப்பு":uyir_check,
    "மெல்லினம் சரிபார்ப்பு":mellinam_check,
    "இடையினம் சரிபார்ப்பு":idaiyinam_check,
    "அளபெடை சரிபார்ப்பு":alapedai_check,
    "ஓரெழுத்து ஒருமொழி சரிபார்ப்பு":oorezhuthoorumozhi_check,
    "சுட்டு சரிபார்ப்பு":suttu_check,
    "வினா சரிபார்ப்பு":vinaa_check,
    }
    return all_rules[option](word)

def punarchi_result_formatter(res):
    if res:
        res1 = res[0][0]
    return res1



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
    col1, col2 = st.columns([2,2])
    with col1:
        word_m = st.text_input("சொல்லை உள்ளிடவும்:", key="m1", placeholder="எ.கா: கற்க")
    
    with col2:
        option = st.selectbox(  'விதியைத் தெரிவுசெய்க ',
            (
                "மெய்ம்மயக்கம்1 : 'க்+க'",
                "மெய்ம்மயக்கம்2 : 'ங்+கங'",
                "மெய்ம்மயக்கம்3 : 'ச்+ச'",
                "மெய்ம்மயக்கம்4 : 'ஞ்+சஞய'",
                "மெய்ம்மயக்கம்5 : 'ட்+கசடப'",
                "மெய்ம்மயக்கம்6 : 'ண்+கசஞடணபமயவ'",
                "மெய்ம்மயக்கம்7 : 'த்+த'",
                "மெய்ம்மயக்கம்8 : 'ந்+தநய'",
                "மெய்ம்மயக்கம்9 : 'ப்+ப'", 
                "மெய்ம்மயக்கம்10 : 'ம்+பமயவ'",
                "மெய்ம்மயக்கம்11 : 'ய்+கசதபஞநமயவங'",
                "மெய்ம்மயக்கம்12 : 'ர்+கசதபஞநமயவங'",
                "மெய்ம்மயக்கம்13 : 'ழ்+கசதபஞநமயவங'",
                "மெய்ம்மயக்கம்14 : 'வ்+வ'",
                "மெய்ம்மயக்கம்15 : 'ல்+கசபலயவ'",
                "மெய்ம்மயக்கம்16 : 'ள்+கசபளயவ'",
                "மெய்ம்மயக்கம்17 : 'ற்+கசபற'",
                "மெய்ம்மயக்கம்18 : 'ன்+கசஞபமயவறன'", 
                )
            )
    
    st.write("##")
    btn1 = st.button("ஆராய்க", key="b1")
        
    if btn1:
        rule_responce = rule1(option,word_m)
        if rule_responce:
            display_result(rule_responce)
        else:
            st.error(" இந்த விதியுடன் பொருந்தவில்லை. சரியான சொல்லை உள்ளிடவும். ")

with tab2:
    st.subheader("மொழிமுதல் எழுத்து ஆய்வு") 
   
    col1, col2 = st.columns([2,2])
    with col1:
        word_m = st.text_input("சொல்லை உள்ளிடவும்:", key="m2", placeholder="எ.கா: கற்க")
    
    with col2:
        option = st.selectbox(  'விதியைத் தெரிவுசெய்க ',
            (
            "உயிர் வரிசை",
            "க வரிசை",
            "ச வரிசை",
            "ஞ வரிசை",
            "த வரிசை",
            "ந வரிசை",
            "ப வரிசை",
            "ம வரிசை",
            "ய வரிசை",
            "வ வரிசை"  
            )
            
        )
    st.write("##")
    btn1 = st.button("ஆராய்க", key="b2")
        
    if btn1:
        rule_responce = word_starting_checker(option,word_m)
        if rule_responce:
            display_result(rule_responce)
        else:
            st.error(" இந்த விதியுடன் பொருந்தவில்லை. சரியான சொல்லை உள்ளிடவும். ")







with tab3:
    st.subheader("மொழியிறுதி எழுத்து ஆய்வு")

    col1, col2 = st.columns([2,2])
    with col1:
        word_m = st.text_input("சொல்லை உள்ளிடவும்:", key="m3", placeholder="எ.கா: கற்க")
    
    with col2:
        option = st.selectbox(  'விதியைத் தெரிவுசெய்க ',
            (
            "உயிர் சரிபார்ப்பு",
            "மெல்லினம் சரிபார்ப்பு",
            "இடையினம் சரிபார்ப்பு",
            "அளபெடை சரிபார்ப்பு",
            "ஓரெழுத்து ஒருமொழி சரிபார்ப்பு",
            "சுட்டு சரிபார்ப்பு",
            "வினா சரிபார்ப்பு",
            )
        )
    st.write("##")
    btn1 = st.button("ஆராய்க", key="b3")
        
    if btn1:
        if word_ending_checker:
            rule_responce = word_ending_checker(option,word_m)
            if rule_responce:
                display_result(rule_responce)
            else:
                st.error(" இந்த விதியுடன் பொருந்தவில்லை. சரியான சொல்லை உள்ளிடவும். ")
        else:
            st.warning("மொழியிறுதி ஆய்வுச் செயல்பாடு இன்னும் இணைக்கப்படவில்லை.")




with tab4:
    st.subheader("புணர்ச்சி ஆய்வு (Sandhi Analysis)")

    option = st.selectbox('எத்தனை சொற்கள் புணரப்படுகின்றன?', ('இரு சொற்கள்', 'மூன்று சொற்கள்'), key="sb1")

    if option == 'இரு சொற்கள்':
    
        c1, c2 = st.columns(2)
        with c1:
            n_mozhi = st.text_input("நிலைமொழி:", key="n1", placeholder="எ.கா: பனை")
        with c2:
            v_mozhi = st.text_input("வருமொழி:", key="v1", placeholder="எ.கா: காய்")
        
        if st.button("புணர்க்க", key="b4"):
            if get:
                res = get([n_mozhi, v_mozhi])
                res = punarchi_result_formatter(res)
                display_result(res, "புணர்ந்த வடிவம்")
            else:
                st.info(f"விதிகள் கிடைக்கவில்லை: {n_mozhi} + {v_mozhi}")

    elif option == 'மூன்று சொற்கள்':
    
        c1, c2, c3 = st.columns(3)
        with c1:
            n_mozhi = st.text_input("நிலைமொழி:", key="nilai", placeholder="எ.கா: பனை")
        with c2:
            m_mozhi = st.text_input("இரண்டாம் நிலைமொழி:", key="nadu", placeholder="எ.கா: காய்")
        with c3:
            v_mozhi = st.text_input("வருமொழி:", key="varu", placeholder="எ.கா: பழம்")
        
        if st.button("புணர்க்க", key="b5"):
            if get:
                res1 = get([n_mozhi, m_mozhi, v_mozhi])
                res1 = punarchi_result_formatter(res1)
                if res1:
                    display_result(res1, "புணர்ந்த வடிவம்")
            else:
                st.info(f"விதிகள் கிடைக்கவில்லை: {n_mozhi} + {m_mozhi} + {v_mozhi}")



# --- அடிக்குறிப்பு ---
st.markdown("""
    <div class="footer">
        <strong>மொழிவல்லுநர்:- முனைவர் சத்தியராசு தங்கச்சாமி</strong><br>
        <strong>தொழில்நுட்பவல்லுநர்:-  சு. பூபாலன், மு. வருண் & குழுவினர்</strong><br>
        <p style="margin-top:5px;">தொல்காப்பியம் உள்ளிட்ட தமிழ் இலக்கணத் தரவுத் தளம் | 2026</p>
    </div>
    """, unsafe_allow_html=True)




