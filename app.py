import streamlit as st
import tamilrulepy
import importlib.util
import os

# 1. vidhikal.py கோப்பைத் தேடி இறக்குதல் (Dynamic Loading)
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

# 2. பக்க வடிவமைப்பு
st.set_page_config(page_title="தொல்காப்பி ஆய்வு", layout="wide")
st.title("📜 Tolkapy (தொல்காப்பி)")

tab1, tab2, tab3, tab4 = st.tabs(["மெய்ம்மயக்கம்", "மொழிமுதல்", "மொழியிறுதி", "புணர்ச்சி"])

# --- TAB 1: மெய்ம்மயக்கம் ---
with tab1:
    st.header("மெய்ம்மயக்கம் ஆய்வு")
    word_m = st.text_input("சொல்லை உள்ளிடவும்:", key="m1")
    if st.button("ஆராய்க", key="b1"):
        if rules and hasattr(rules, 'meymayakkam_checker'):
            res = rules.meymayakkam_checker(word_m)
            st.success(f"முடிவு: {res}")

# --- TAB 2: மொழிமுதல் (சிக்கல் 1 தீர்வு) ---
with tab2:
    st.header("மொழிமுதல் ஆய்வு")
    word_f = st.text_input("சொல்லை உள்ளிடவும்:", key="f1")
    if st.button("சரிபார்", key="b2"):
        if rules and hasattr(rules, 'mozhi_muthal_checker'):
            res = rules.mozhi_muthal_checker(word_f)
            st.info(f"ஆய்வு முடிவு: {res}")
        else:
            st.warning("மொழிமுதல் விதிச் செயல்பாடுகள் கண்டறியப்படவில்லை.")

# --- TAB 3: மொழியிறுதி (சிக்கல் 2 தீர்வு) ---
with tab3:
    st.header("மொழியிறுதி ஆய்வு")
    word_e = st.text_input("சொல்லை உள்ளிடவும்:", key="e1")
    if st.button("சரிபார்", key="b3"):
        if rules and hasattr(rules, 'mozhi_iruthi_checker'):
            res = rules.mozhi_iruthi_checker(word_e)
            st.info(f"ஆய்வு முடிவு: {res}")
        else:
            st.warning("மொழியிறுதி விதிச் செயல்பாடுகள் கண்டறியப்படவில்லை.")

# --- TAB 4: புணர்ச்சி (சிக்கல் 3 தீர்வு) ---
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
            # நூலகத்தில் புணர்ச்சி விதி இல்லை எனில் ஒரு எளிய மாதிரி
            st.code(f"{n_mozhi} + {v_mozhi}")
            st.write("குறிப்பு: நூலகத்தில் புணர்ச்சி விதிகள் மேம்படுத்தப்படுகின்றன.")

st.divider()
st.caption("முனைவர் சத்தியராசு தங்கச்சாமி & குழுவினர் | ")
