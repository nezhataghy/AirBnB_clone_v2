#!/usr/bin/python3
"""This module starts a Flask web application"""

from flask import Flask
from models import storage, State
from flask import render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page: (inside the tag BODY)"""
    states = list()
    states_dict = storage.all("State")
    for state in states_dict.values():
        states.append(state)
    return render_template("7-states_list.html", states_list=states)


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
                           states=states,
                           cities=cities,
                           id=id)


@app.route("/hbnb_filters", strict_slashes=False)
def display_filters():
    state_dict = storage.all("State")
    city_dict = storage.all("City")
    amenities_dict = storage.all("Amenity")
    states = list()
    cities = list()
    amenities = list()
    for state in state_dict.values():
        states.append(state)
    for city in city_dict.values():
        cities.append(city)
    for amenity in amenities_dict.values():
        amenities.append(amenity)

    return render_template("10-hbnb_filters.html",
                           states=states,
                           cities=cities,
                           amenities=amenities)


@app.teardown_appcontext
def terminate(exception):
    """close the storage"""
    storage.close()


if __name__ == '__main__':
    """Listening on"""
    app.run(port=5000, host='0.0.0.0')
