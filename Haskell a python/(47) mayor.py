def mayor(lista):
    if lista==[]:
        return 0
    elif lista[0] > mayor(lista[1:]):
        return lista[0]
    else:
        return mayor(lista[1:])
print(mayor ([78,24,56,93,21,237,46,74,125]))
