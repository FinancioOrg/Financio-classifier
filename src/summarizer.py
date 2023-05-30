from transformers import pipeline

def summarize_article(sum_pipeline, text):
    result = sum_pipeline(text)
    print(result)
    return result