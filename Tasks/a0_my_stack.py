"""My little Stack"""

a = []

"""Operation that add element to stack
:param elem: element to be pushed
:return: Nothing"""


def push(elem):
	global a
	a.append(elem)
	return None


"""Pop element from the top of the stack
:return: popped element"""


def pop():
	global a
	return a.pop()


def peek(ind: int = 0):

	"""Allow you to see at the element in the stack without popping it
	:param ind: index of element (count from the top)
	:return: peeked element"""
	return None


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	return None


if __name__ == '__main__':
	push(2)
	push(1)
	print(a)
	print(pop())
	# print(a)
	print(pop())