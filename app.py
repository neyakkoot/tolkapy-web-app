import streamlit as st
import tamilrulepy
import pkgutil

st.set_page_config(page_title="தொல்காப்பி", page_icon="📜")
st.title("📜 தொல்காப்பி (Tolkapy)")
st.subheader("தமிழ் இலக்கண விதி சரிபார்ப்பான்")

# நூலகத்திற்குள் இருக்கும் சப்-மாடுயூல்களைத் தேடுதல்
package = tamilrulepy
sub_modules = [name for _, name, _ in pkgutil.iter_modules(package.__path__)]

# 'vidhikal' அல்லது அது போன்ற கோப்பு இருக்கிறதா எனப் பார்த்தல்
module_to_use = None
if 'vidhikal' in sub_modules:
    import tamilrulepy.vidhikal as vidhikal
    module_to_use = vidhikal
elif len(sub_modules) > 0:
    # முதல் மாடுயூலை எடுத்து முயற்சிப்போம் (எ.கா: rules)
    module_to_use = __import__(f"tamilrulepy.{sub_modules[0]}", fromlist=[''])

word = st.text_input("தமிழ் சொல்லை உள்ளிடவும்:", "தமிழ்")

if st.button("சரிபார்"):
    if word:
        try:
            if module_to_use:
                # 'tamil_word_checker' அல்லது 'validate' போன்ற சார்புகளைத் தேடுதல்
                funcs = dir(module_to_use)
                
                if 'tamil_word_checker' in funcs:
                    result = module_to_use.tamil_word_checker(word)
                    st.success(f"முடிவு: {result}")
                elif 'check_word' in funcs:
                    result = module_to_use.check_word(word)
                    st.success(f"முடிவு: {result}")
                else:
                    st.warning("மாடுயூல் கண்டறியப்பட்டது, ஆனால் சரியான சார்பு பெயர் இல்லை.")
                    st.write("கிடைக்கக்கூடிய சார்புகள்:", [f for f in funcs if not f.startswith('_')])
            else:
                st.error("இலக்கண விதிகள் அடங்கிய கோப்பு (Sub-module) எதுவும் கண்டறியப்படவில்லை.")
                st.write("உள்ளே இருக்கும் கோப்புகள்:", sub_modules)
                
        except Exception as e:
            st.error(f"பிழை: {e}")
    else:
        st.info("தயவுசெய்து ஒரு சொல்லை உள்ளிடவும்.")

st.divider()
st.caption("நன்றி: கணியம் அறக்கட்டளை")
