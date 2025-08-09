from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_jovian():
    return "<h1>Hello Jovian</h1>"