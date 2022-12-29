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
tokenizer = GPT2Tokenizer.from_pretrained(Config.NEW_TRAINED_MODEL_HF_NAME)
model = GPT2LMHeadModel.from_pretrained(Config.NEW_TRAINED_MODEL_HF_NAME)
model.eval()
model.to(device)
print("Done.")


def generate_n_words(
    lenght_of_sentence, 
    start_sentence, 
    determenistic_n, 
    context=None, 
    device=device
):

    # model_path = os.path.join(
    #     Config.MODELS_FOLDER, Config.MODEL_STORE_NAME.format(Config.MODEL_EPOCH)
    # )
    # model.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")))

    start_ids = torch.tensor(tokenizer.encode(start_sentence)).unsqueeze(0).to(device)

    if context:
        start_sentence = f"{context} {start_sentence} {context} {start_sentence}"

    cur_ids = torch.tensor(tokenizer.encode(start_sentence)).unsqueeze(0).to(device)
    out_ids = torch.tensor([[]])

    print("Text generation...")

    for _ in tqdm(range(lenght_of_sentence)):
        outputs = model(cur_ids, labels=cur_ids)

        _, logits = outputs[:2]

        softmax_logits = torch.softmax(logits[0, -1], dim=0)

        next_token_id = np.random.choice(
            softmax_logits.topk(determenistic_n).indices.numpy(), 1
        )[0]
        # next_token_id = choose_from_top(softmax_logits.to('cpu').detach().numpy(), n=determenistic_n)
        cur_ids = torch.cat([cur_ids, torch.tensor(next_token_id).view(1, 1)], dim=1)
        out_ids = torch.cat([out_ids, torch.tensor(next_token_id).view(1, 1)], dim=1)

    out_ids = torch.cat([start_ids, out_ids], dim=1)
    output_list = list(out_ids.squeeze().numpy())
    output_text = tokenizer.decode(output_list)

    return output_text


if __name__ == "__main__":
    start_sentence = "Хочу поздравить Россиян с"
    LENGTH_OF_SENTENCE = 30
    print(generate_n_words(
        lenght_of_sentence=LENGTH_OF_SENTENCE,
        start_sentence=start_sentence,
        determenistic_n=2,
        context="Иблис и Сатана",
        device=device
        )
    )
