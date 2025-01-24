# assume nums[0] is smallest



def find_min_index(nums):
	smallest = nums[0]
	index_of_smallest = 0

	for k, v in enumerate(nums[1:]):
		if v < smallest:
			smallest = v
			index_of_smallest = k

	return index_of_smallest

print(find_min_index([10, 20, 5, 3, 8]))
