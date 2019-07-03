import numpy as np
from typing import Tuple


def calculate_paths(shape: Tuple[int, int], point: Tuple[int, int]) -> int:
	"""Given field with size rows*cols count available paths from (0, 0) to point
	:param shape: tuple of rows and cols (each from 1 to rows/cols)
	:param point: desired point for horse
	:return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)"""
	n, m = map(int, input().split())
	f = [[0] * (m+1) for i in range(n+1)]
	f[1][1] = 1
	for i in range(2, n+1):
		for j in range(2, m + 1):
			f[i][j] = f[i-2][j-2] + f[i-2][j-1]
	return n + m
