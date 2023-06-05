#!/usr/bin/python3
"""defines rebel integer class"""


class MyInt(int):
    """rebel integer class that switches == and !="""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
