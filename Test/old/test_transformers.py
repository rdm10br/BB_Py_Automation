from transformers import pipeline

# Load the text classification pipeline
classifier = pipeline("sentiment-analysis")

# Classify a single text
result = classifier("Transformers is a great library for NLP!")
print(result)
# Output: [{'label': 'POSITIVE', 'score': 0.999765932559967}]
# Output: [{'label': 'POSITIVE', 'score': 0.9992212057113647}]