import langchain
import transformers
import torch
import os

model_id = "google/gemma-3-4b-it"

llm = langchain.llm.pipeline.LLM(
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

llm.invoke("Hello, how are you?")