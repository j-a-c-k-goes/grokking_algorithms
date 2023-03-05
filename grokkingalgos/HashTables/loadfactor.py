#!/usr/bin/python3.11
"""
    @name loadfactor.py
    @purpose demonstrate calculating the load factor of an array.
"""
from random import randint
test_array = list([None]) * randint(2,100)
zero_array = [0 for i in range(randint(2,100))]
def calculate_load_factor(test_array):
    size_of_array = len(test_array)
    items_in_array = list()
    for item in test_array:
        if item != None:
           items_in_array.append(item)
    load_factor = len(items_in_array) / size_of_array
    if load_factor >= 0.7:
        print("Allocate more spac or reconfigure the list.")
    else:
        print("Load is ok.")
    return load_factor
