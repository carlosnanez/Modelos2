#1
import functools
from functools import reduce

def retornar():
    return [1,2,3,4,5,6,7,8]
#[[1,1], [5,2], [8,3], [10,4], [23,5], [31,6], [28,7], [36,8], [47,9], [55,10], [77,11], [93,12]]

print(reduce(lambda x,y: (x,y) ,retornar()))
