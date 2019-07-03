def binary_search(elem, arr, x=0, y=None):
	"""Performs binary search of given element inside of array (using recursive way)
	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise"""
	if y is None:
		y = len(arr) - 1
	if y < x:
		return None
	z = (x + y) // 2

	if arr[z] == elem:
		return z
	elif elem > arr[z]:
		return binary_search(elem, arr, z+1, y)
	elif elem < arr[z]:
		return binary_search(elem, arr, x, z-1)

