#!/usr/bin/python3.11
"""
    @name factorial.py
    @purpose Demonstrate a recursive factorial. 
"""
import random

def factorial(value):
	baseCase = (value == 1)
	if baseCase:
		return 1 
	else:
		recursiveCase = ( value * factorial(value - 1) )
		return recursiveCase

if __name__ == "__main__":
	randInt = random.randint(2,32)
	print(f"Value to factorial: { randInt } ")
	print(f"{ randInt }! = { factorial(randInt) }")