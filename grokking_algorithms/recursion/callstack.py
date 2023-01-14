# callstack.py
def greet( name ):
	print( f'hello { name }' )
	greet_2( name )
	print( f'getting ready to say bye.' )
def greet_2( name ):
	print( f'how are you, { name }' )
	def bye():
		print( 'ok bye!' )
greet( 'jack' )