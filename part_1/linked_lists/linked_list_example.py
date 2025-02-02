class Node:
	def __init__(self, data):
		self.data = data  # Data stored in the node
		self.next = None  # Pointer to the next node


class LinkedList:
	def __init__(self):
		self.head = None  # Head of the linked list

	def append(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			current = self.head

			while current.next:
				current = current.next
			current.next = new_node

	def __str__(self):
		if not self.head:  # Handle the case where the list is empty
			return "None"
		nodes = []
		current = self.head
		while current:
			nodes.append(str(current.data))
			current = current.next
		return " -> ".join(nodes) + " -> None"


# Create a linked list
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

# Print the linked list
print(ll)  # Output: 1 -> 2 -> 3 -> 4 -> None
