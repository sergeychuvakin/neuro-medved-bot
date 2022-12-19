from config import Config

from transformers import (
    GPT2LMHeadModel,
    GPT2Tokenizer,
    pipeline
)

print("Downloading model binaries...")
tokenizer = GPT2Tokenizer.from_pretrained(Config.MODEL_HF_NAME)
model = GPT2LMHeadModel.from_pretrained(Config.MODEL_HF_NAME)
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
pipe.save_pretrained(Config.MODEL_LOCAL_PATH)
print("Done.")