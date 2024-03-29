#!/usr/bin/python3
"""
city module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes City instance with state_id and name attributes
        """
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', "")
        self.name = kwargs.get('name', "")
