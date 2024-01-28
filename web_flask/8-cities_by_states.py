#!/usr/bin/python3
"""This module starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    state_dict = storage.all("State")
    city_dict = storage.all("City")
    states = list()
    cities = list()
    for state in state_dict.values():
        states.append(state)
    for city in city_dict.values():
        cities.append(city)
    return render_template("8-cities_by_states.html",
                           states_list=states,
                           cities_list=cities)


@app.teardown_appcontext
def terminate(exception):
    """close the storage"""
    storage.close()


if __name__ == '__main__':
    """Listening on"""
    app.run(port=5000, host='0.0.0.0')
