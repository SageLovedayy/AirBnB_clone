#!/usr/bin/python3
"""reload storage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
