# app.py

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/parse_arguments')
def parse_arguments():
    arg1 = request.args.get('arg1')
    arg2 = request.args.get('arg2')
    return f'Arguments received: arg1={arg1}, arg2={arg2}'

app.run(debug=True)
print("HELLO!")
