import streamlit as st

st.set_page_config(page_title="Text Classifier", layout="centered")

st.title("🧠 Text Classification Hub")
st.write("Choose what you want to analyze")

col1, col2 = st.columns(2)

with col1:
    if st.button("📩 SMS Spam Detection"):
        st.switch_page("pages/1_SMS_Detector.py")  

with col2:
    if st.button("🛍️ Fake Review Detection"):
        st.switch_page("pages/2_Review_Detector.py")


st.markdown('<div class="footer">🚀 Built with ❤️ by Nithin | SMS & Review Classification System using ML</div>', unsafe_allow_html=True)
