from os import *

DOLAR = 5.66
EURO = 6.3

while True:
    system('clear')
    print('Conversor de moedas')
    dinheiro = float(input('informe o valor em real: '))

    print(f'o valor de R$ {dinheiro} em dolar é US$ {(DOLAR * dinheiro):.2f}')
    print(f'O valor de R$ {dinheiro} em euro é {(EURO * dinheiro):.2f}')
    input()