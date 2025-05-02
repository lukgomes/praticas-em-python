import random


def embaralhar_string_manual(s):
    letras = list(s)  # Converte a string em uma lista de caracteres
    tamanho = len(letras)
    for i in range(tamanho):
        # Escolhe um índice aleatório
        j = random.randint(0, tamanho - 1)
        # Troca as letras nas posições i e j
        letras[i], letras[j] = letras[j], letras[i]
    return ''.join(letras)  # Junta os caracteres de volta em uma string

# Exemplo de uso
string_original = "hipopotomonstrosescpedaliofobia"
string_embaralhada = embaralhar_string_manual(string_original)

print("Original:", string_original)
print("Embaralhada:", string_embaralhada)
