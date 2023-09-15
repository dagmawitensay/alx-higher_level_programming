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

    def test_from_json_string(self):
        list_input = [
        {'id': 89, 'width': 10, 'height': 4},
        {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}])
