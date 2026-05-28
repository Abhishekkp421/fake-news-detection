import streamlit as st
import pickle
from preprocess import clean_text

# Load saved model
model      = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Page config
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="🔍",
    layout="centered"
)

st.title("🔍 Fake News Detection System")
st.markdown("*Enter a news article or headline to check if it's real or fake.*")
st.divider()

# Input
news_text = st.text_area(
    "Paste news article here:",
    height=200,
    placeholder="Enter news text..."
)

if st.button("🔎 Analyze", use_container_width=True):
    if news_text.strip() == "":
        st.warning("Please enter some text first!")
    else:
        with st.spinner("Analyzing..."):
            cleaned   = clean_text(news_text)
            vectorized = vectorizer.transform([cleaned])
            prediction = model.predict(vectorized)[0]
            proba      = model.predict_proba(vectorized)[0]
            confidence = max(proba) * 100

        st.divider()

        if prediction == 1:
            st.error(f"❌ FAKE NEWS  —  Confidence: {confidence:.1f}%")
        else:
            st.success(f"✅ REAL NEWS  —  Confidence: {confidence:.1f}%")

        # Confidence bar
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Real probability",  f"{proba[0]*100:.1f}%")
        with col2:
            st.metric("Fake probability",  f"{proba[1]*100:.1f}%")

st.divider()
st.caption("Final Year Project | CSE AI/ML | Built with Python + Streamlit")