import streamlit as st
from transformers import pipeline

# Load model
@st.cache_resource  # prevents reloading on every run
def load_model():
    return pipeline("sentiment-analysis")

sentiment_pipeline = load_model()

# UI
st.title("Sentiment Analysis Web App")
st.write("Classify text as Positive / Negative")

user_input = st.text_area("Enter text here:")

if st.button("Analyze"):
    if user_input.strip() != "":
        result = sentiment_pipeline(user_input)[0]
        st.write(f"**Label:** {result['label']}")
        st.write(f"**Score:** {result['score']:.2f}")
    else:
        st.warning(" Please enter some text.")
