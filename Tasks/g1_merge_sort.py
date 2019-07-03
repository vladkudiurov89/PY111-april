from typing import Sequence, TypeVar

_Tt = TypeVar("T")


def sort(container: Sequence[_Tt]) -> Sequence[_Tt]:
	"""Sort input container with merge sort
	:param container: container of elements to be sorted
	:return: container sorted in ascending order"""
	a = len(container)
	if a <= 1:
		return container

	x = sort(container[:a // 2])
	y = sort(container[a // 2: a])
	j = 0
	i = 0
	b = []
	while i < len(x) or j < len(y):
		if not i < len(x):
			b.append(y[j])
			j += 1
		elif not j < len(y):
			b.append(x[i])
			i += 1
		else:
			b.append(y[j])
			j += 1
	return b

