import time

inicio = int(input("Informe o numero inicial da contagem: "))
fim = int(input("Informe o numero final da contagem: "))

def show_valor(inicio):
    print(inicio)
    time.sleep(.1)

if (inicio < fim):
    while True:
        show_valor(inicio)
        inicio += 1
        if (inicio > fim):
            break


elif (inicio > fim):
    while True:
        show_valor(inicio)
        inicio -= 1
        if (inicio < fim):
            break