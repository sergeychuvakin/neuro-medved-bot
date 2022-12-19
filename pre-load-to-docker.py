from config import Config

from transformers import (
    GPT2LMHeadModel,
    GPT2Tokenizer,
)

print("Downloading model binaries...")
tokenizer = GPT2Tokenizer.from_pretrained(Config.MODEL_HF_NAME)
model = GPT2LMHeadModel.from_pretrained(Config.MODEL_HF_NAME)
print("Done.")