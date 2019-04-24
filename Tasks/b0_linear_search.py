"""
This module implements some functions based on linear search algo
"""

"""Function that find minimal element in array
:param arr: Array containing numbers
:return: index of first occurrence of minimal element in array"""

arr = [17, 4, 1, 3, 4, 6, 2, 9, 11, 18]


# def min_search(arr) -> int:
# 	v = arr[0]
# 	for i in arr:
# 		if v < i:
# 			pass
# 		else:
# 			v = i
# 	return arr.index(v)


def min_search(arr) -> int:
	m = arr[0]
	n = 0
	for i in range(len(arr)):
		if arr[i] < m:
			m = arr[i]
			n = i
	return n

# def min_search(arr) -> int:
# 	m = arr[0]
# 	n = 0
# 	for i in arr:
# 		if i < m:
# 			m = arr[i]
# 			n = [i]
# 	return n











