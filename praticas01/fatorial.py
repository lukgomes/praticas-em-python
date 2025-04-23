num = int(input("Informe um número para calcular o fatorial: "))
fatorial = 1
cont = num
while(cont > 1):
    fatorial *= num
    num -= 1

print (f"O fatorial de {num} é {fatorial}")