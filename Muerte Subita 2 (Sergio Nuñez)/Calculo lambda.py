import functools
lista = [[1,1], [5,2], [8,3], [10,4], [23,5], [31,6], [28,7], [36,8], [47,9], [55,10], [77,11], [93,12]]
resultado = filter(lambda x: x[0] == ((x[1]*(x[1]+1))/2), lista)
print(list(resultado))
