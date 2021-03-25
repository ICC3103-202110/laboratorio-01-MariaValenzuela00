import random

card_number = int(input("Ingrese la cantidad de cartas: "))

cards = card_number*2
div = cards // 4

#siempre 2 jugadores
player_1 = 0
player_2 = 0

#necesitamos crear un tablero de NxN
def board(rows,columns):
    for i in range (rows + 1):
        line_1 = " "
        line_2 = " "

        for j in range (columns):
            line_1 +=  " " + str (j)
            if i != 0:
                line_2 +=  "_ " 
    
        if i == 0:
            print (line_1)

        else:
            print (str(i-1) + line_2 )  

    return board

board (div,4)

#necesitamos que se agregen los numeros al tablero
def num_board (div):
    cards_values = []
    nums = [] #matriz
    
    for i in range (div):
        row = []
        repeat = 0

        while repeat < 4:
            x = random.randint(1, card_number)

            if cards_values.count(x) < 2:
                cards_values.append(x)
                row.append(x)
                repeat += 1

            elif len(cards_values) == cards:
                row.append("_")

            else:
                continue
        
    return nums

num_board(div)





