"""Priority Queue
Queue priorities are from 0 to 5"""

my_stack = []

"""Operation that add element to the end of the queue
:param elem: element to be added
:return: Nothing"""

def enqueue(elem, priority: int = 0) -> None:
	global my_stack
	elem.append(my_stack)
	return None


"""Return element from the beginning of the queue
:return: dequeued element"""

def dequeue():
	global my_stack
	a = 1

	return a

"""Allow you to see at the element in the queue without dequeuing it
:param ind: index of element (count from the beginning)
:return: peeked element"""
def peek(ind: int = 0, priority: int = 0):

	return None

"""Clear my queue
:return: None"""
def clear() -> None:


	return None
