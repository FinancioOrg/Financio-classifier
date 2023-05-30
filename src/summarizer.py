from transformers import pipeline

def summarize_article(text):
    sum_pipeline = pipeline("summarization",model="sshleifer/distilbart-cnn-12-6", device='cpu')
    result = sum_pipeline(text)
    print(result)
    return result