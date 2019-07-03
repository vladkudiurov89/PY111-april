from typing import Sequence, TypeVar
import random
_Tt = TypeVar("T")


def sort(container: Sequence[_Tt]) -> Sequence[_Tt]:
	"""Sort input container with quick sort
	:param container: container of elements to be sorted
	:return: container sorted in ascending order"""
	if len(container) <= 1:
		return container
	else:
		x = random.choice(container)
	a = [i for i in container if i < x]

	set = [x] * container.count(x)
	b = [i for i in container if i > x]
	return sort(a) + set + sort(b)

