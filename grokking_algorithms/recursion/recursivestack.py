# recursivestack.py
def factorial( x ):
	base_case = ( x == 1 )
	if base_case:
		print( 'Done.' )
		return 1
	else:
		recursive_case = ( ( x )  *  factorial( x - 1 ) )
		return recursive_case
fact_5 = factorial( 5 )
print('5!', fact_5)