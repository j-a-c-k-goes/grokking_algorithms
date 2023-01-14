import random

'''
	Create a Binary Search for an integer in a sorted list.
'''

def binary_search( my_list, item ):
	'''
	    binary search on a sorted list

	    parameters:
	        my_list ( list ): this is the sorted list to search from
	        item ( integer, str ): the item being searched for in this list
	'''
	number_of_guesses = 0
	low = 0
	high = ( ( len( my_list ) ) - ( 1 ) )
	while low <= high:
		middle = ( ( low ) + ( high ) ) / ( 2 )
		guess = my_list[ int(middle) ]
		if guess == item:
			''' found item, return middle '''
			print( f'steps to find item ( { item } ):', number_of_guesses )
			return middle
		if guess > item:
			''' guess is too high, reassign value '''
			high = ( ( middle ) - ( 1 ) )
		else:
			''' guess too low, reassign value '''
			low = middle
		number_of_guesses += 1

def create_test_list( n_items:int ):
	''' create a test list of n items '''
	test_list = list()
	for i in range( n_items ):
		test_list.append( i )
	return sorted( test_list )

<<<<<<< HEAD
test_list = create_test_list( 10_000 )
search_a = binary_search( test_list, 201 )
=======
test_list = create_test_list( 128 )
search_a = binary_search( test_list, 12)
print( 'search result:', search_a )
>>>>>>> 019a9a0a1ca52a98bae97e8e4c1d01eaf4ce4836
