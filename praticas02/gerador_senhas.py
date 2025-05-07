import string
import random

caracteres_pass = list()
caracteres_pass = list(string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation)
password = list()

quant = int(input("quantos caracteres voce deseja na sua senha: "))
if quant <= 7:
    quant = 8

for i in range(0, quant):
    index = random.randint(0, len(caracteres_pass))
    password.append(caracteres_pass[index])

senha = ''.join(password)
print(senha)