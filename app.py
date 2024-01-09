from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>\n"

@app.route("/goodbye")
def hello_world():
    return "<p>Goodbye, World!</p>\n"
