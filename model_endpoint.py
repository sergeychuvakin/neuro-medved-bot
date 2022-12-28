from flask import request
from flask import Flask


app = Flask(__name__)
from generate_text import  generate_n_words, device

@app.route("/gpt/medved")

def send_sector():
    
    phrase = request.args.get('phrase')
    
    out = generate_n_words(
        lenght_of_sentence=30, 
        start_sentence=phrase, 
        device=device
        )
    return {"Your phrase is": out}

if __name__ == '__main__':
   app.run()