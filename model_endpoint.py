from flask import Flask, request
from generate_text import  generate_n_words, device
import redis

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
            lenght_of_sentence=30,
            start_sentence=phrase,
            determenistic_n=2,
            context="Санкции Пиндостана",
            device=device
        )
        r.set(phrase, out)

    return {"Dmitro says": out.decode("utf-8")}

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)