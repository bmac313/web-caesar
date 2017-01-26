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
	
def rotate_character(chara, rot):
	alpha_upper = string.ascii_uppercase
	alpha_lower = string.ascii_lowercase
	new_chara = ""	
	
	if alphabet_position(chara) >= 0:               # Skip character rotation if the character is not alphabetic
		current_idx = alphabet_position(chara) + 1  # Shift alphabet index 1 to the right to help with possible "wrap around" operations. e.g.: if alphabet_position is 0, make it index 1 instead.
		next_idx = current_idx + rot                # For example: current_idx == 20, rot == 7, next_idx == 27. 26 represents 'Z' in this case, and we need it to 'wrap around' to 'A'. So (cont. below):
		if next_idx > 26:                           #              
			next_idx -= 26                          #              ...subtract 26 from next_idx to get 1.
		next_idx -= 1                               #              ...subtract 1 from next_idx to bring it back in line with the string index of 'A' (index 0)
		
		if chara in alpha_upper:
			new_chara = alpha_upper[next_idx]
		elif chara in alpha_lower:
			new_chara = alpha_lower[next_idx]
		
	else:
		new_chara = chara
	
	return new_chara