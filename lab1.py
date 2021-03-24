from numpy import random

card_number = int(input("Ingrese la cantidad de cartas: "))
print (card_number)

cards = card_number*2
div = cards // 6

#necesitamos crear un tablero de NxN
def board(rows,columns):
    board = []
    for i in range (rows + 1):
        line_1 = " "
        line_2 = " "
        row_board = []

        for j in range (columns):
            line_1 +=  " " + str (j)
            if i != 0:
                line_2 +=  "_ " 
        
            elif i == 0:
                row_board.append (line_1)

            else:
                row_board.append (str(i-1) + line_2 )  

        board.append(row_board) 
    return board

b = board (div, 6)

#necesitamos que se agregen los numeros al tablero
def num_board (div):
    cards_values = []
    nums = [] #matriz
    
    for i in range (2):
        row = []
        repeat = 0

        while repeat < 5:
            x = random.randint(1, card_number)

            if cards_values.count(x) < 2:
                cards_values.append(x)
                row.append(x)
                repeat += 1

            elif len(cards_values) == cards:
                row.append("_ ")

            else:
                continue

    return nums

num_board(div)

#debemos mostrar las cartas que elige cada jugador
def card_show (x, y, board, nums):
    board [y - 1][x - 1] = nums [x - 1][y - 1]
    for i in board:
        for j in i:
            print (j, " ", end = "")
        
        print()
    
    return board [y - 1][x - 1]




