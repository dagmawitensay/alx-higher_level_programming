#!/usr/bin/python3
from models.rectangle import Rectangle
import unittest
from io import StringIO
import sys
"""
This module contains test class for the Rectangle class.
"""


class TestRectangle(unittest.TestCase):
    """Test the rectangle class"""
    def test_id(self):
        r1 = Rectangle(10, 2)
        r3 = Rectangle(3, 4, 0, 0, 20)
        self.assertEqual(r1.id, 9)
        self.assertEqual(r3.id, 20)

    def test_width(self):
        r1 = Rectangle(5, 8)
        self.assertEqual(r1.width, 5)

    def test_height(self):
        r1 = Rectangle(10, 10)
        self.assertEqual(r1.height, 10)

    def test_invalid_width(self):
        r = Rectangle(4, 5)
        with self.assertRaises(TypeError):
            r.width = "width"

    def test_invalid_width_value(self):
        r = Rectangle(10, 3)
        with self.assertRaises(ValueError):
            r.width = -10

    def test_invalid_height(self):
        r = Rectangle(10, 4)
        with self.assertRaises(TypeError):
            r.height = "height"

    def test_invalid_height_value(self):
        r = Rectangle(3, 4)
        with self.assertRaises(ValueError):
            r.height = -10

    def test_invalid_x(self):
        r = Rectangle(1, 4)
        with self.assertRaises(ValueError):
            r.x = -39

    def test_invalid_y(self):
        r = Rectangle(1, 3)
        with self.assertRaises(ValueError):
            r.y = -18

    def test_area(self):
        r = Rectangle(1, 3)
        self.assertEqual(r.area(), 3)

    def test_display(self):
        r = Rectangle(3, 3)
        expected = "###\n###\n###\n"
        captured = StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), expected)

    def test_string_representaion(self):
        r = Rectangle(4, 6, 2, 1, 12)
        expected = "[Rectangle] (12) 2/1 - 4/6\n"
        captured = StringIO()
        sys.stdout = captured
        print(r)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), expected)

class TestUpdateFunction(unittest.TestCase):
    def test_id_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_width_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual(r.width, 2)

    def test_height_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual(r.height, 3)

    def test_x_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual(r.x, 4)

    def test_y_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.y, 5)

class TestKwargs(unittest.TestCase):
    def test_height_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)

    def test_width_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(width=1)
        self.assertEqual(r.width, 1)

    def test_id_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual(r.id, 1)

    def test_x_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(x=1)
        self.assertEqual(r.x, 1)

    def test_y_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1)
        self.assertEqual(r.y, 1)
