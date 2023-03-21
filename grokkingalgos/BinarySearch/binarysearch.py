#!/usr/bin/python3.11
"""
    @name binarysearch.py
    @purpose demo a binary search algorithm for a sorted list. 
"""
import random
import math
class BinarySearch:
	random_number = random.randint( 1,10_000 )
	_default_data = [ 0 , 1, 2, 3, 4, 5 ]
	def __init__( self, data:list=_default_data ):
		self.data = data
	def query( self, data:list, int_searching_for:int ) -> int:
		"""
		    @method query()
		    @purpose Perform a binary search on a sorted list.
		    @param my_list, a list ( array ), database basically. 
		    @param item, the item being searched for.  
		    @return found_item
	    """
		try:
			print( f"Searching for { int_searching_for }" )
			sorted_data = sorted( data ); print( f"Sorting list by default." )
			attempts = 0; print( f"Starting with { attempts } attempts." )
			low = 0
			high = ( ( len( sorted_data ) ) - ( 1 ) )
			while low <= high:
				middle = ( ( low ) + ( high ) ) / ( 2 )
				guess = sorted_data[ int( middle ) ]
				if guess == int_searching_for:
					print( f"Found { int_searching_for }! Attempts to locate: { attempts }" )
					return math.floor( middle )
				elif guess > int_searching_for:
				    high = ( ( middle ) - ( 1 ) ) # Reassign high value as ( middle - 1 )
				else:
				    low = middle # Reassign low threshold as middle threshold.
				    attempts += 1 # Increment the accumulator value.
		except Exception:
			print( "Unexpected things are triggering exceptions." )
	@staticmethod
	def demo_integer_values( n_items:int=1_000 ) -> list:
		try:
		    print( f"Creating an integer list { n_items } items long." )
		    test_list = list()
		    for item in range( n_items ):
			    test_list.append( item )
		    return sorted( test_list )
		except Exception:
			print( "Exception triggered." )
	@staticmethod
	def generate_kings( n_items:int ) -> list:
		try:
			alphabets = ( 'a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v' )
			print( f"Creating a list of Kings { n_items } long." )
			data = list()
			for item in range( n_items ):
				random_character = random.choice( alphabets )
				data.append( f"MartinLutherKingJr{ item }{ random_character }" )
			return sorted( data )
		except Exception:
			print( "Exception triggered." )

if __name__ == "__main__":
	print(" ---- Binary Search ---- ")
	lower_bound = 1_000; 
	upper_bound = 100_000_000
	random_number = random.randint( lower_bound, upper_bound )
	test_values = BinarySearch.demo_integer_values( random_number )
	binary_search = BinarySearch( test_values )
	random_data_index = random.randint( 1, len( test_values ) )
	data_point = ( ( len( test_values ) ) % ( random_data_index ) )
	binary_search.query( test_values, data_point )