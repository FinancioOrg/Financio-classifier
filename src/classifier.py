from transformers import pipeline

def classify_article(text, categories):
    pipe = pipeline(model="facebook/bart-large-mnli")
    result = pipe(text,candidate_labels=categories)
    return result