
board_game = [['_','_','_'], ['_','_','_'], ['_','_','_']]


def show_board(board_game):
    print("      1    2    3")
    row = 1
    for board in board_game:
        print(f"{row} - {board}")
        row += 1
    print('\n')

def play(row, col, letter):
    board_game[row - 1][col - 1] = letter

def jogador(letter):
    row = int(input("Em qual linha deseja jogar: "))
    col = int(input("Em qual coluna deseja jogar: "))
    play(row, col, letter)


if __name__ == "__main__":
    while True:
        show_board(board_game)
        print("Jogador X")
        jogador("X")
        show_board(board_game)
        print("Jogador O")
        jogador("O")
        