#!/usr/bin/python3
"""defines a function that inserts a line
of text to a file after each line with given string"""


def append_after(filename="", search_string="", new_string=""):
    """adds a text after each line with given string"""
    txt = ""
    with open(filename, 'r') as f:
        f_line = f.readline()
        while f_line != "":
            txt += f_line
            if search_string in f_line:
                txt += new_string
            f_line = f.readline()
    with open(filename, 'w') as f:
        f.write(txt)
