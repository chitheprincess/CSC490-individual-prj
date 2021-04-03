from model import InputForm
from flask import Flask, render_template, request
from compute import compute

app = Flask(__name__)


@app.route('/pde', methods=['GET', 'POST'])
def hello():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)
