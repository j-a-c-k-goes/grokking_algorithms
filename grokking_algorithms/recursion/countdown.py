# countdown.py 
import time
def countdown( i ):
	'''
	    countdown() is a recursive function to countdown from a number ( i )
	    Parameters:
	        i (int): Number to countdown from.
	'''
	time.sleep( 0.50 )
	print( 'Counting down ...', i )
	base_case = ( i <= 0 )
	if base_case:
		''' 
		    Base case keeps function from\
		    becoming an infinite loop.
		'''
		print( 'Finished.' )
		return
	else:
		''' 
		    Recursive case; call countdown.
		    Parameters:
		        i (int)
		'''
		countdown( i - 1 )
countdown( 10 )