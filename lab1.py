import random

tablero = []
cantidad_cartas = int(input("Ingrese la cantidad de cartas: "))
print (cantidad_cartas)

#orden del tablero depende de la cantidad de cartas
ordentablero = cantidad_cartas

#necesitamos crear un tablero de NxN
def crear_tablero():
    for lines in range (ordentablero):
        line = []

        for columns in range (ordentablero):
            line.append ("*")    

    tablero.append(line)

