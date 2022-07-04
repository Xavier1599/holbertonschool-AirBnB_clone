#!/usr/bin/python3
""" module defines FileStorage """

import imp
import json
from pydoc import importfile
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """ defines class FileStorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns dictionary """
        return self.__objects

    def new(self, obj):
        """ sets objects attribute """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """ serializes objects to JSON file """
        new = {}
        with open(self.__file_path, 'w', encoding='utf-8') as json_file:
            for key, value in self.__objects.items():
                new.update({key: value.to_dict()})
            json_file.write(json.dumps(new))

    def reload(self):
        """ deserializes JSON file to object """
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load()
                for o in obj_dict.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name(**o)))
        except FileNotFoundError:
            return
