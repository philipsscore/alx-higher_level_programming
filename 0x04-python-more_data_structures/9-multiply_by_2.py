#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    k_list = list(new_dict.keys())

    for k in k_list:
        new_dict[k] *= 2

    return (new_dict)
