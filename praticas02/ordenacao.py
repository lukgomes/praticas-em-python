list_numbers = [5, 15, 2, 78, 96, 35, 3, 100, 1, 65, 43]
aux = 0

for x in range(len(list_numbers)):
    for y in range(x + 1, len(list_numbers)):
        if list_numbers[x] > list_numbers[y]:
            aux = list_numbers[x]
            list_numbers[x] = list_numbers[y]
            list_numbers[y] = aux


print(list_numbers)