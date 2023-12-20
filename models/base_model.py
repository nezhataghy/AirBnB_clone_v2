#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


if os.getenv('HBNB_TYPE_STORAGE') != 'db':
    class Base:
        pass
else:
    Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

# ____________________________________________________________________________________________

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                if key != '__class__':
                    setattr(self, key, value)

            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()

    # ____________________________________________________________________________________________

    def __str__(self):
        """Returns the String representation of an instance"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    # ____________________________________________________________________________________________

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    # ____________________________________________________________________________________________

    def to_dict(self):
        """Returns a dictionary contains __dict__ keys/values of instance"""

        instance_dict = self.__dict__.copy()

        instance_dict["__class__"] = self.__class__.__name__

        # Change datetime object to string format
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in instance_dict.keys():
            del instance_dict['_sa_instance_state']

        return instance_dict

    # ____________________________________________________________________________________________

    def delete(self):
        """Deletes the current instance from the storage
        by calling the method delete"""
        from models import storage
        storage.delete(self)
