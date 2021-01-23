
firstPlayer = input('x or o')
PlayerDefined = False
rows = ['#','1','2','3','4','5','6','7','8','9']
gameActive = True
Moves = 0

#definir los jugadores
while PlayerDefined == False:
    if firstPlayer == 'x':
        secondPlayer = 'o'
        PlayerDefined = True
    elif firstPlayer == 'o':
        secondPlayer = 'x'
        PlayerDefined = True
    else:
        firstPlayer = input('x or o')
        PlayerDefined = False
print(secondPlayer)


def display():
    print('\n' * 100)
    print(rows[1] + '|' + rows[2] + '|' + rows[3])
    print('------')
    print(rows[4] + '|' + rows[5] + '|' + rows[6])
    print('------')
    print(rows[7] + '|' + rows[8] + '|' + rows[9])
    # print(' '.join(rows[1:4]))
    #print(' '.join(rows[4:7]))
    #print(' '.join(rows[7:10]))
    
display()
def PlayerInput():
    Choice = 'WRONG'
    AcceptableRange = range(1,10)
    withinRange = False
    isTaken = False
    
    while Choice.isdigit() == False or withinRange == False or isTaken == False:
        Choice = input('Pick a number (1-9): ')
        if Choice.isdigit() == False:
            print('Sorry that is not a valid number')
        if Choice.isdigit() == True:
                if int(Choice) in AcceptableRange:
                    withinRange = True
                    if rows[int(Choice)] == 'x' or rows[int(Choice)] == 'o':
                        isTaken = False
                        print('Sorry, this spot is taken')
                    else:
                        isTaken = True
                        return int(Choice)

                elif int(Choice) == 69:
                    print('nice but no')
                    withinRange = False
                else:
                    withinRange = False
                    print('Sorry that is not a valid number')


def CheckIfWinner(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or # horizontal superior
            (board[4] == mark and board[5] == mark and board[6] == mark) or # horizontal medio
            (board[7] == mark and board[8] == mark and board[9] == mark) or # horizontal inferior
            (board[1] == mark and board[4] == mark and board[7] == mark) or # vertical izquierda
            (board[2] == mark and board[5] == mark and board[8] == mark) or # vertical medio
            (board[3] == mark and board[6] == mark and board[9] == mark) or # vertical derecha
            (board[1] == mark and board[5] == mark and board[9] == mark) or # diagonal
            (board[7] == mark and board[5] == mark and board[3] == mark)) # diagonal
#def CheckIfTie(moves):
 #   moves = moves + 1
  #  return moves == 9

#Movimientos de los jugadores
def FirstPlayerMove():
    position = PlayerInput()
    rows[position] = firstPlayer

def SecondPlayerMove():
    Pos = PlayerInput()
    rows[Pos] = secondPlayer


#Juego Activo
while gameActive == True:
    FirstPlayerMove()
    Moves = Moves + 1
    display()
    if CheckIfWinner(rows, firstPlayer):
        print('Congratulations ' + firstPlayer + ' you have won the game' )
        break
    if Moves == 9:
        print('The game ends with a tie, no more possible moves')
        break
    SecondPlayerMove()
    Moves = Moves + 1
    display()
    if CheckIfWinner(rows, secondPlayer):
        print('Congratulations ' + secondPlayer + ' you have won the game' )
        break
    if Moves == 9:
        print('The game ends with a tie, no more possible moves')
        break
    