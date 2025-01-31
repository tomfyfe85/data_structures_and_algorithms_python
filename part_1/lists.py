# assume nums[0] is smallest



# def find_min_index(nums):
# 	smallest = nums[0]
# 	index_of_smallest = 0
#
# 	for k, v in enumerate(nums[1:]):
# 		if v < smallest:
# 			smallest = v
# 			index_of_smallest = k
#
# 	return index_of_smallest
#
# print(find_min_index([10, 20, 5, 3, 8]))



def remove_duplicates(nums):
	no_dups = []
	for num in nums:
	 	if num not in no_dups:
			no_dups.append(num)
	return no_dups


print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))