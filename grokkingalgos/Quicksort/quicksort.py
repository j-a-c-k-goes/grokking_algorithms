#!/usr/bin/python3.11
"""
    @name quicksort.py
    @purpose demonstrate using a quicksort function on an array/list
"""
import random

def quickSort(myList:list, pivot:int):
	""" 
	    @method quickSort()
	    @param myList:list
	    @param pivot:int
	    @return myList or recursiveCase
	"""
	baseCase = len(myList) < 2
	if baseCase:
		""" Base case occurs when list is two elements or less"""
		return myList
	else:
		pivot = myList[ pivot ]
		leftPartition = [ item for item in myList[1:] if item < pivot ]
		rightPartition = [ item for item in myList[1:] if item > pivot ]
		partition = quickSort( leftPartition ) + [pivot] + quickSort( rightPartition )
		recursiveCase = partition 
		return recursiveCase

if __name__ == "__main__":
	myList = [ 5, 3, 59, 9, 11, 8, 13 ]
	pivotChoice = random.choice( myList )
	print( "Pivot value:", pivotChoice )
	myPivot = myList.index( pivotChoice)
	quickSorted = quickSort( myList, myPivot )
	print( quickSorted )