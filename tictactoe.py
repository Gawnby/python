#Tic Tac Toe
import random
board=[1]*16
for field in range(0,len(board)):
    if(len(str(field))==1):
      board[field]=' '+str(field)
    else:
      board[field]=field
def drawBoard(board):
    #this function draw the board if that was passed
  width=4
  height=4
  print('-------------------------')
  for slice in range(0,height):
      print('|',end='')
      for field in range(slice*width,slice*width+width):  
        print('     |',end='')
      print('\n',end='')
      print('| ',end='')
      for field in range(slice*width,slice*width+width):
        print(' '+str(board[field])+' | ',end='')
      print('\n',end='')
      print('|',end='')
      for field in range(slice*width,slice*width+width):
        print('     |',end='')
      print('\n',end='')
      print('-------------------------')


drawBoard(board)

hit=" x"
while True:
    field = eval(input("Select a field: "))
    if board[field] !=' x' and board[field] !=' x':
       board[field] =hit
       drawBoard(board)
    else:
        print ("This field is taken!")  
    if board[field] ==' x' :
        hit =' O'
    else: 
        hit =' x'

       
