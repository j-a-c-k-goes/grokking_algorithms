#!/usr/bin/python3.11
"""
    @name countdown.py
    @datelastmodified 2023 03 22
    @purpose Demonstrate a recursive countdown. 
"""
from random import randint
class Countdown:
	#.......................................... Constructor
	def __init__( self, from_value:int ):
		self.value_to_recurse_with = from_value
		self.end_comment = "Recursion is like cat calling yourself."
	#.......................................... Getters
	def get_value_to_recurse( self ):
		return self.value_to_recurse_with
	#.......................................... Setters
	def set_value_to_recurse( self, value:int ):
		self.value_to_recurse_with = value
	#.......................................... Data Methods
	def recursive( self, value_to_recurse_with:int ):
		""" 
		   @method 		recursive
		   @param 		value_to_recurse_with
		   @purpose 	Recursive countdown. Base case:\
		                the value to recurse with is less\
		                than or equal to zero. Recursive case:\
		                Method self calls, subtracts value\
		                from 1 until reaching the base case.
        """
		print( value_to_recurse_with )
		base_case = ( value_to_recurse_with <= 0 )
		if base_case:
			print( self.end_comment )
			return True
		else:
			self.recursive( value_to_recurse_with - 1 )
if __name__ == "__main__":
	random_integer = randint( 2, 100 ) 
	countdown = Countdown( random_integer )
	countdown.recursive( random_integer )
	
