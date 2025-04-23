word = input("Informe uma palavra para chegar se é um palindromo: ").lower()
drow = []
qtda = len(word)


while (qtda > 0):
    drow.append(word[qtda - 1])
    qtda -= 1

if (word == ''.join(drow)):
    print("Essa palavra é um palindromo.")
else:
    print("Essa palavra não é um palindromo.")