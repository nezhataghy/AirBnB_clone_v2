#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ returns list of Review instances related to state """
            from models import storage, Review
            reviews_list = []
            for review in storage.all(Review).values():
                if review.state_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            """ returns list of Review instances related to state """
            from models import storage, Amenity
            amenities_list = []
            for amenity in storage.all(Amenity).values():
                if amenity.state_id == self.id:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            """Amenity id setter"""
            from models import Amenity
            if type(obj) is Amenity:
                self.amenity_ids.append(obj.id)

    else:
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", cascade="delete", backref="place")
        amenities = relationship(
            "Amenity", secondary="place_amenity", viewonly=False)
