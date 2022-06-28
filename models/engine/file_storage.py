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

        new = {}
        with open(self.__file_path, mode='w', encoding='utf-8') as json_file:
            for key, value in self.__objects.items():
                new.update({key: value.to_dict()})
            json_file.write(json.dumps(new))
           

    def reload(self):

        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as json_file:
                new_dict = json.loads(json_file())
                for key, value in new_dict.items():
                    class_name = value.get("__class__")
                    obj = eval(class_name + "(**value)")
                    self.__objects[key] = obj

        except IOError:
            pass
