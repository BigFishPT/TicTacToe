import random

#mostra o tabuleiro
def display_board(board):
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("--|---|--")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("--|---|--")
    print(board[7] + " | " + board[8] + " | " + board[9])

#escolhe o apontador
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input("Jogador 1 queres ser 'X' ou 'O'").upper()

    if marker == 'X':
        player1 ="X"
        player2="O"
        return (player1, player2)
    else:
        player1 ="O"
        player2="X"
        return (player1,player2)

#coloca o marcador na posição
def place_marker(board, marker, position):
    board[position]=marker

#verifica se a ganhou
def win_check(board, mark):
    return((board[1] == mark and board[2] == mark and board[3] == mark) or
          (board[4] == mark and board[5] == mark and board[6] == mark) or
          (board[7] == mark and board[8] == mark and board[9] == mark) or
          (board[1] == mark and board[4] == mark and board[7] == mark) or
          (board[2] == mark and board[5] == mark and board[8] == mark) or
          (board[3] == mark and board[6] == mark and board[9] == mark) or
          (board[1] == mark and board[5] == mark and board[9] == mark) or
          (board[3] == mark and board[5] == mark and board[7] == mark))

#escolhe quem joga primeiro
def choose_first():
    if random.randint(0,1) == 0:
        return "Jogador 1"
    else:
        return "Jogador 2"

#verifica se a posição esta livre
def space_check(board, position):
    return board[position] == " "

#verifica se ainda ha posições livre
def full_board_check(board):
    for space in range(1,10):
        if space_check(board,space):
            return False
    return True

#pede e valida proxima posição
def player_choice(board):
    position = -1
    while position not in  [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Escolhe a proxima posição: (1-9) '))
    return position

# pergunta se quer jogar de novo
def replay():
     return input("Queres jogar de novo? (S)(N)").lower().startswith('s')

#ciclo principal 
print("Bem vindo Jogo do Galo em Python - by Milagre de Deus \n")

while True:
    myBoard = [" "]*10
    player1,player2 = player_input()
    turn = choose_first()
    print(turn + " é o primeiro a jogar ! \n")
    jogar = True
    
    while jogar:
        if turn == "Jogador 1":
            print("É a tua vez " + turn)
            display_board(myBoard)
            posicao = player_choice(myBoard)
            place_marker(myBoard,player1,posicao)
            
            if win_check(myBoard,player1):
                display_board(myBoard)
                print("Parabens Jogador 1 , ganhas-te o jogo \n")
                jogar = False
            else:
                if full_board_check(myBoard):
                    display_board(myBoard)
                    print("O jogo ficou empatado.. \n")
                    break
                else:
                    turn = "Jogador 2"
                    
                    
        if turn == "Jogador 2":
            print("É a tua vez " + turn)
            display_board(myBoard)
            posicao = player_choice(myBoard)
            place_marker(myBoard,player2,posicao)
            
            if win_check(myBoard,player2):
                display_board(myBoard)
                print("Parabens Jogador 2 , ganhas-te o jogo \n")
                jogar = False
            else:
                if full_board_check(myBoard):
                    display_board(myBoard)
                    print("O jogo ficou empatado.. \n")
                    break
                else:
                    turn = "Jogador 1"
                    
    if not replay():
        break