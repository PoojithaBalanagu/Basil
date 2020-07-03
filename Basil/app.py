from flask import Flask, request, jsonify, render_template, redirect, flash, session,url_for
import os
from SPARQLWrapper import SPARQLWrapper, XML,JSON

app = Flask(__name__)
app.secret_key=os.urandom(24)

@app.route("/specs")
def specs():
    return render_template('specs.html',page='1')

@app.route("/desc")
def desc():
    return render_template('desc.html',page='2')

@app.route("/scripts")
def scripts():
    return render_template('scripts.html',page='3')









if __name__ == "__main__":
    #app.secret_key = os.urandom(24)
    app.run(debug=True, port=5002)
