import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# ✅ Load the fine-tuned model and tokenizer from files
model_path = "./fine_tuned_gpt2"  # Path where files are stored

model = GPT2LMHeadModel.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_path)

# ✅ Move model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# ✅ Set model to evaluation mode
model.eval()

# Generate example text using the model
input_text = "Generate honeytoken related event:"
input_ids = tokenizer.encode(input_text, return_tensors="pt").to(device)

with torch.no_grad():
    generated_ids = model.generate(input_ids, max_length=50, num_return_sequences=1)

generated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
print(f"Generated Text: {generated_text}")
