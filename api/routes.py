from flask import Flask
import controllers

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>TODO send welcome form template</p>"

@app.route("/query")
def post():
    return "<p>TODO set up POST that fires up NLP</p>"