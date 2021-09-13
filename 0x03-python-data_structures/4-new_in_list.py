#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    ret = my_list[:]
    if idx < 0 or idx > len(ret):
        return ret
    else:
        ret[idx] = element
        return ret
