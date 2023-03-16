from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Este é meu primeiro site em flask"

app.run