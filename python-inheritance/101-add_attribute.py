#!/usr/bin/python3
"""defines a function that checks if you can add attribute to an object"""


def add_attribute(obj, name, value):
    """checks if you can add atrribute"""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
