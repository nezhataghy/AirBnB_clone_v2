#!/usr/bin/python3
"""This module starts a Flask web application"""

from flask import Flask
from models import storage, State
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def show_states(id=None):
    state_dict = storage.all("State")
    city_dict = storage.all("City")
    states = list()
    cities = list()
    for state in state_dict.values():
        states.append(state)
    for city in city_dict.values():
        cities.append(city)

    state_id = "State.{}".format(id)
    if id is not None and state_id not in state_dict:
        states = None
    return render_template("9-states.html",
                           states_list=states,
                           cities_list=cities,
                           id=id)


@app.teardown_appcontext
def terminate(exception):
    """close the storage"""
    storage.close()


if __name__ == '__main__':
    """Listening on"""
    app.run(port=5000, host='0.0.0.0')
