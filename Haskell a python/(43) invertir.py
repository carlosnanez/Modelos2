def invertir(lista):
    if lista==[]:
        return []
    else:
        return invertir(lista[1:]) + [lista[0]]
    
print(invertir([5,4,7,8]))


