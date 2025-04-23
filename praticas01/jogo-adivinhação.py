import random

num = random.randint(0, 99)
player = 0
tentativas = 0

while True:
    tentativas += 1
    player = int(input("Informe um numero para comparação: "))
    if (player > num):
        print("O número informado é maior que a resposta, tente algo menor.")
    elif (player < num):
        print("O número informado é menor que a resposta, tente algo maior.")
    else:
        break

print(f"Parabens!\nVoce acertou, o número sorteado foi {num}\nE levou {tentativas} tentativas.")