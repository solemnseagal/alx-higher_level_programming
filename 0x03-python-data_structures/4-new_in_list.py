#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    ret = my_list[:]
    if 0 <= idx < len(ret):
        ret[idx] = element
        return ret
    else:
        return my_list
