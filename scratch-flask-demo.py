# working flask demo
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return app.make_response("Hello world")