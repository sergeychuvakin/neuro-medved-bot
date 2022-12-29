from flask import Flask, jsonify, request
from flask_caching import Cache  


from generate_text import  generate_n_words, device


app = Flask(__name__)
app.config.from_object('config.RedisConfig')
# cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': 'redis://localhost:6379/0'})  # Initialize Cache

@app.route("/gpt/medved")
@cache.cached(timeout=50, query_string=True)
def infer():
    
    phrase = request.args.get('phrase')
    
    out = generate_n_words(
        lenght_of_sentence=30, 
        start_sentence=phrase, 
        device=device
        )
    return {"Dmitro says": out}

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5005)