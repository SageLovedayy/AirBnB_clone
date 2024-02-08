#!/usr/bin/python3
from datetime import datetime
import uuid

"""
Module - BaseModel
Parent class with common attributes/ methods
"""


class BaseModel():
    """
    Base class model for other classes
    """
    # public instance attributes
    def __init__(self):
        """
	Initializes instance with random unique id, time created and
	time updated
    	"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
    	returns details of instance
    	"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    # public instance methods
    def save(self):
        """
    	updates time for instance
    	"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
    	returns new dictionary with name, and time/date in isoformat
    	"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return (new_dict)
