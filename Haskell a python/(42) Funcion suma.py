def suma(lista):
    if lista == []:
        return 0
    else:
        return lista[0]+suma(lista[1:])
print (suma([5,4,7,8]))
