#!/usr/bin/python3
""" module defines FileStorage """

import json
from models.base_model import BaseModel

class FileStorage():
    """ defines class FileStorage """
    __file_path = "file.json"
    __objects = {}
    def __init__(self) -> None:
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        new = {}
        with open(self.__file_path, mode='w', encoding='utf-8') as json_file:
            for key, value in self.__objects.items():
                new.update({key: value.to_dict()})
            json_file.write(json.dumps(new))
           

    def reload(self):
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as json_file:
                for o in json.load(json_file).values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**o))
        except FileNotFoundError:
            pass
