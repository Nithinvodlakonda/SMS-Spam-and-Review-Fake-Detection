import joblib
import streamlit as st

vectorizer = joblib.load('tfidf_vectorizer_review.pkl')
model = joblib.load('review_fake_detection_model.pkl')

st.title("🕵️‍♂️ Review Fake Detection 🔍")
input_text = st.text_area("📝 Enter Review Text here👇:")

if st.button("Detect🕵️‍♀️"):
    if input_text.strip() == "":
        st.warning("Please enter a Review.")
    else:
        transformed_text = vectorizer.transform([input_text])
        prediction = model.predict(transformed_text)[0]
        
        if prediction == 1:
            st.success("✅ This review appears to be **human-written** and authentic.")
        else:
            st.warning("⚠️ This review appears to be **computer-generated** or fake.")
st.markdown("---")
if st.button("🔙 Back to Home"):
    st.switch_page("app.py")
