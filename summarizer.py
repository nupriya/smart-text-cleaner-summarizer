# summarizer.py

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Use mT5 multilingual model that supports Arabic and English
model_name = "csebuetnlp/mT5_multilingual_XLSum"

# ✅ Use slow tokenizer for SentencePiece compatibility
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def summarize_text(text, lang="en"):
    prefix_map = {
        "en": "summarize: ",
        "ar": "تلخيص: "
    }
    prefix = prefix_map.get(lang, "summarize: ")
    input_text = prefix + text

    inputs = tokenizer.encode(
        input_text,
        return_tensors="pt",
        max_length=512,
        truncation=True
    )

    summary_ids = model.generate(
        inputs,
        max_length=100,
        min_length=30,
        do_sample=False
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return [f"- {line.strip()}" for line in summary.split(". ") if line.strip()]
