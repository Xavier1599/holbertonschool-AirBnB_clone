#!/usr/bin/python3
""" module defines FileStorage """

import json


class FileStorage():
    """ defines class FileStorage """
    __file_path = "file.json"
    __objects = {}
    def __init__(self) -> None:
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__name__}.{obj.id}"] = obj

    def save(self):
        string_rep = json.dumps(self.__objects)
        with open(self.__file_path, 'a') as jsonfile:
            jsonfile.write(string_rep)

    def reload(self):
        pass
