import numpy as np 
print("Ejemplo practico para mover columnas")
matriz=np.arange(1,17).reshape(4,4)     #EN ESTE CASO UTILIZAREMOS 16 ELEMENTOS EN UNA MATRIZ 4X4
print(matriz)
print("Cambiaremos la primera columna por la primera")
invertir=matriz[:,::-1]
print(invertir)



