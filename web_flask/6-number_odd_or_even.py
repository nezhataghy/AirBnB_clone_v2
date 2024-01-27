#!/usr/bin/python3
"""This module starts a Flask web application"""""
from flask import Flask, render_template
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
    """Handling C route"""
    return f"C {escape(text.replace('_', ' '))}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def handle_python_route(text="is cool"):
    """Handling Python route"""
    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<int:n>", strict_slashes=False)
def display_integer(n):
    """Handling number route"""
    return f"{escape(n)} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Handling number and pass it to html template"""
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_even_or_odd(n):
    """Handling number and pass it to html template using condition inside template"""
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == '__main__':
    """Listening on"""
    app.run(port=5000, host='0.0.0.0')
