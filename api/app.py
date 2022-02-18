from flask import Flask, render_template
import controllers

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/query")
def post():
    return "<p>TODO set up POST that fires up NLP</p>"