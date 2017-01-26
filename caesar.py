import sys
from helpers import rotate_character

def encrypt(message, rot):
	new_message = ""
	for character in message:
		new_message += rotate_character(character, rot)
		
	return new_message
	
def user_input_is_valid(cl_args):
	if cl_args != "":
		return True
	
	return False
	
