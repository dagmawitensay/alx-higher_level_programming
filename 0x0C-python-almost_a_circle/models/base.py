#!/usr/bin/python3
"""
This module defines a base class for models.
"""
import json
import csv


class Base:
    """
    A base class for the package.
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """Instantiation of the class"""
        if not id:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON sring reprsentation of list_dictionaries.
        Args:
            list_dictionaries: list of dictionaries
        """
        if not list_dictionaries or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file.
        Args:
            list_objs: list of objects
        """
        name = cls.__name__ + ".json"
        with open(name, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                dictionary = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(dictionary))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.
        Args:
            json_string: a string representing a list of dictionaries.
        """
        if json_string is None:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.
        """
        if dictionary:
            if cls.__name__ == 'Rectangle':
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.
        """
        name = cls.__name__ + ".json"
        with open(name) as file:
            content = file.read()

        parsed = Base.from_json_string(content)
        instances = []
        for obj in parsed:
            instances.append(cls.create(**obj))

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes and saves the data to a csv file.
        """
        name = cls.__name__ + ".csv"
        with open(name, 'w') as file:
            if list_objs is None:
                writer = csv.writer(file)
                writer.writerows('[]')
            else:
                dictionary = [obj.to_dictionary() for obj in list_objs]
                if cls.__name__ == 'Rectangle':
                    order = ['id', 'width', 'height', 'x', 'y']
                else:
                    order = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(file, fieldnames=order)
                writer.writeheader()
                print(dictionary)
                writer.writerows(dictionary)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialized and return the csv data from a csv file.
        """
        data = []
        name = cls.__name__ + ".csv"
        with open(name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(dict(row))
        instances = []
        for obj in data:
            instances.append(cls.create(**obj))

        return instances
