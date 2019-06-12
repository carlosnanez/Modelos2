#Dada una lista de tuplas caracterizada por (int x, int y) sumar los x que cumplan con el criterio de ser el número triangular de y
import functools
from functools import reduce
lista= [[1,1], [5,2], [8,3], [10,4], [23,5], [31,6], [28,7], [36,8], [47,9], [55,10], [77,11], [93,12]]
print(reduce(lambda x,y: x+y, list(map(lambda x:x[1], list(filter(lambda x: x[0] == ((x[1]*(x[1]+1))/2),lista)) )) ))
