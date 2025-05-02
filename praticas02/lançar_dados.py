import random

def lancar_dados():
    face1 = random.randint(1, 6)
    face2 = random.randint(1, 6)
    return face1, face2


dado1, dado2 = lancar_dados()

print(f"dado 1: {dado1}\ndado 2: {dado2}")
print(f"A soma dos valores é {dado1 + dado2}")