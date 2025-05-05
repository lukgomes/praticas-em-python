
def binary_search(array, number, begin = 0, end=None):
    if end is None:
        end = len(array) - 1
    if begin <= end:
        m = (begin + end) // 2
        if array[m] == number:
            return m
        if number < array[m]:
            return binary_search(array, number, begin, m - 1)
        else:
            return binary_search(array, number, m + 1, end)
    else:
        return None


numbers = [0,10,15,25,45,84,105,210,324,400]
print(f'same list\n\t{numbers}')

print(f"o numero foi encontrado na posição {binary_search(numbers, 324)}")