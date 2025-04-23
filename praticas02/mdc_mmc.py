def mdc(num1, num2):
    if num1 > num2:
        dividendo = num1
        divisor = num2
    else:
        dividendo = num2
        divisor = num1
    
    while True:
        res = dividendo % divisor
        if res == 0:
            return divisor
        else:
            dividendo = divisor
            divisor = res


def mmc(num1, num2):
    res_mdc = mdc(num1, num2)
    return int(num1 * (num2 / res_mdc))
    pass


valor1 = 16
valor2 = 40
print(mdc(valor1, valor2))
print(mmc(valor1, valor2))