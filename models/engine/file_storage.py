#!/usr/bin/python3
""" module defines FileStorage """

import json
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
        return FileStorage.__objects

    def new(self, obj):
        """ sets objects attribute """
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """ serializes objects to JSON file """
        obj_dict = FileStorage.__objects
        objd = {objd: obj_dict[obj].to_dict() for obj in obj_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objd, f)

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
            pass
