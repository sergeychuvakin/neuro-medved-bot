from generate_text import  generate_n_words, device
import redis
from config import Config


r = redis.Redis(
    host='redis', 
    port=6379,
    db=0, 
    password=None, 
    socket_timeout=500,
    )


for i in range(Config.N_OPTIONS):
    
    for sent in Config.PRESET_PHARASES_WITH_CONTEXT.keys():
        
        out = generate_n_words(
            lenght_of_sentence=Config.NUMBER_OF_WORDS,
            start_sentence=sent,
            determenistic_n=3,
            context=Config.PRESET_PHARASES_WITH_CONTEXT.get(sent, None),
            device=device
        )
        r.set(f"{sent}_{i}", out)
