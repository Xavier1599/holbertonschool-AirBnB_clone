#!/usr/bin/python3
""" module defines BaseModel """

from datetime import datetime
from time import strptime
import uuid
import models


class BaseModel():
    """ defines class BaseModel """
    def __init__(self, *args, **kwargs):
        """ initializes class """
        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, time_form)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def __str__(self):
        """ defines str method """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """ updates de updated_at attribute """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns dictionary of key/values """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
