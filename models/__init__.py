#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from models.engine.file_storage import FileStorage
import os
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


classes = {"User": User, "BaseModel": BaseModel,
           "Place": Place, "State": State,
           "City": City, "Amenity": Amenity,
           "Review": Review}


if os.getenv('HBNB_TYPE_STORAGE') != 'db':
    storage = FileStorage()
    storage.reload()
else:
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
