#Tic Tac Toe
while True: 
  try:
    width=int(input("set map size: "))+1
    break
  except:
    print("number please")
height=width
board=[1]*width*height
for field in range(0,len(board)):
  board[field]=' '
def drawBoard(board):
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
drawBoard(board)

cross='\033[93m'+'X'+'\033[0m'
circle='\033[92m'+'O'+'\033[0m'
hit=cross
while True:
    #target=[int(x) for x in input("Target coordinates (y,x): ").split()]
    target=[]
    while True:
      try:
        for coordinate in input("Target coordinates (Y X): ").split():
          target.append(int(coordinate))
        field=target[0]*width+target[1]
        break
      except:
        print("two numbers please")

    if board[field]!=circle and board[field]!=cross:
      board[field]=hit
      drawBoard(board)
      
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
      if target[1]>=width-2:
        horizontal.remove('+')
      #start inspection around target
      for move in vertical:
        Y=eval(str(target[0])+move+'1')
        for adjust in horizontal:
          X=eval(str(target[1])+adjust+'1')
          neighbor=Y*width+X
          if board[neighbor]==board[field] and neighbor!=field:
            YY=eval(str(Y)+move+'1')
            XX=eval(str(X)+adjust+'1')
            nextNeighbor=YY*width+XX
            if board[nextNeighbor]==board[field]:
              print(hit+' WIN!')
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
              YY=eval(str(Y)+move+'1'+move+'1')
              XX=eval(str(X)+adjust+'1'+adjust+'1')
              nextNeighbor=YY*width+XX
              if board[nextNeighbor]==board[field]:
                print(hit+' WIN!')

      if board[field]==cross:
        hit=circle
      else:
        hit=cross
    
    else:
      print("This field is taken!")
      if board[field]==cross:
        hit=circle
      else:
        hit=cross



