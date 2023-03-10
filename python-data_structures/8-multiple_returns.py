#!/usr/bin/python3
def multiple_returns(sentence):
    Length = len(sentence)
    if Length == 0:
        first_character = None
    else:
        first_character = sentence[0]
    Tuple = (Length, first_character)
    return Tuple
