#!/usr/bin/env python3
def no_c(my_string):
    new_string = ""
    for i in my_string:
        if i is not 'c' and i is not 'C':
            new_string += i
    return (new_string)
# return my_string.translate({ord(c): None for c in "cC"})
