#!/usr/bin/python3
""" module defines User """

from models.base_model import BaseModel


class User(BaseModel):
    """ defines User class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """cunstructor for base model"""
        super().__init__(*args, **kwargs)
