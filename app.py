from flask import Flask
from flask import flash, render_template, request, redirect, url_for, jsonify, Response
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    hello="Welcome to my website"
    return render_template('index.html',hello=hello)

@app.route('/portfolio', methods=['GET','POST'])
def portfolio():
    return render_template('portfolio.html')

@app.route('/resume', methods=['GET','POST'])
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug=True)