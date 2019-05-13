def lista_ordenada(lista):
    if lista==[]:
        return True
    elif len(lista)==1:
        return True
    else:
        return (lista[0]<=lista[1] and lista_ordenada(lista[1:]))
print(lista_ordenada(['a','b','c','d']))
