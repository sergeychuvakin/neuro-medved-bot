import os

import numpy as np
import torch
from tqdm import tqdm
from transformers import (
    GPT2LMHeadModel,
    GPT2Tokenizer,
)

from config import Config

device = torch.device("cpu")

print("Downloading model binaries...")
tokenizer = GPT2Tokenizer.from_pretrained(Config.MODEL_LOCAL_PATH, local_files_only=True)
model = GPT2LMHeadModel.from_pretrained(Config.MODEL_LOCAL_PATH, local_files_only=True)
print("Done.")

def generate_n_words(lenght_of_sentence, start_sentence, device):

    n = 5  ## top for random choice

    model_path = os.path.join(
        Config.MODELS_FOLDER, Config.MODEL_STORE_NAME.format(Config.MODEL_EPOCH)
    )
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))

    model.eval()
    model.to(device)

    cur_ids = torch.tensor(tokenizer.encode(start_sentence)).unsqueeze(0).to(device)
    
    print("Text generation...")

    for _ in tqdm(range(lenght_of_sentence)):
        outputs = model(cur_ids, labels=cur_ids)

        _, logits = outputs[:2]

        softmax_logits = torch.softmax(logits[0, -1], dim=0)

        next_token_id = np.random.choice(softmax_logits.topk(n).indices.numpy(), 1)[0]
        cur_ids = torch.cat([cur_ids, torch.tensor(next_token_id).view(1, 1)], dim=1)

        output_list = list(cur_ids.squeeze().numpy())
        output_text = tokenizer.decode(output_list)
    return output_text


# start_sentence = "Хочу поздравить Россиян с"
# LENGTH_OF_SENTENCE = 100
# print(generate_n_words(LENGTH_OF_SENTENCE, start_sentence, device))
