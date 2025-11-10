from transformers import pipeline

def generate_summary(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    if len(text.split()) < 30:
        text += " " + text
    summary = summarizer(text, max_length=60, min_length=20, do_sample=False)
    return summary[0]['summary_text']
