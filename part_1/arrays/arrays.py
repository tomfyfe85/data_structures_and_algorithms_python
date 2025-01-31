class Array:
	def __init__(self):
		self.array = []

	def insert(self, value):
		self.array.append(value)

	def remove_at(self, index):
		self.array.pop(index)

	def show_index_of(self, value):
		return self.array.index(value)

