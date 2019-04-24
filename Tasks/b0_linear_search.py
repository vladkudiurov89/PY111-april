"""
This module implements some functions based on linear search algo
"""

"""Function that find minimal element in array
:param arr: Array containing numbers
:return: index of first occurrence of minimal element in array"""

arr = [1, 3, 4, 6, 2, 9, 11, 18]


def min_search(arr) -> int:
	v = arr[0]
	for i in arr:
		if v < i:
			pass
		else:
			v = i

	return arr.index(v)


min_search()



def min_weight_search(Graph) -> tuple:
	"""
	Function that find edge in graph with minimal weight of all

	:param Graph: NetworkX Graph (or digraph) with weighted edges
	:return: tuple of nodes (node, node) the weight of edge between which is minimal (any occurrence)
	"""

	return None, None

if __name__ == '__main__':
    min_search(5)