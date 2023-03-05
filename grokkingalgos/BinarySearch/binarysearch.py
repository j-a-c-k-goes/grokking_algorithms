#!/usr/bin/python3.11
"""
    @name binarysearch.py
    @purpose demo a binary search algorithm for a sorted list. 
"""
import random
import math
def binarySearch( my_list, item ):
	"""
	    @method binary_search()
	    @purpose function performs the binary search on a sorted list
	    @param my_list: list | this is the sorted list to search from
	    @param item: integer or str | the item being searched for in this list
	    @return found item
	"""
	number_of_guesses = 0
	low = 0
	high = ( ( len( my_list ) ) - ( 1 ) )
	while low <= high:
		middle = ( ( low ) + ( high ) ) / ( 2 )
		guess = my_list[ int(middle) ]
		if guess == item:
			# Found item. Return middle value.
			print( 'Steps to find item:', number_of_guesses )
			return math.floor(middle)
		if guess > item:
			# Guess exceeds item. Reassign high value as (middle - 1)
			high = ( ( middle ) - ( 1 ) )
		else:
			# Guess is too low. Reassign low value as middle value.
			low = middle
		number_of_guesses += 1 # Increment the accumulator value.

def createIntegerList( n_items:int ):
	''' create a test list of n items '''
	print(f"Creating a test list of with { n_items } items.")
	test_list = list()
	for item in range( n_items ):
		test_list.append( item )
	return sorted( test_list )

def createStringList( nItems:int ):
	''' create a test list of n items '''
	print(f"Creating a test list of with { n_items } items.")
	testList = list()
	for item in range( nItems ):
		testList.append( f"{item}hello" )
	return sorted( testList )

if __name__ == "__main__":
	testIntegers = createIntegerList( random.randint( 1,10_000 ) )
	itemSearchingFor = int(input("Input the integer you are searching for: "))
	binSearchIntegers = binarySearch( testIntegers, itemSearchingFor)
	print( "Search result:", binSearchIntegers )