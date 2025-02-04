def find_first_rep_char(input_string):
	seen = set()

	for char in input_string:
		if char in seen:
			return char
		seen.add(char)



print(find_first_rep_char("green apple"))