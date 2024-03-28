from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "This is Home Page"

@app.route("/about")
def about():
    return "This is about page"