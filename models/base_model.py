#!/usr/bin/python3
""" module defines BaseModel """

from datetime import datetime
import uuid
import time


class BaseModel():
    """ defines class BaseModel """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.update_at = datetime.now()


test = BaseModel()
print(test)
