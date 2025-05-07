"""
Solicita o número de lançamentos (N);

Simula os lançamentos de um dado de 6 faces;

Mostra estatísticas básicas, como:

Total de lançamentos

Frequência de cada face (1 a 6)

A face mais frequente

A média dos resultados
"""

import random

quant = int(input("quantas vezes jogar o dado: "))
face = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}

for i in range(quant):
    dado = random.randrange(1, 7)
    print(dado)
    match dado:
        case 1:
            face['1'] += 1
        case 2:
            face['2'] += 1
        case 3:
            face['3'] += 1
        case 4:
            face['4'] += 1
        case 5:
            face['5'] += 1
        case 6:
            face['6'] =+ 1

print(f"total de lançamentos: {quant}")
for key, value in face.items():
    if value > 0:
        print(f"Face {key} apareceu {value} vezes")
    
    

    