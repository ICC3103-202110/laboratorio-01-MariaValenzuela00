import random

cantidad_cartas = int(input("Ingrese la cantidad de cartas: "))
print (cantidad_cartas)

cartas = cantidad_cartas*2

#necesitamos crear un tablero de NxN
def crear_tablero(rows,columns):
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
            print( str(i-1) + line_2 )   
    return crear_tablero

x = crear_tablero(cartas,cartas)

#necesitamos que se agregen los numeros al tablero
def num_tablero (num):
    nums = []
    a = 0
    for i in range (cartas):
        nums.append ([])

        for j in range (cartas):
            nums[i].append(num[a])
            a += 1

    for i in range (len(nums)):
        print(nums[i])
    
    return nums

#debemos mostrar las cartas que elige cada jugador
#def mostrar_cartas (a,b):


