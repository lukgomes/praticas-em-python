fibonacci = [0 ,1]
quant = int(input("Informe a quantidade de numeros a ser exibido da sequencia fibonacci: "))

while True:
    fibonacci.append(fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2])
    quant -= 1
    if quant == 0:
        break


print(fibonacci)