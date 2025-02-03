
def find_first_non_rep_char(input_string):
	char_count = {}
	for char in input_string.replace(" ", ""):
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1

	for k, v in char_count.items():
		if v == 1:
			return k


print(find_first_non_rep_char("a green apple"))