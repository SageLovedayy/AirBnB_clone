#!/usr/bin/python3
"""
FileStorage module
"""

from models.base_model import BaseModel
import json
import os


class FileStorage():
    """
    serializes instances to a JSON file, deserializes JSON file to instances
    """
    # private class attributes
    __file_path = "file.json"
    __objects = {}

    # public instance methods
    def all(self):
        """
        returns the dictionary, __objects
        """
        return (self.__objects)

    def new(self, obj):
        """
        stores new object by <class name>.id in the __objects dictionary
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        deserializes JSON file to __objects
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                try:
                    data = json.load(file)
                    for key, value in data.items():
                        class_name, obj_id = key.split('.')
                        cls = globals()[class_name]
                        self.__objects[key] = cls(**value)

                except json.JSONDecodeError:
                    pass
