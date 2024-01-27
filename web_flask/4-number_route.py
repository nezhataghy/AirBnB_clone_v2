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
    """Handling C routes"""
    return f"C {escape(text.replace('_', ' '))}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def handle_python_route(text="is cool"):
    """Handling Python route"""
    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<n>", strict_slashes=False)
def display_integer(number):
    """"""


if __name__ == '__main__':
    """Listening on"""
    app.run(port=5000, host='0.0.0.0')
