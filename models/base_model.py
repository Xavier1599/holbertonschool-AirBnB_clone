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

    def save(self):
        self.update_at = datetime.now()

test = BaseModel()
print(test.update_at)
time.sleep(5)
test.save()
print(test.update_at)
