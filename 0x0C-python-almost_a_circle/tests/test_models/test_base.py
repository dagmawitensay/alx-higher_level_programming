#!/usr/bin/python3
import unittest
from models.base import Base



class TestBaseClass(unittest.TestCase):
    def test_valued_instance(self):
        b1 = Base(1)
        self.assertEqual(b1.id, 1)

    def test_Empty_instance(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
