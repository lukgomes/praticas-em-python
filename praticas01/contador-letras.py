complete_string = input("Digite uma palavra ou frase: ")

contador = 0

for letter in complete_string:
    if (letter != " "):
        contador += 1

print(f"A palavra ou frase possui {contador} letras.\nOBS: Não foi contado os espaços em branco.")