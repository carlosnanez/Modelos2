def divisible(x,y):
    return  bool(x%y==0)

def divisibles(x):
    return [y for y in range(1,x+1) if divisible(x,y)]

def esPrimo(n):
    return bool(len(divisibles(n))<=2)

def primos(n):
    return [x for x in range(1,n+1) if esPrimo(x)]


print(primos(100))





