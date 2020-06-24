import random
fil=int(input("Ingrese el numero de filas : "))
col=int(input("Ingrese el numero de columnas : "))
#COLOCO DEL 1 AL 100 PARA QUE NO ME IMPRIMA ALEATORIOS CON PUNTOS
a=[[random.randint (1,100) for i in range(fil)] for j in range(col)] 
print("Salidas de datos aleatorios")
for f in a:
    print(f)





    




