import streamlit as st
import importlib.util
import os
import tamilrulepy

# 1. பக்க வடிவமைப்பு
st.set_page_config(page_title="தொல்காப்பி - மெய்மயக்கம்", page_icon="📜")

# 2. vidhikal.py கோப்பைத் தேடி இறக்குதல் (Fixing the sub-module issue)
def get_vidhikal():
    try:
        # tamilrulepy ஃபோல்டர் எங்கே இருக்கிறது என்று கண்டுபிடிக்கிறோம்
        base_path = os.path.dirname(tamilrulepy.__file__)
        vidhikal_path = os.path.join(base_path, "vidhikal.py")
        
        # அந்த கோப்பை ஒரு மாடுயூலாக ஏற்றுகிறோம்
        spec = importlib.util.spec_from_file_location("vidhikal", vidhikal_path)
        vidhikal_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(vidhikal_module)
        return vidhikal_module
    except Exception as e:
        return None

rules = get_vidhikal()

# 3. பயனர் இடைமுகம்
st.title("📜 தொல்காப்பி (Tolkapy)")
st.subheader("தமிழ் மெய்மயக்கம் விதி சரிபார்ப்பான்")

if rules:
    st.success("✅ தொல்காப்பிய விதிகள் வெற்றிகரமாக இணைக்கப்பட்டன!")
    
    word = st.text_input("சரிபார்க்க வேண்டிய தமிழ் சொல்லை உள்ளிடவும்:", "தமிழ்")

    if st.button("சரிபார்"):
        if word:
            try:
                # நாம் கண்டறிந்த 'meymayakkam_checker' சார்பை அழைக்கிறோம்
                if hasattr(rules, 'meymayakkam_checker'):
                    result = rules.meymayakkam_checker(word)
                    
                    if result == True or str(result).strip().lower() == "true":
                        st.balloons()
                        st.success(f"✅ '{word}' - மெய்மயக்கம் விதிகளின்படி சரியான சொல்.")
                    else:
                        st.warning(f"⚠️ ஆய்வு முடிவு: {result}")
                else:
                    st.error("சார்பு (meymayakkam_checker) கோப்பில் இல்லை.")
                    st.write("கோப்பில் உள்ளவை:", [f for f in dir(rules) if not f.startswith('_')])
            except Exception as e:
                st.error(f"ஆய்வு செய்வதில் பிழை: {e}")
else:
    st.error("❌ 'vidhikal.py' கோப்பைக் கண்டறிய முடியவில்லை. நூலக அமைப்பைச் சரிபார்க்கவும்.")

st.divider()
st.caption("வழங்குபவர்: கணியம் அறக்கட்டளை & Tolkapy குழுவினர்")
