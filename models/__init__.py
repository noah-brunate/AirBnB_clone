#!/usr/bin/python3
""" module identifies this directory as a package """

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
