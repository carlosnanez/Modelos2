class Nodo:
    def __init__(self, valor, hijos=[]):
        self.valor = valor
        self.hijos = hijos

def buscar(arbol,valor):
    if arbol.valor==valor:
        return True
    return buscarHijos(arbol.hijos, valor)

def buscarHijos(lista, valor):
    if lista==[]:
        return False
    return buscar(lista[0], valor) or buscarHijos(lista[1:], valor)
    
nodito = Nodo(1, [Nodo(2),Nodo(3),Nodo(4, [Nodo(5)])])
print(buscar(nodito,0))
print(buscar(nodito,5))

