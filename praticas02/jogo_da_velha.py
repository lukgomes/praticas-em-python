import os

board_game = [['_','_','_'], ['_','_','_'], ['_','_','_']]

def show_board(board_game):
    print("      1    2    3")
    row = 1
    for board in board_game:
        print(f"{row} - {board}")
        row += 1
    print('\n')

def play(row, col, letter):
    board_game[row][col] = letter

def jogador(letter):
    print(f"Jogador {letter}")
    while True:
        row = int(input("Em qual linha deseja jogar: "))
        col = int(input("Em qual coluna deseja jogar: "))
        if row >= 1 and row <= 3 and col >= 1 and col <= 3:
            break
        else:
            print("Valores incorretos, tente novamente...")
    os.system('clear')
    return row - 1, col -1 

def verifica_vencedor(board_game, letter):
    if "_" in board_game:
        print('Deu veia!')
        return 'end'
    elif (board_game[0][0] == letter and board_game[0][1] == letter and board_game[0][2] == letter) or (board_game[1][0] == letter and board_game[1][1] == letter and board_game[1][2] == letter) or (board_game[2][0] == letter and board_game[2][1] == letter and board_game[2][2] == letter) or (board_game[0][0] == letter and board_game[1][0] == letter and board_game[2][0] == letter) or (board_game[0][1] == letter and board_game[1][1] == letter and board_game[2][1] == letter) or (board_game[0][2] == letter and board_game[1][2] == letter and board_game[2][2] == letter) or (board_game[0][0] == letter and board_game[1][1] == letter and board_game[2][2] == letter) or (board_game[2][0] == letter and board_game[1][1] == letter and board_game[0][2] == letter):
        print(f'Jogador {letter} ganhou.')
        return 'end'

if __name__ == "__main__":
    while True:
        while True:
            os.system('clear')
            show_board(board_game)
            row, col = jogador("X")
            if board_game[row][col] == '_':
                play(row, col, "X")
                test = verifica_vencedor(board_game, 'X')
                break
        if test == 'end':
            break
        
        while True:
            os.system('clear')
            show_board(board_game)
            row, col = jogador("O")
            if board_game[row][col] == '_':
                play(row, col, "O")
                test = verifica_vencedor(board_game, 'O')
                break
        if test == 'end':
            break
