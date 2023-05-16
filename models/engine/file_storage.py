#!/usr/bin/python3
""" module defines class FileStorage """

import json
import os


class FileStorage:
    """ class serializes instances to a JSON file and/
        deserializes JSON file to instances """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """

        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """

        obj_id = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[obj_id] = obj

    def save(self):
        """ serializes __objects to the JSON file """

        jsonfile = self.__file_path
        with open(jsonfile, "w", encoding="utf-8") as file:
            dict_obj = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dict_obj, file)

    def classes(self):
        """ returns a dictionary valid classes as\
            values to their string names"""

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel, "User": User,
                   "State": State, "City": City,
                   "Amenity": Amenity, "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """ deserializes the JSON file to __objects """

        jsonfile = self.__file_path
        if os.path.exists(jsonfile):
            new_dict = {}
            with open(jsonfile, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)

            for id, dictionary in obj_dict.items():
                class_name = dictionary["__class__"]
                new_dict[id] = self.classes()[class_name](**dictionary)

            self.__objects = new_dict
