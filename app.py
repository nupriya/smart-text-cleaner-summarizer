# app.py

import streamlit as st
from text_utils import clean_text, remove_duplicates
from summarizer import summarize_text

st.set_page_config(page_title="Smart Text Cleaner & Summarizer", layout="wide")
st.title("🧠 Smart Text Cleaner & Summarizer")
st.markdown("Supports both **Arabic** and **English** input text.")

text_input = st.text_area("📄 Paste your raw text here:", height=300)
lang_option = st.radio("🌍 Select Language of Input", ["English", "Arabic"])
lang_code = "ar" if lang_option == "Arabic" else "en"

if st.button("🚀 Process"):
    if text_input.strip():
        cleaned = clean_text(text_input)
        deduped = remove_duplicates(cleaned)
        summary = summarize_text(deduped, lang=lang_code)

        st.subheader("🧹 Cleaned Text")
        st.write(deduped)

        st.subheader("📝 Summary")
        for point in summary:
            st.markdown(point)
    else:
        st.warning("Please paste some text to process.")
