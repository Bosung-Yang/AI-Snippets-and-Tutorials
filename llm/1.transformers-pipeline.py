import langchain
import transformers
import torch
import os

model_id = "google/gemma-3-4b-it"

pipe = transformers.pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

# transformers pipline example
prompt = "Hello, how are you?"
response = pipe(prompt, max_length=100)
