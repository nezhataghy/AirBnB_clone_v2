#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """SQL database storage"""
    __engine = None
    __session = None

    # -------------------------------------------------------------------

    def __init__(self):
        """Create engine and connect to database"""
        user = os.getenv("HBNB_MYSQL_USER")
        pswrd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env_ = os.getenv("HBNB_ENV", "none")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pswrd, host, db), pool_pre_ping=True)

        if env_ == 'test':
            Base.metadata.drop_all(self.__engine)

    # -------------------------------------------------------------------

    def all(self, cls=None):
        """Returns a dictionary of __object"""
        my_dic = {}
        if not cls:
            classes_list = [State, City, User, Place, Review, Amenity]
            for clase in classes_list:
                query = self.__session.query(clase)
                for v in query:
                    k = "{}.{}".format(v.__class__.__name__, v.id)
                    my_dic[k] = v

        else:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for v in query:
                k = "{}.{}".format(v.__class__.__name__, v.id)
                my_dic[k] = v

        return (my_dic)

    # -------------------------------------------------------------------

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    # -------------------------------------------------------------------

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    # -------------------------------------------------------------------

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    # -------------------------------------------------------------------

    def reload(self):
        """Create current database session from the engine
        using a sessionmaker"""
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    # -------------------------------------------------------------------

    def close(self):
        """Remove session"""
        self.__session.close()
