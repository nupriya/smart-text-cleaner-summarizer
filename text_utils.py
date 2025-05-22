# text_utils.py

import re
import nltk
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize

# ✅ Explicitly download 'punkt' tokenizer for NLTK
nltk.download("punkt", quiet=True)

def is_arabic(text):
    return any('\u0600' <= c <= '\u06FF' or '\u0750' <= c <= '\u077F' for c in text)

def arabic_sent_tokenize(text):
    sentences = re.split(r'(?<=[؟.!؛])\s+', text)
    return [s.strip() for s in sentences if s.strip()]

def clean_text(text):
    text = BeautifulSoup(text, "html.parser").get_text()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s.,!?؛،ءاأإآ-ي]', '', text)
    return text.strip()

def remove_duplicates(text):
    if is_arabic(text):
        sentences = arabic_sent_tokenize(text)
    else:
        sentences = sent_tokenize(text)

    seen = set()
    unique_sentences = []
    for s in sentences:
        s_clean = s.strip().lower()
        if s_clean not in seen:
            seen.add(s_clean)
            unique_sentences.append(s)
    return " ".join(unique_sentences)
