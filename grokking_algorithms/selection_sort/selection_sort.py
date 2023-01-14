'''
    Modern languages have a sort function. 
    However, knowing how one of these works, is fundamental.
    Use-case: Selection Sort prior to a binary search.
'''

def find_smallest(array):
	smallest = array[ 0 ] # beginning of the array
	smallest_index = 0
	for i in range( 1, len( array ) ):
		''' Loop through the array '''
		if array[ i ] < smallest:
			''' 
			    array [i] less than smallest
			    Reassign smallest 
			    Reassign smallest index
			'''
			smallest = array [ i ]
			smallest_index = i
	return smallest_index

def selection_sort(array):
	''' 
	    Selection sort
	    Operates on array, creates new data.  
	'''
	new_array = list()
	for i in range( len( array ) ):
		''' 
		    Find smallest in array
		    Append the popped smallest to new array
		'''
		smallest = find_smallest( array )
		new_array.append( array.pop( smallest ) )
	return new_array

print( selection_sort( [ 15, 3, 6, 200, 10 ] ) )