from guizero import App, Box, PushButton, Text

# Fonctions --------------------------------------------------------------------

def clear_board():
    new_board=[[None,None,None],[None,None,None],[None,None,None]]
    for x in range(3):
        for y in range(3):
            button = PushButton(board, text="",grid=[x,y],width=3,command=choose_square,args=[x,y])
            new_board[x][y]=button
    return new_board

def choose_square(x,y):
    board_squares[x][y].text=turn
    board_squares[x][y].disable()
    changement_j()
    check_win()

def changement_j():
    global turn
    if turn=="X":
        turn="O"
    else:
        turn="X"
    message.value="C'est à ton tour, joueur "+turn

def check_win():
    winner = None
    #Lignes verticales
    if board_squares[0][0].text == board_squares[0][1].text == board_squares[0][2].text and board_squares[0][0].text != "":
        winner = board_squares[0][0]
    elif board_squares[1][0].text == board_squares[1][1].text == board_squares[1][2].text and board_squares[1][0].text != "":
        winner = board_squares[1][0]
    elif board_squares[2][0].text == board_squares[2][1].text == board_squares[2][2].text and board_squares[2][0].text != "":
        winner = board_squares[2][0]

    #lignes horizontales
    elif board_squares[0][0].text == board_squares[1][0].text == board_squares[2][0].text and board_squares[0][0].text != "":
        winner = board_squares[0][0]
    elif board_squares[0][1].text == board_squares[1][1].text == board_squares[2][1].text and board_squares[0][1].text != "":
        winner = board_squares[0][1]
    elif board_squares[0][2].text == board_squares[1][2].text == board_squares[2][2].text and board_squares[0][2].text != "":
        winner = board_squares[0][2]

    #lignes diagonales
    elif board_squares[0][0].text == board_squares[1][1].text == board_squares[2][2].text and board_squares[0][0].text != "":
        winner = board_squares[0][0]
    elif board_squares[2][0].text == board_squares[1][1].text == board_squares[0][2].text and board_squares[2][0].text != "":
        winner = board_squares[2][0]

    if winner != None:
        message.value=winner.text+' a gagné !'

    elif moves_taken()==9:
        message.value="Match nul !"

def moves_taken():
    moves=0
    for row in board_squares:
        for col in row:
            if col.text=="X" or col.text=="O":
                moves+=1
    return moves

# Variables --------------------------------------------------------------------
turn ="X"

# App --------------------------------------------------------------------------
app=App("Morpion",200,170,"auto",None,True)
board=Box(app,layout="grid")
board_squares=clear_board()
#print(board_squares)
message=Text(app,text="C'est à ton tour, joueur "+turn)

print("Démarrage de l'application graphique !")
app.display()