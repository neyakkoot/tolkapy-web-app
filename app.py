import streamlit as st

# -----------------------------------
# Page Config
# -----------------------------------
st.set_page_config(
    page_title="Tolkapy | தொல்காப்பிய ஆய்வு",
    page_icon="📜",
    layout="centered"
)

# -----------------------------------
# CSS
# -----------------------------------
st.markdown("""
<style>
.title {
    font-size: 32px;
    font-weight: 700;
    color: #4b2e1e;
    text-align: center;
}
.subtitle {
    font-size: 17px;
    text-align: center;
    color: #6b4b3e;
}
.card {
    background-color: #fffaf3;
    padding: 18px;
    border-radius: 12px;
    border-left: 6px solid #b08968;
    box-shadow: 0 4px 8px rgba(0,0,0,0.08);
}
.footer {
    text-align: center;
    color: #777;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# Sidebar
# -----------------------------------
st.sidebar.title("📚 தொல்காப்பிய ஆய்வு")
st.sidebar.markdown("""
இந்த கருவி தொல்காப்பிய  
**எழுத்தியல் & சொல்லியல் விதிகளை**  
Python மூலம் ஆராய உதவுகிறது.
""")

st.sidebar.markdown("### 🔍 ஆய்வு விதிகள்")
st.sidebar.markdown("""
• மெய்ம்மயக்கம்  
• மொழிமுதல்  
• மொழியிறுதி  
• புணர்ச்சி  
""")

# -----------------------------------
# Title
# -----------------------------------
st.markdown('<div class="title">📜 Tolkapy</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">தொல்காப்பிய விதி ஆய்வுக் கருவி</div>', unsafe_allow_html=True)
st.write("")

# -----------------
