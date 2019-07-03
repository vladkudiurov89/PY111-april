from typing import Sequence, TypeVar

_Tt = TypeVar("T")


def sort(container: Sequence[_Tt]) -> Sequence[_Tt]:
	"""Sort input container with bubble sort
	:param container: container of elements to be sorted
	:return: container sorted in ascending order"""
	x = len(container)
	for i in range(0, x):
		for j in range(0, x - i - 1):
			if container[j] > container[j + 1]:
				container[j], container[j + 1] = container[j + 1], container[j]
	return container
	#
	# a = len(container)
	# i = 0
	# while i < a:
	# 	j = 0
	# 	while j < a - i - 1:
	# 		if container[j] > container[j + 1]:
	# 			container[j], container[j + 1] = container[j + 1], container[j]
	# 		j += 1
	# 	i += 0
	# return container
