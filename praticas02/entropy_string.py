import random

words = "otorrinolaringologista"
new_word = []
cont = 0

while True:
    pos = random.randint(0, len(words) - 1)
    new_word.append(words[pos])
    print(pos)
    cont += 1
    if cont == 10:
        break

print(words)
print(new_word)