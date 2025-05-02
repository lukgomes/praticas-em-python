fruits = ["banana", "maçã", "laranja", "uva", "abacaxi"]

def busca_sequencial(lista, item):
    for i in range(len(lista)):
        print(lista[i])
        if item == lista[i]:
            return f"Fruta {item} encontrado na lista na posição {i}"
    return f"Fruta {item} não encontrado na lista"
        

print(busca_sequencial(fruits, "uva"))
print(busca_sequencial(fruits, "pera"))