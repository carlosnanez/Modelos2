#3
import functools
from functools import reduce

def retornar2():
    return [[1,2,3,4],[7,6,7,8],[5,6],[1],[0,9,8,7,6,5]]

def retornar():
    return [1,2,3,4,5,6]

def valormax(lista):
    
    if lista==[]:
        return 0
    if lista[0]>lista[1]:
        return valormax(lista[1:]) 
    
    

print(valormax(retornar()))
