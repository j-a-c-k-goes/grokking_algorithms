#!/usr/bin/python3.11
"""
    @name countdown.py
    @purpose Demonstrate a recursive countdown. 
"""
def countdown(item):
	print(item)
	baseCase = (item <= 0)
	if baseCase:
		return
	else:
		recursiveCase = countdown(item - 1)
		recursiveCase

if __name__ == "__main__":
	countdown(3)
