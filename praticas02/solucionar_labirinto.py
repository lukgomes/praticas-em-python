def resolver_labirinto_iterativo(labirinto):
    N = len(labirinto)
    M = len(labirinto[0])
    visitado = [[False for _ in range(M)] for _ in range(N)]

    # Pilha: cada item é (x, y, caminho_percorrido)
    pilha = [(0, 0, [])]

    while pilha:
        x, y, caminho = pilha.pop()

        # Se fora dos limites ou parede ou já visitado, ignora
        if x < 0 or x >= N or y < 0 or y >= M:
            continue
        if labirinto[x][y] == 1 or visitado[x][y]:
            continue

        visitado[x][y] = True
        caminho = caminho + [(x, y)]

        # Se chegou ao final
        if (x, y) == (N - 1, M - 1):
            imprimir_caminho_visual(labirinto, caminho)
            print("\nCoordenadas do caminho:")
            print(caminho)
            return True

        # Adiciona vizinhos na pilha (ordem: baixo, direita, cima, esquerda)
        pilha.append((x + 1, y, caminho))
        pilha.append((x, y + 1, caminho))
        pilha.append((x - 1, y, caminho))
        pilha.append((x, y - 1, caminho))

    print("Não há caminho possível.")
    return False


def imprimir_caminho_visual(labirinto, caminho):
    N = len(labirinto)
    M = len(labirinto[0])
    grade = [[' ' for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if labirinto[i][j] == 1:
                grade[i][j] = '#'

    for x, y in caminho:
        grade[x][y] = '*'

    print("Caminho visual:")
    for linha in grade:
        print(''.join(linha))


# --- Labirinto complexo (10x10) ---
labirinto = [
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
]

# --- Executar o resolvedor ---
resolver_labirinto_iterativo(labirinto)
