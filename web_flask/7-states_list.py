#!/usr/bin/python3
"""This module starts a Flask web application"""""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page: (inside the tag BODY)"""
    states = list()
    states_dict = storage.all("State")
    for state in states_dict.values():
        states.append(state)
    return render_template("7-states_list.html", states_list=states)


@app.teardown_appcontext
def terminate(exception):
    """Close the storage"""
    storage.close()


if __name__ == '__main__':
    """Listening on"""
    app.run(port=5000, host='0.0.0.0')
