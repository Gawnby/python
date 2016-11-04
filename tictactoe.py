#Tic Tac Toe

#toolkit
import os
import sys

#launch
def launch():
  os.system('cls' if os.name == 'nt' else 'clear')
  print('\033[94m' + "\
                                              \n\
                                              \n\
  TTTTTT  II  CCCC    TTTTTT    AA    CCCC    \n\
    TT    II  C         TT     A__A   C       \n\
    TT    II  CCCC      TT    A    A  CCCC    \n\
                                              \n\
                                              \n\
              TTTTTT  OOOO  EEEE              \n\
                TT    O  O  EE                \n\
                TT    OOOO  EEEE              \n\
                                              \n\
                                              \n\
             Press Ctrl+C to quit"+'\033[0m\n\n')
  try:
    width=int(input("set board size: "))+1
    height=width
    players=['X','O']
    player=players[players.index(input("Choose a player (X/O): ").upper())]
    target(width,height,players,player)
  except ValueError:
    print("number please")

#mapping
def drawBoard(board,width,height):
  os.system('cls' if os.name == 'nt' else 'clear')
  print('    ',end='')
  for column in range(1,width):
    if(len(str(column))==1):
      print(column,end=' ')
    else:
      print(column,end='')
  print('\n',end='')
  for slice in range(1,height):
    if(len(str(slice))==1):
      print(str(slice)+'  |',end='')
    else:
      print(str(slice)+' |',end='')
    for field in range(slice*width,slice*width+width-1):
      print(str(board[field+1])+'|',end='')
    print('\n',end='')
  print('\n',end='')

#switch player
def switchplayer(board,field,players,player):
  if board[field]==players[0]:
    player=players[1]
  else:
    player=players[0]

#wincheck
def wincheck(target,width,height,board,field,players,player,finish):
  #inspect neighborhood for winner sequence
  vertical=['+','+1-','-']
  horizontal=['+','+1-','-']
  #exclude off-margin inspection
  if target[0]<=2:
    vertical.remove('-')
  if target[0]>=width-2:
    vertical.remove('+')
  if target[1]<=2:
    horizontal.remove('-')
  if target[1]>=height-2:
    horizontal.remove('+')
  #find neighbors around target
  for move in vertical:
    Y=eval(str(target[0])+move+'1')
    for adjust in horizontal:
      X=eval(str(target[1])+adjust+'1')
      neighbor=Y*width+X
      #compare them to the target field
      if board[neighbor]==board[field] and neighbor!=field:
        YY=eval(str(Y)+move+'1')
        XX=eval(str(X)+adjust+'1')
        nextNeighbor=YY*width+XX
        if board[nextNeighbor]==board[field]:
          print(player+' WIN!')
          eval(finish[int(input("1:continue\n2:replay\n3:quit\n"))-1])
        #if no success, try the opposite direction
        else:
          if move=='+':
            move='-'
          if move=='-':
            move='+'
          if adjust=='+':
            adjust='-'
          if adjust=='-':
            adjust='+'
          YYY=eval(str(Y)+move+'1'+move+'1')
          XXX=eval(str(X)+adjust+'1'+adjust+'1')
          oppositeNeighbor=YYY*width+XXX
          if board[oppositeNeighbor]==board[field]:
            print(player+' WINS!')
            eval(finish[int(input("1:continue\n2:replay\n3:quit\n"))-1])

#takefield
def takefield(target,width,height,board,field,players,player,finish):
  if board[field]!=players[1] and board[field]!=players[0]:
    board[field]=player
    drawBoard(board,width,height)
    wincheck(target,width,height,board,field,players,player,finish)
  else:
    print("This field is taken!")

#target
def target(width,height,players,player):
  board=[" "]*width*height
  drawBoard(board,width,height)
  finish=["","target(width,height,players,player)","sys.exit()"]
  while True:
    #def target(): 
    #  while True 
    #    if 
    #  return target
    #target=target()
    try:
      target=[int(coordinate) for coordinate in input("Target coordinates (vertical,horizontal): ").split(',') if coordinate != "kill"]
      if target==[]:
        for field in range(len(board)):
          if board[field]!=player:
            board[field]=" "
            drawBoard(board,width,height)
      else:
        field=target[0]*width+target[1]
        takefield(target,width,height,board,field,players,player,finish)
      if player==players[0]:
        player=players[1]
      else:
        player=players[0]
    except ValueError:
      print("csv please")

#start game
try:
  launch()
except KeyboardInterrupt:
  sys.exit("\nAu revoir!")