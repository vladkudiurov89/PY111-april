"""Priority Queue
Queue priorities are from 0 to 5"""


my_queue = [[], [], [], [], [], []]


def enqueue(elem, priority: int = 0) -> None:
	"""Operation that add element to the end of the queue
	:param priority:
	:param elem: element to be added
	:return: Nothing"""
	my_queue[priority].append(elem)
	return None


def dequeue():
	"""Return element from the beginning of the queue
	:return: dequeued element"""
	global my_queue
	for i in range(len(my_queue)):
		if my_queue[i]:
			elem = my_queue[i][0]
			del my_queue[i][0]
			return elem


def peek(ind: int = 0, priority: int = 0):
	"""Allow you to see at the element in the queue without dequeuing it
	:param priority:
	:param ind: index of element (count from the beginning)
	:return: peeked element"""
	try:
		return my_queue[priority][ind]
	except IndexError:
		return None


def clear() -> None:
	"""Clear my queue
	:return: None"""
	global my_queue
	for i in range(len(my_queue)):
		if my_queue[i]:
			my_queue[i].clear()
		return None
