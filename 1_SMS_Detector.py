import streamlit as st
import joblib

model = joblib.load("spam_classifier_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.title("📩 SMS Spam Classifier")
user_input = st.text_area("Enter the message to classify 👇:")

if st.button("Predict 🤔"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        transformed_text = vectorizer.transform([user_input])
        prediction = model.predict(transformed_text)[0]
        
        if prediction == 1:
            st.error("🚫 This message is **SPAM**.")
        else:
            st.success("✅ This message is **NOT SPAM**.")
st.markdown("---")
if st.button("🔙 Back to Home"):
    st.switch_page("app.py")