!pip install datasets transformers torch accelerate

import torch
from transformers import Trainer, TrainingArguments, GPT2LMHeadModel, GPT2Tokenizer
from datasets import load_dataset

# ✅ Load pre-trained DistilGPT2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained("distilgpt2")
tokenizer = GPT2Tokenizer.from_pretrained("distilgpt2")

# ✅ Ensure the tokenizer has a padding token
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# ✅ Load and preprocess the dataset efficiently (for large dataset handling)
dataset = load_dataset("text", data_files={"train": "formatted_honeytokens.txt"}, split="train")

# ✅ Tokenization function
def tokenize_function(examples):
    tokenized_inputs = tokenizer(examples["text"], truncation=True, padding="max_length", max_length=64)
    tokenized_inputs["labels"] = tokenized_inputs["input_ids"].copy()
    return tokenized_inputs

# ✅ Tokenize dataset
tokenized_datasets = dataset.map(tokenize_function, batched=True, remove_columns=["text"])

# ✅ Move model to GPU (if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# ✅ Training arguments (Optimized for large datasets)
training_args = TrainingArguments(
    output_dir="./fine_tuned_gpt2",
    per_device_train_batch_size=16,  # Reduce batch size for memory efficiency
    gradient_accumulation_steps=4,  # Helps manage GPU memory
    num_train_epochs=10,  # Increase epochs for better training
    fp16=True,  # Mixed precision for faster training
    save_strategy="no",
    logging_steps=100,
    report_to="none",
    dataloader_pin_memory=True,
    dataloader_num_workers=4,
)

# ✅ Trainer setup
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets,
    tokenizer=tokenizer,
)

# ✅ Check GPU availability
print("Checking GPU availability:")
!nvidia-smi

# ✅ Start training
trainer.train()

# ✅ Save trained model and tokenizer
model.save_pretrained("./fine_tuned_gpt2")
tokenizer.save_pretrained("./fine_tuned_gpt2")

print("✅ Model and tokenizer saved successfully!")
