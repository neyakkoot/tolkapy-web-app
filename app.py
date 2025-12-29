import streamlit as st

# -------------------------------------------------
# 1. நூலக இறக்குமதி மற்றும் விதிகள் அமைப்பு
# -------------------------------------------------
try:
    import tamilrulepy
    from tamilrulepy import vidhikal
    from tamilrulepy.meymayakkam import (
        meymayakkam1, meymayakkam2, meymayakkam3, meymayakkam4, meymayakkam5,
        meymayakkam6, meymayakkam7, meymayakkam8, meymayakkam9, meymayakkam10,
        meymayakkam11, meymayakkam12, meymayakkam13, meymayakkam14, meymayakkam15,
        meymayakkam16, meymayakkam17, meymayakkam18
    )
    
    meymayakkam_rules = [
        meymayakkam1, meymayakkam2, meymayakkam3, meymayakkam4, meymayakkam5,
        meymayakkam6, meymayakkam7, meymayakkam8, meymayakkam9, meymayakkam10,
        meymayakkam11, meymayakkam12, meymayakkam13, meymayakkam14, meymayakkam15,
        meymayakkam16, meymayakkam17, meymayakkam18
    ]
    status = True
except Exception as e:
    status = False
    error_msg = str(e)

# -------------------------------------------------
# 2. பக்க வடிவமைப்பு
# -------------------------------------------------
st.set_page_config(page_title="Tolkapy - முழுமையான ஆய்வு", layout="wide")

st.title("📜 Tolkapy (தொல்காப்பி)")
st.subheader("தொல்காப்பிய இலக்கண ஆய்வு மையம்")
st.divider()

if not status:
    st.error(f"❌ பிழை: {error_msg}")
    st.stop()

# -------------------------------------------------
# 3. பக்கவாட்டுப் பட்டி (ஆய்வு வகை தெரிவு)
# -------------------------------------------------
with st.sidebar:
    st.header("🔍 ஆய்வு வகை")
    mode = st.radio(
        "தேர்வு செய்க:",
        ["மெய்ம்மயக்கம்", "மொழிமுதல் & இறுதி", "புணர்ச்சி ஆய்வு"]
    )
    st.info("தொல்காப்பிய எழுத்ததிகார விதிகளின் அடிப்படையில் இந்த ஆய்வு அமைகிறது.")

# -------------------------------------------------
# 4. ஆய்வுப் பகுதிகள்
# -------------------------------------------------

# --- மெய்ம்மயக்கம் ---
if mode == "மெய்ம்மயக்கம்":
    st.header("🧩 மெய்ம்மயக்கம் ஆய்வு")
    word = st.text_input("சொல்லை உள்ளிடவும்:", placeholder="உதா: கற்றல்")
    
    if st.button("ஆராய்க"):
        if word:
            results = []
            for i, rule in enumerate(meymayakkam_rules, 1):
                try:
                    res = rule(word)
                    if res: results.append(f"விதி {i}: {res}")
                except: continue
            
            if results:
                for r in results: st.success(r)
            else:
                st.warning("எந்த மெய்ம்மயக்க விதியும் பொருந்தவில்லை.")

# --- மொழிமுதல் & மொழியிறுதி ---
elif mode == "மொழிமுதல் & இறுதி":
    st.header("📍 மொழிமுதல் & மொழியிறுதி ஆய்வு")
    word = st.text_input("சொல்லை உள்ளிடவும்:", placeholder="உதா: அம்மா")
    
    col1, col2 = st.columns(2)
    
    if st.button("ஆய்வு செய்க"):
        with col1:
            st.subheader("மொழிமுதல்")
            try:
                # vidhikal-ல் mozhi_muthal_checker இருப்பதாகக் கொண்டு:
                muthal_res = vidhikal.mozhi_muthal_checker(word)
                st.info(muthal_res if muthal_res else "விதிக்கு உட்பட்டது")
            except: st.write("தகவல் இல்லை")
            
        with col2:
            st.subheader("மொழியிறுதி")
            try:
                # vidhikal-ல் mozhi_iruthi_checker இருப்பதாகக் கொண்டு:
                iruthi_res = vidhikal.mozhi_iruthi_checker(word)
                st.info(iruthi_res if iruthi_res else "விதிக்கு உட்பட்டது")
            except: st.write("தகவல் இல்லை")

# --- புணர்ச்சி ஆய்வு ---
elif mode == "புணர்ச்சி ஆய்வு":
    st.header("🔗 புணர்ச்சி (Sandhi) ஆய்வு")
    c1, c2 = st.columns(2)
    nilaichol = c1.text_input("நிலைமொழி:", placeholder="உதா: பல")
    varuchol = c2.text_input("வருமொழி:", placeholder="உதா: சில")
    
    if st.button("புணர்க்க"):
        if nilaichol and varuchol:
            try:
                # punarchi_checker செயல்பாட்டை அழைத்தல்
                punarchi_res = vidhikal.punarchi_checker(nilaichol, varuchol)
                st.success(f"முடிவு: {punarchi_res}")
            except Exception as e:
                st.error(f"புணர்ச்சி ஆய்வில் பிழை: {e}")

# -------------------------------------------------
# 5. அடிக்குறிப்பு
# -------------------------------------------------
st.divider()
st.caption("வழங்குபவர்: முனைவர் சத்தியராசு தங்கச்சாமி | [Source Code](https://gitlab.com/kachilug/tamilrulepy)")
