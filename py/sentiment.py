from transformers import pipeline

nlp = pipeline("sentiment-analysis")

result = nlp("I hate you")[0]
print(f"label: {result['label']}, with score: {round(result['score'], 4)}")

result = nlp("I love you")[0]
print(f"label: {result['label']}, with score: {round(result['score'], 4)}")
