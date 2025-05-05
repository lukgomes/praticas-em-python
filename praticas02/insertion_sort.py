import random


def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = chave

numbers = random.sample(range(1, 1000), 42)
# numbers = [4, 7, 2, 5, 4, 0]


# print(f'Unordered list\n {numbers}')
# insertion_sort(numbers)
# print(f'Ordered list\n {numbers}')