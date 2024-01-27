#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    # -------------------------------------------------------------------

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            class_objects = {}
            for k, v in FileStorage.__objects.items():
                if k.split('.')[0] == cls.__name__:
                    class_objects[k] = v
            return class_objects
        else:
            return FileStorage.__objects

    # -------------------------------------------------------------------

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    # -------------------------------------------------------------------

    def save(self):
        """Saves storage dictionary to file"""
        temp = {}
        for key, val in FileStorage.__objects.items():
            temp[key] = val.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf8') as f:
            json.dump(temp, f)

    # -------------------------------------------------------------------

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(FileStorage.__file_path, 'r') as f:
                file_data = json.load(f)

                for key, val in file_data.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    # -------------------------------------------------------------------

    def delete(self, obj=None):
        """Deletes obj from __objects if it is inside"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    # -------------------------------------------------------------------

    def close(self):
        """Calling reload() to deserialize the JSON file to objects"""
        self.reload()
