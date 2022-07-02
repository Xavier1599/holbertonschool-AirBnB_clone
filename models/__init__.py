#!/usr/bin/python3
""" init for Python Package """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
