import time

num = 29
res = []
div = num

while True:
    res.insert(0, div % 2)
    div = int(div / 2)
    if div == 0 :
        break

decimal_number = map    (str, res)
print(''.join(decimal_number))