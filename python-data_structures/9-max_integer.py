#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        maximum_value = my_list[0]
        for x in my_list:
            if x > maximum_value:
                maximum_value = x
        return maximum_value
