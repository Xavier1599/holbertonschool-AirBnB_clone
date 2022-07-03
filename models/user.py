#!/usr/bin/python3
""" module defines User """

from models.base_model import BaseModel


class User(BaseModel):
    """ defines User class

    Inherets from BaseModel

    Attributes:
    email: The user's email
    password: The user's password
    first_name: The user's first name
    last_name: The user's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
