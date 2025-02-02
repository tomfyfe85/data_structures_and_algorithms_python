class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.first = None
		self.last = None

	def add_first(self, data):
		new_node = Node(data)
		new_node.next = self.first
		self.first = new_node

		if not self.last:
			self.last = new_node

	def add_last(self, data):
		new_node = Node(data)

		if not self.first:
			self.first = self.last = new_node
		else:
			current = self.first

			while current.next:
				current = current.next
			current.next = new_node
			self.last = new_node

	def delete_first(self):
		if not self.first:
			print('list empty')
			return

		if not self.first.next:
			self.first = self.last = None
		else:
			self.first = self.first.next

	def delete_last(self):
		if not self.first:
			print('list empty')
			return

		if not self.first.next:
			self.first = self.last = None
			return

		current = self.first
		while current.next.next:
			current = current.next
		self.last = current
		current.next = None

	def contains(self, item):
		current = self.first
		while current:
			if current.data == item:
				print("true")
				return True
			current = current.next
		print("false")
		return False

	def	index_of(self, item):
		current = self.first
		i = 0
		while current:
			if current.data == item:
				print(i)
				return
			current = current.next
			i += 1

		print("item not found")



ll = LinkedList()
ll.add_last(1)
ll.add_last(2)
ll.add_last(3)
ll.add_last(4)

ll.index_of(4)
ll.index_of(10)