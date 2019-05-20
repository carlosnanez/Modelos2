#definir una funcion de añadir un nodo en un arbol
#coja un lista y meta todos los elementos
class Nodo:
    def __init__(self, valor, izq=None, der=None):
        self.valor=valor
        self.izq=izq
        self.der=der

def buscar(arbol,valor):
    if (arbol==None):
        return False
    elif (arbol.valor==valor):
        return True
    elif (arbol.valor<valor):
        return buscar(arbol.der,valor)
    return buscar(arbol.izq,valor)

def getLista(arbol):
    if arbol==None:
        return[]
    return getLista(arbol.izq)+[arbol.valor]+getLista(arbol.der)

def crearHoja(valor):
    return Nodo(valor)
   
def sumar(arbol):
    if arbol==None:
        return 0
    return sumar(arbol.izq)+arbol.valor+sumar(arbol.der)

def insertar(arbol, valor):    
    if (arbol.valor>valor):
        if arbol.der==None:
            return Nodo(arbol.valor, arbol.izq, valor)
        return Nodo(arbol.valor, arbol.izq, insertar(arbol.der,valor))
    elif (arbol.valor<valor):
        if arbol.izq==None:
            return Nodo(arbol.valor, valor, arbol.der)
        return Nodo(arbol.valor, insertar(arbol.izq, valor), arbol.der)

nodito = Nodo(20,Nodo(10, Nodo(5), Nodo(18)),Nodo(40,None,Nodo(50)))
print(buscar(nodito,55))
#print(getLista(nodito))
print(sumar(nodito))
#print(getLista(crearHoja(10)))
nodito2=insertar(nodito,4)
print(buscar(nodito2,4))
