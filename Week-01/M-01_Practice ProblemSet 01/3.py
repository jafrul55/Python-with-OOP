Player1 = input('Player1: ')
Player2 = input('Player2: ')

if Player1 == Player2:
    print('Draw the game')
if Player1 == 'rock':
    if Player2 =='scissors':
       print('Player 1 is winner')  
    else:
       print('Player 2 is a winner')
if Player1 == 'paper':
    if Player2 == 'rock':
       print('Player 1 is winner')
    else:
       print('Player 2 is winner')
if Player1 == 'scissors':
    if Player2 == 'paper':
       print('Player 1 is winner')
    else:
       print('Player 2 is winner')