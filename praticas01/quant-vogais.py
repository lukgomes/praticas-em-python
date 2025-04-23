vogais = ['a', 'e', 'i', 'o', 'u']
word = input("Informe uma palavra para ser contada as vogais: ")
cont = 0
for letter in word:
    if letter in vogais:
        cont += 1

print (f"Na palavra {word} existem {cont} vogais.")