#@Vuitya
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Viktor Syrotkin, TI-92'
@app.route('/first')
def first():
    num_0 = None
    num_1 = 124
    num_2 = 123
    name = request.args.get("name", "World")
    return f'{num_0},{num_1},{num_2}'

if __name__ == '__main__':
    app.run('0.0.0.0')