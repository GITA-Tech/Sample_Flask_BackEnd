from flask import Flask, render_template

app = Flask(__name__)

wsgi_app = app.wsgi_app

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")
    