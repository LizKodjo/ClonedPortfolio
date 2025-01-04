from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

# Create app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("aboutme.html")

@app.route("/code")
def code():
    return render_template("code.html")

@app.route("/scs")
def scs():
    return render_template("scs.html")

if __name__ in "__main":
    app.run(debug=True)