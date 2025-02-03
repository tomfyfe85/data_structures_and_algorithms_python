from operator import indexOf


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.first = None
		self.last = None

	def add_first(self, data: int):
		new_node = Node(data)
		new_node.next = self.first
		self.first = new_node

		if not self.last:
			self.last = new_node

	def add_last(self, data: int):
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

	def contains(self, item: int):
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
				return i
			current = current.next
			i += 1

		print("item not found")

	def reverse(self):

		current = self.first
		prev = None

		while current is not None:
			next_node = current.next
			current.next = prev
			prev = current
			current = next_node

		self.last = self.first
		print(self.last.next)
		self.first = prev

	def show_list(self):
		result = []
		current = self.first
		while current:
			result.append(current.data)
			current = current.next
		return result

	def get_kth_from_the_end(self, k: int ):
# 		declare two pointers
#		one starts from the beginning of the list (p1)
#		next one starts k -1 from the beginning (p2)
#		when p1 reaches the end node - give the position of p2
		pass

ll = LinkedList()
ll.add_last(10)
ll.add_last(20)
ll.add_last(30)
ll.add_last(40)
ll.add_last(50)

print(ll.get_kth_from_the_end(1))