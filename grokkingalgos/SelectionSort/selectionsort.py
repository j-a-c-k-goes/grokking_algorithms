#!/usr/bin/python3.11
"""
    @name selectionsort.py
    @purpose Demonstrating the fundamentals of a sort function.
             Could selction sort prior to a binary search. 
"""
import random
def findSmallest(array):
	"""
	    @name findSmallest
	    @purpose find the smallest value in a given array/list
	    @param array: list | the list to find a value in
	    @return smallestIndex
	"""
	smallest = array[ 0 ] # beginning of the array
	smallestIndex = 0
	for item in range( 1, len( array ) ):
		if array[ item ] < smallest:
			smallest = array [ item ]
			smallestIndex = item
	return smallestIndex

def selectionSort(array):
	"""
	    @name findSmallest()
	    @purpose sort an array/list
	    @param array: list | the list to be sorted.
	    @return newArray
	"""
	newArray = list()
	for item in range( len( array ) ):
		# print("Original array:", array)
		smallest = findSmallest( array )
		newArray.append( array.pop( smallest ) )
		# print("New array:", newArray)
	return newArray

def createRandValues(nItems=10):
	"""
	    @name createRandValues()
	    @purpose create random integers values up to n items.
	    @param nItems: Integer | the size of the set.
	    @return newArray
	"""
	randValues = set()
	for item in range(nItems):
		randValue = random.randint(1,1000)
		randValues.update( {randValue} )
	return list(randValues)

if __name__ == "__main__":
	randomValues = createRandValues(10)
	sortThis = selectionSort(randomValues)
	print("Sorted Values:", sortThis)