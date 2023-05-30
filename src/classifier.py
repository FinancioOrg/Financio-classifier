from transformers import pipeline
from categoriesDAL import fetch_categories

def classify_article(text):
    categories = fetch_categories()
    pipe = pipeline("zero-shot-classification", model="roberta-large-mnli", device='cpu')
    result = pipe(text,candidate_labels=categories)
    print(result)
    return result


# from transformers import pipeline
# from categoriesDAL import fetch_categories

# def classify_article(text):
#     categories = fetch_categories()
#     print(categories)
#     pipe = pipeline(model="facebook/bart-large-mnli")
#     result = pipe(text,candidate_labels=categories)
#     return result