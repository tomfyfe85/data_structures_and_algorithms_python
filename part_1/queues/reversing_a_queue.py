from collections import deque

# add / remove / isEmpty only

def reverse(queue):
	stack = deque()
	while queue:
		stack.appendleft(queue.pop())
	while stack:
		queue.append(stack.pop())

	# for num in stack:
	# 	queue.
	return queue


q = deque()
q.append(10)  # Add to the right (end)
q.append(20)
q.append(30)
print(reverse(q))