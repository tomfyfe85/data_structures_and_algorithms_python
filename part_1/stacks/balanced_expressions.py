def balanced_expression_checker(string):
	# edge cases
	# (
	# ( ]
	# (()
	# )(

	stack = []

	for char in string:
		if is_right_bracket(char):
			if len(stack) == 0:
				return "Unbalanced"

			popped = stack.pop()
			if bracket_dont_match(popped, char):
				print('sticj')
				return "Unbalanced"

		if is_left_bracket(char):
			stack.append(char)

	return "Unbalanced" if len(stack) > 0 else "Balanced"

def is_left_bracket(char):
	return  char in '([{'


def is_right_bracket(char):
	return char in ')}]'


def bracket_dont_match(popped, char):
	return	popped == '(' and char != ')'or \
		 popped == '[' and char != ']'or \
		popped == '{' and char != '}'

print(balanced_expression_checker("((1 + 2)]"))
