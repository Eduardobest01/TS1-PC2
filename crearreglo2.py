import random
import numpy as np

fil=int(input("Ingrese el numero de filas : "))
col=int(input("Ingrese el numero de columnas : "))

a=[[random.randint (1,100) for i in range(fil)] for j in range(col)]
print("Salidas de datos aleatorios")
for f in a:
    print(f)
    
print("Cambio de lista a arreglo")
arreglo=np.array(a)
print(arreglo)

print("1ra iteración:")
invertir=arreglo[:,::-1]
print(invertir)

print("2da iteración:")
invertir1=invertir[:,::-1]
print(invertir1)

print("3ra iteración:")
invertir2=invertir1[:,::-1]
print(invertir2)

print("4ta iteración:")
invertir3=invertir2[:,::-1]
print(invertir3)






