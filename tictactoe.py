#Tic Tac Toe
import random

board = ["0"," 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10","11","12","13","14","15","16"]


def drawBoard(board):
    #this function draw the board if that was passed

    print('    |    |    |')
    print(' ' + board[13] + ' | ' + board[14] + ' | ' + board[15] + ' | ' + board[16])
    print('    |    |    |')
    print('-------------------')
    print('    |    |    |')
    print(' ' + board[9] + ' | ' + board[10] + ' | ' + board[11] + ' | ' + board[12])
    print('    |    |    |')
    print('-------------------')
    print('    |    |    |')
    print(' ' + board[5] + ' | ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('    |    |    |')
    print('-------------------')
    print('    |    |    |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ' + board[4])
    print('    |    |    |')
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


