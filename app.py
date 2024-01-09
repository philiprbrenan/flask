from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "<p>Hello, World!</p>\n"

@app.route("/goodbye")
def goodbye():
    return "<p>Goodbye, World!</p>\n"
