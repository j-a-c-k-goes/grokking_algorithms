#!/usr/bin/python3.11
"""
    @name Factorial.py
    @datelastmodified 2023 03 22
    @purpose Demonstrate the recursive factorial of an integer. 
"""
from random import randint
class Factorial:
	#.......................................... Constructor
	def __init__(self, value_to_factorial:int):
		self.end_comment = "Infinite Loops are Glitches in the Matrix."
		self.factorial = 0 # Nothing has been factorialized yet.
		self.value_to_factorial = value_to_factorial
	#.......................................... Getters
	def get_factorial(self):
		return self.factorial
	def get_value_to_factorial(self):
		return self.value_to_factorial
	#.......................................... Setters
	def set_factorial(self, value:int):
		self.factorial = value
	def set_value_to_factorial(self, new_value:int):
		self.value_to_factorial = new_value
	#.......................................... Data Methods
	def recursive(self, value:int):
		""" 
		   @method 		recursive
		   @param 		value_to_recurse_with
		   @purpose 	Recursive factorial. Base case:\
		                the value to recurse with is one.\
		                Recursive case: Value multiplied\
		                by self.recursive(recurisve_expression)\
		                until reaching the base case.
        """
		base_case = ( value == 1 )
		if base_case:
			print( self.end_comment )
			return True
		else:
			recursive_expression = value - 1
			recursive_case = value * self.recursive( recursive_expression )
			self.factorial = recursive_case
			return recursive_case
	def view(self):
		print(f"{ self.value_to_factorial }! {self.factorial}")

if __name__ == "__main__":
	random_number = randint( 2,32 )
	Factorial = Factorial( random_number )
	Factorial.recursive( Factorial.value_to_factorial )
	Factorial.view()
