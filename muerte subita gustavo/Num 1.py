#1
import functools
from functools import reduce
def retornar2():
    return [[1,2,3,4],[7,6,7,8],[5,6],[1],[0,9,8,7,6,5]]

print(list(map(lambda x:[x[0],x[-1]] ,retornar2())))


