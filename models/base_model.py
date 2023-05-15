#!/usr/bin/python3
""" module defines a class BaseModel """


import uuid
import datetime
from models import storage


class BaseModel:
    """ class BaseModel that defines all common attributes/
    methods for other classes """

    def __init__(self, *args, **kwargs):
        """ method initiates instance attributes """

        if kwargs is not None and kwargs != {}:
            for key in kwargs.keys():
                if key == "__class__":
                    continue
                else:
                    if key == "created_at" or key == "updated_at":
                        kwargs[key] = datetime.datetime.strptime(
                            kwargs[key],
                            '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """ returns string representation of an object """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ method updates the public instance\
        attribute updated_at with the current datetime """

        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ method returns a dictionary containing all keys/
        values of __dict__ of the instance """

        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__

        return my_dict
