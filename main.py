# Import necessary modules and classes
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
import torch
import time

# Define available models and their label mappings
MODEL_IDS = {
    'Fake-News-Bert-Detect': 'jy46604790/Fake-News-Bert-Detect',
    'Albert-Base-v2-Fakenews-Discriminator': 'XSY/albert-base-v2-fakenews-discriminator',
    'Roberta-Fake-News-Classification': 'hamzab/roberta-fake-news-classification'
}

LABEL_MAPPINGS = {
    'Fake-News-Bert-Detect': {0: "fake", 1: "true"},
    'Albert-Base-v2-Fakenews-Discriminator': {0: "fake", 1: "true"},
    'Roberta-Fake-News-Classification': {0: "fake", 1: "true"}
}

# Load a specific model and tokenizer
def load_model(model_name):
    model_id = MODEL_IDS[model_name]
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSequenceClassification.from_pretrained(model_id)
    return model, tokenizer

# Define a function to generate AI responses based on the given query and selected model
def genai_engine(query, model_name):
    model, tokenizer = load_model(model_name)
    start_time = time.time()
    # Tokenize input text
    inputs = tokenizer(query, return_tensors="pt")
    # Get model outputs
    outputs = model(**inputs)
    # Get logits and probabilities
    logits = outputs.logits
    probabilities = torch.nn.functional.softmax(logits, dim=-1)
    # Get predicted label
    predicted_label = torch.argmax(probabilities, dim=-1).item()
    # Get confidence scores
    confidence_scores = probabilities[0].tolist()
    
    # Ensure labels are correctly mapped
    labels = LABEL_MAPPINGS[model_name]  # Get label mapping
    predicted_label_name = labels[predicted_label]

    reasoning = f"Model '{model_name}' predicted the text as '{predicted_label_name}' with confidence scores: {confidence_scores}"

    end_time = time.time()
    processing_time = end_time - start_time
    response = predicted_label_name
    return response, reasoning, processing_time
