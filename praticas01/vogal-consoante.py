vogais = ['a', 'e', 'i', 'o', 'u']
letter = input("Digite uma letra: ")

if (letter[0] in vogais):
    print(f"A letra '{letter}' é uma vogal.")
else:
    print(f"A letra '{letter}' é uma consoante.")
