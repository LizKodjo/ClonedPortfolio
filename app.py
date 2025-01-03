from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

# Create app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ in "__main":
    app.run(debug=True)