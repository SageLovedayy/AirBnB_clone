#!/usr/bin/python3
"""
state module
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes State instance with name attribute
        """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
