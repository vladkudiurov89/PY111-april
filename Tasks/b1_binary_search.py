
def binary_search(elem, arr):
    """Performs binary search of given element inside of array
    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise"""

    x = 0
    y = len(arr)

    while x <= y:
        z = (x + y) // 2
        if elem < arr[z]:
            y = z - 1
        elif elem > arr[z]:
            x = z + 1
        else:
            return z



