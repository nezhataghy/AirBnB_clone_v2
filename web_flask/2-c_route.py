#!/usr/bin/python3
"""This module starts a Flask web application"""""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def handle_c_route(text):
    """handling varible routes"""
    return f"C {escape(text.replace('_', ' '))}"


if __name__ == '__main__':
    """Listening on"""
    app.run(port=5000, host='0.0.0.0')
