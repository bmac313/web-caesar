import string

def alphabet_position(letter):
	""" 
	Returns the index of the letter in the alphabet if it is in the alphabet.
	Returns -1 if it is not.
	"""
	alphabet = string.ascii_uppercase
	if letter.upper() in alphabet:
		return alphabet.index(letter.upper())
		
	return -1
	
def rotate_char(char, rot):
	pass