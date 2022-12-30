from flask import Flask, request
from generate_text import  generate_n_words, device
import redis
from config import Config

app = Flask(__name__)
r = redis.Redis(
    host='redis', 
    port=6379,
    db=0, 
    password=None, 
    socket_timeout=500,
    )

@app.route("/gpt/medved")
def infer():
    
    phrase = request.args.get('phrase')
    
    out = r.get(phrase) 

    if out is None:
        out = generate_n_words(
            lenght_of_sentence=Config.NUMBER_OF_WORDS,
            start_sentence=phrase,
            determenistic_n=3,
            context=Config.PRESET_PHARASES_WITH_CONTEXT.get(phrase, None),
            device=device
        )
        r.set(phrase, out)
    else:
        out = out.decode("utf-8")
    return {"Dmitro says": out}

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)