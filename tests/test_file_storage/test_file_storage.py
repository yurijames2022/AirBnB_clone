import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ Test the FileStorage class """

    def setUp(self):
        """ Set up test environment """
        self.storage = FileStorage()

    def tearDown(self):
        """ Remove test environment """
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except:
            pass

    def test_all_method(self):
        """ Test that all method returns an empty dictionary initially """
        self.assertEqual(self.storage.all(), {})

    def test_new_method(self):
        """ Test that new method adds an object to __objects """
        obj = BaseModel()
        self.storage.new(obj)
        key = obj.__class__.__name__ + '.' + obj.id
        self.assertEqual(self.storage.all()[key], obj)

    def test_save_method(self):
        """ Test that save method saves __objects to file """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        key = obj.__class__.__name__ + '.' + obj.id
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            file_contents = json.load(f)
            self.assertEqual(file_contents[key], obj.to_dict())

    def test_reload_method(self):
        """ Test that reload method loads __objects from file """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = obj.__class__.__name__ + '.' + obj.id
        self.assertEqual(self.storage.all()[key].to_dict(), obj.to_dict())

if __name__ == '__main__':
    unittest.main()
