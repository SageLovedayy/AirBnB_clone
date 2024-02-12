#!/usr/bin/python3
"""user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    user class, an instance of base model
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes user instance with email. password
        , first_name and last_name attributes
        """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")

    #state_id = ""
    #name = ""
