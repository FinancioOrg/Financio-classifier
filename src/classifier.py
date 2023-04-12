from transformers import pipeline
from categoriesDAL import fetch_categories

def classify_article(text):
    categories = fetch_categories()
    pipe = pipeline(model="facebook/bart-large-mnli")
    result = pipe(text,candidate_labels=categories)
    print(result)
    return result