def fib_recursive(n: int) -> int:
    """Calculate n-th number of Fibonacci sequence using recursive algorithm
	:param n: number of item
	:return: Fibonacci number"""
    if n < 0 or type(n) == float:
        raise ValueError
    if n < 3:
        return 1
    return fib_iterative(n - 1) + fib_iterative(n - 2)


def fib_iterative(n: int) -> int:
    """Calculate n-th number of Fibonacci sequence using iterative algorithm
	:param n: number of item
	:return: Fibonacci number"""
    if n < 0 or type(n) == float:
        raise ValueError
    fib_1 = fib_2 = 1
    num = 2
    fib_sum = None
    while num < n:
        fib_sum = fib_2 + fib_1
        fib_1 = fib_2
        fib_2 = fib_sum
        num += 1
    return fib_sum
