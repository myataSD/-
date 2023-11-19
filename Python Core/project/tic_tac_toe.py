import random

def draw_board(board):
        print(f"""                {board[0]} | {board[1]} | {board[2]}
                --|---|--
                {board[3]} | {board[4]} | {board[5]}
                --|---|--
                {board[6]} | {board[7]} | {board[8]}""")

def get_player_move(board, player_symbol):
    while True:
        try:
            move = int(input(f"Игрок '{player_symbol}', введите номер ячейки (1-9): "))
            if 1 <= move <= 9  and board[move - 1] == ' ':
                return move - 1
            else:
                print("error")
        except ValueError:
                print("Введите число")

def get_computer_move(board):
    empty_cells = [i for i in range(9) if board[i] == ' ']
    return random.choice(empty_cells)
    

def check_win(board, symbol):
    for i in range(3):
        if all(board[i*3 + j] == symbol for j in range(3)) or \
           all(board[i + j*3] == symbol for j in range(3)):
            return True
    if all(board[i] == symbol for i in [0, 4, 8]) or \
       all(board[i] == symbol for i in [2, 4, 6]):
        return True
    return False

def main(): 
    board = [' '] * 9
    choose_symbol = input("Введите за какую  сторону вы буддте играть (X или O): ")
    if  choose_symbol == 'X':    
        players = [(f'Игрок {choose_symbol}', f'{choose_symbol}'), ('Компьютер O', 'O')]
    elif choose_symbol == 'O':
         players = [('Компьютер X', 'X'), (f'Игрок {choose_symbol}', f'{choose_symbol}')]
    else: 
        print("Введите X или O!")
        main()

    draw_board(board)

    for turn in range(9):
        player_name, symbol = players[turn % 2]
        
        
        if player_name == f'Игрок {choose_symbol}':
            move = get_player_move(board, symbol)
        else:
            move = get_computer_move(board)


        board[move] = symbol
        draw_board(board)

        if check_win(board, symbol):
            print(f"{player_name} победил!")
            break
    else:
        print("Ничья!")
        
    
main()   