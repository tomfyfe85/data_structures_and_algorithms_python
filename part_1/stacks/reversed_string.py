def reverse(str):
	stack = []  # Initialize an empty stack
	reversed_string = ""  # Initialize the reversed string
	if not str :
		raise ValueError(
			"Argument cannot be None"
		)
	# Push each character of the string onto the stack
	for char in str:
		stack.push(char)

	# Pop characters from the stack to build the reversed string
	while stack:
		reversed_string += stack.pop()

	# return reversed_string  # Return the reversed string
	return stack  # Return the reversed string



print(reverse(None))  # Example usage
