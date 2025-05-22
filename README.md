# smart-text-cleaner-summarizer
# 🧠 Smart Text Cleaner & Summarizer

A simple multilingual Streamlit app that:
- 🧹 Cleans messy raw text (HTML, OCR, etc.)
- 🔁 Removes duplicate sentences
- 📝 Summarizes content (English + Arabic)

## 🌐 Features
- Clean text using regex and BeautifulSoup
- Sentence deduplication with Arabic-aware tokenizer
- Summarization via multilingual mT5 (`csebuetnlp/mT5_multilingual_XLSum`)
- Streamlit interface

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
