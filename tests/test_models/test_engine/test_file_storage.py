#!/usr/bin/python3
"""
Unit tests for the FileStorage class
"""
import unittest
import pep8
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''
    Testing the FileStorage class.
    '''

    @classmethod
    def setUpClass(cls):
        """
        Set up class instance
        """
        cls.rev1 = Review()
        cls.rev1.place_id = "Housto"
        cls.rev1.user_id = "Sage"
        cls.rev1.text = "Fast"

    @classmethod
    def tearDownClass(cls):
        """
        Clean up resources
        """
        del cls.rev1

    def tearDown(self):
        """
        Clean up method to remove the 'file.json' if it exists
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            # The file doesn't exist, nothing to remove
            pass
        except PermissionError:
            # Permission denied when trying to remove the file
            # Handle this according to your application's logic
            print("Permission denied when trying to remove file.json")
        except Exception as e:
            # Catch any other unexpected exceptions & handle appropriately
            print(f"An error occurred: {e}")

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """
        Tests method: all (returns dictionary <class>.<id> : <obj instance>)
        """
        storage = FileStorage()
        instances_dic = storage.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, storage._FileStorage__objects)

    def test_new(self):
        """
        Tests method: new (saves new object into dictionary)
        """
        m_storage = FileStorage()
        instances_dic = m_storage.all()
        johndoe = User()
        johndoe.id = 999999
        johndoe.name = "Johndoe"
        m_storage.new(johndoe)
        key = johndoe.__class__.__name__ + "." + str(johndoe.id)
        self.assertIsNotNone(instances_dic[key])

    def test_reload(self):
        """
        Tests method: reload (reloads objects from string file)
        """
        a_storage = FileStorage()
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
