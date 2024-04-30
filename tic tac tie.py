
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    #Ta część kodu sprawdza rzędy
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
        
    #Ta część kodu sprawdza kolumny
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
        
        #Ta część kodu sprawdza przekątne
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return board[0][0]
        
        return None
    
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("Zagrajmy w kolko i krzyzyk!")
    print_board(board)

    while True:
        row = int(input("Wybierz rzad (0, 1, 2): "))
        col = int(input("Wybierz kolumne (0, 1, 2): "))

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Nie mozesz tego tak robic! Sprobuj ponownie.")
            continue

        board[row][col] = player
        print_board(board)

        winner = check_winner(board)
        if winner:
            print("Gracz {player} wygrywa!")
            break
        elif is_board_full(board):
            print("Remis!")
            break

        player = "0" if player == "X" else "X"
