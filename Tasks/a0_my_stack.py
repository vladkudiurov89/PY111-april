"""My little Stack"""

my_stack = []

"""Operation that add element to stack
:param elem: element to be pushed
:return: Nothing"""


def push(elem):
	global my_stack
	my_stack.append(elem)
	return None


"""Pop element from the top of the stack
:return: popped element"""


def pop():
	global my_stack
	if len(my_stack) != 0:
		b = my_stack[-1]
		del my_stack[-1]
		return b
	else:
		return None


"""Allow you to see at the element in the stack without popping it
:param ind: index of element (count from the top)
:return: peeked element"""

def peek(ind: int = 0):
	global my_stack
	b = ind + 1
	return my_stack[-b]



"""Clear my stack
:return: None"""

def clear() -> None:
	global my_stack
	my_stack.clear()
	return None


if __name__ == '__main__':
	push(2)
	push(1)
	print(my_stack)
	print(pop())
	print(my_stack)
	print(pop())