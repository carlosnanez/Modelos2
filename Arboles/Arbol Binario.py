#TAREA:
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

def sumar(arbol):
    if arbol==None:
        return 0
    return sumar(arbol.izq)+arbol.valor+sumar(arbol.der)

def insertar(arbol, valor):    #Inserta un valor en un arbol
    if (arbol.valor<valor):
        if arbol.der==None:
            return Nodo(arbol.valor, arbol.izq, Nodo(valor))
        return Nodo(arbol.valor, arbol.izq, insertar(arbol.der,valor))
    elif (arbol.valor>valor):
        if arbol.izq==None:
            return Nodo(arbol.valor, Nodo(valor), arbol.der)
        return Nodo(arbol.valor, insertar(arbol.izq, valor), arbol.der)

def crearArbol(lista, arbol): #Crea un arbol basado en una lista
    if len(lista)==1:
        return insertar(arbol, lista[0])
    arbol = insertar(arbol, lista[0])
    return crearArbol2(lista[1:], arbol)

nodito = Nodo(20,Nodo(10, Nodo(5), Nodo(18)),Nodo(40,None,Nodo(50)))
print(buscar(nodito,55))
print(sumar(nodito))
print(getLista(nodito))
nodito = insertar(nodito,4)
nodito = insertar(nodito,21)
print(getLista(nodito))
print(buscar(nodito,4))
nodito2 = Nodo(0)
nodito2 = crearArbol([5,4,3,2,1],nodito2)
print(getLista(nodito2))
