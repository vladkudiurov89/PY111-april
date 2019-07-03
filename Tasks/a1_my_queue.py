"""My little Queue"""

little_queue = []


def enqueue(elem) -> None:
	"""Operation that add element to the end of the queue
	:param elem: element to be added
	:return: Nothing"""
	if little_queue is not None:
		little_queue.append(elem)


def dequeue():
	"""Return element from the beginning of the queue
	:return: dequeued element"""
	if little_queue:
		return little_queue.pop(0)


def peek(ind: int = 0):
	"""Allow you to see at the element in the queue without dequeuing it
	:param ind: index of element (count from the beginning)
	:return: peeked element"""
	try:
		return little_queue[ind]
	except IndexError:
		return None

def clear() -> list:
	"""Clear my queue
	:return: None"""
	little_queue.clear()
	return None

