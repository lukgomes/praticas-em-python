var1 = int(input("Digite o primeiro valor: "))

while True:
    var2 = int(input("Digite o segundo valor: "))
    if (var2 > 0):
        break
    print("Informe um valor maior que zero.")        

print(f"A soma entre {var1} e {var2} é igual a {var1 + var2}")
print(f"A subtração entre {var1} e {var2} é igual a {var1 - var2}")
print(f"A multiplicação entre {var1} e {var2} é igual a {var1 * var2}")
print(f"A divisão entre {var1} e {var2} é igual a {var1 / var2}")