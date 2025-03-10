from transformers import AutoTokenizer, AutoModelForCausalLM
from accelerate import Accelerator
import torch

# Load model and tokenizer
model_name = "ibm-granite/granite-3.0-1b-a400m-base"  # Replace with the correct model name or path
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Initialize accelerator (optional for performance optimization)
accelerator = Accelerator()

# Set device (GPU or CPU based on availability)
device = accelerator.device
model = model.to(device)

def generate_text(input_text: str) -> str:
    """Generate text from the model given an input text"""
    # Tokenize input and generate attention mask
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True).to(device)

    # Get the attention mask
    attention_mask = inputs['attention_mask']

    # Generate text with the attention mask
    outputs = model.generate(inputs['input_ids'], attention_mask=attention_mask, max_length=100)

    # Decode and return generated text
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
