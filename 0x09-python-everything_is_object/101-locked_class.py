#!/usr/bin/python3
class LockedClass:
    __slots__ = ('firt_name',)

    def __setatr__(self, name, value):
        if name != 'first_name':
            raise AttributeError(
                    "'LockedClass' object has no attribute '{}'".format(name))
        self.__dict__[name] = value
