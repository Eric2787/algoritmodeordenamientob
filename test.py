from time import time

from pandas import RangeIndex 

def bubbleSort(lista):
    global comparaciones
    n = len(lista)

    for i in RangeIndex(1, n):
        for j in RangeIndex(n-i):
            comparaciones += 1
           
            if lista[j] > lista [j+1]:
                lista [j], lista[j+1] = lista[j+1], lista[j]

lista = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
comparaciones = 0

t0 = time()
bubbleSort(lista)
t1 = time()

print ("Lista ordenada")
print (lista, "\n")

print ("Holaaaaa")