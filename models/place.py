#!/usr/bin/python3
""" This is the Place Model Module"""


from models.base_model import BaseModel


class Place(BaseModel):
    """Define Place Model"""

    def __init__(
            self, city_id="", user_id="",
            amenity_ids=[], *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.city_id = city_id
        self.user_id = user_id
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = amenity_ids