import streamlit as st

# -------------------------------------------------
# 1. நூலக இறக்குமதி (Library Import)
# -------------------------------------------------
try:
    import tamilrulepy
    from tamilrulepy.meymayakkam import (
        meymayakkam1, meymayakkam2, meymayakkam3, meymayakkam4, meymayakkam5,
        meymayakkam6, meymayakkam7, meymayakkam8, meymayakkam9, meymayakkam10,
        meymayakkam11, meymayakkam12, meymayakkam13, meymayakkam14, meymayakkam15,
        meymayakkam16, meymayakkam17, meymayakkam18
    )
    
    # விதிகளை ஒரு பட்டியலில் சேர்த்தல்
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
st.set_page_config(page_title="Tolkapy - மெய்ம்மயக்கம் ஆய்வு", layout="centered")

st.title("📜 Tolkapy")
st.subheader("தொல்காப்பிய மெய்ம்மயக்கம் ஆய்வு")

if not status:
    st.error(f"❌ நூலகத்தை ஏற்ற முடியவில்லை: {error_msg}")
    st.info("requirements.txt கோப்பில் `git+https://gitlab.com/kachilug/tamilrulepy.git` உள்ளதா என உறுதி செய்யவும்.")
    st.stop()

# -------------------------------------------------
# 3. பயனர் உள்ளீடு
# -------------------------------------------------
word = st.text_input("தமிழ் சொல்லை உள்ளிடவும்", placeholder="உதா: தங்கம்")

if st.button("🔍 விதிகளின்படி ஆராய்க"):
    if not word.strip():
        st.warning("⚠️ தயவுசெய்து ஒரு சொல்லை உள்ளிடவும்")
    else:
        st.write(f"### '{word}' - ஆய்வு முடிவுகள்:")
        
        results_found = False
        
        # 18 விதிகளையும் சரிபார்த்தல்
        for i, rule_func in enumerate(meymayakkam_rules, 1):
            try:
                res = rule_func(word)
                if res: # விதி பொருந்தினால்
                    st.success(f"✅ **விதி {i}:** பொருந்துகிறது")
                    st.info(f"விளக்கம்: {res}")
                    results_found = True
            except:
                continue
        
        if not results_found:
            st.warning("❌ இந்தச் சொல் மெய்ம்மயக்க விதிகளுக்கு உட்பட்டதாகத் தெரியவில்லை.")

st.divider()
st.caption("முனைவர் சத்தியராசு தங்கச்சாமி & பூபாலன் | tamilrulepy project")
