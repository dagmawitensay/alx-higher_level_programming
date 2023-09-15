#!/usr/bin/python3
"""
This module contains test classes for the Square object.
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_object_createion(self):
        s1 = Square(10)
        s2 = Square(10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_getter(self):
        s = Square(3)
        self.assertEqual(s.width, 3)

    def test_invlaid_width(self):
        with self.assertRaises(ValueError):
            Square(-10)

    def test_invalid_type_size(self):
        with self.assertRaises(TypeError):
            Square("integer")

    def test_id_updage(self):
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)

    def test_size_update(self):
        s = Square(5)
        s.update(10, 10)
        self.assertEqual(s.width, 10)

    def test_x_update(self):
        s = Square(5)
        s.update(10, 10, 10)
        self.assertEqual(s.x, 10)

    def test_y_update(self):
        s = Square(5)
        s.update(10, 10, 10, 10)
        self.assertEqual(s.y, 10)

    def test_dictonary_representation(self):
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 1, 'x': 2, 'size': 10, 'y': 1})
