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

for i in range(quant):
    dado = random.randrange(1, 7)
    print(dado)
    if dado == 1:
        pass