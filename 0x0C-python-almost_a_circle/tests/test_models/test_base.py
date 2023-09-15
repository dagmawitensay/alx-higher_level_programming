#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle



class TestBaseClass(unittest.TestCase):
    def test_valued_instance(self):
        b1 = Base(1)
        self.assertEqual(b1.id, 1)

    def test_Empty_instance(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_dict_to_json(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)
