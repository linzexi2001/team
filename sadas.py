import flask
import os
import random
from main import myleast,numbersclass,prearray,notkeynum,bestchoice
app=flask.Flask(__name__)
@app.route("/")
def hello():
    return "heelo"
@app.route("/hi")
def hi():
    return "Hi,nuhao"

if __name__=="__main__":
    app.run()