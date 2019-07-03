from typing import Optional, List


def kmp_algo(inp_string: str, substr: str) -> Optional(int):
	"""Implementation of Knuth-Morrison-Pratt algorithm
	:param inp_string: String where substr is to be found (haystack)
	:param substr: substr to be found in inp_string (needle)
	:return: index where first occurrence of substr in inp_string started or None if not found"""

	def prefix_fun(prefix_str: str) -> List[int]:
		"""Prefix function for KMP
		:param prefix_str: dubstring for prefix function
		:return: prefix values table"""
		prefix_str = [0] * len(inp_string)
		for i in range(1, len(prefix_str)):
			j = prefix_str[i - 1]
			while j > 0 and prefix_str != inp_string[i]:
				j = prefix_str[j-1]
			if prefix_str == inp_string:
				j += 1
			prefix_str[i] = j
		print(prefix_str)
		return []

	print(inp_string, substr, prefix_fun)
	return None
