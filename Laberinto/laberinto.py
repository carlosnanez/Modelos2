#metodo que carga el archivo
def leerArchivo():
    return[x.split() for x in open("lab.txt").readlines()]

#Clase que crea el arbol y metodos para interactuar con él
class Nodo:
    def __init__(self,valor,x,y,hijos=[]):
        self.valor=valor
        self.hijos=hijos
        self.x=x
        self.y=y
        
    def agregar(self,x,y,valor):
        self.hijos.append(Nodo(valor,x,y))
        
def buscar(arbol,valor):
    if arbol.valor==valor:
        return True
    return buscarHijos(arbol.hijos, valor)

def buscarHijos(lista,valor):
    if lista==[]:
        return False
    return buscar(lista[0],valor) or buscarHijos(lista[1:],valor)


#metodos para ubicar la posicion de un valor en la matriz(lista de listas)

def buscarValor(matriz,valor):
    if(len(matriz)==0):
        return False
    if(buscarLista(matriz[0],valor)==True):
        return matriz[0]
    return buscarValor(matriz[1:],valor)

def buscarLista(lista,valor):
    if(len(lista)==0):
        return False
    if(lista[0]==valor):
        return True
    return buscarLista(lista[1:],valor)

def coorX(valor):
    return leerArchivo().index(buscarValor(leerArchivo(),valor))
def coorY(valor):
    return buscarValor(leerArchivo(),valor).index(valor)

def verificar(valor):
    if valor=='1':
        return False
    return True


def jugar(arbol):
        if(arbol.valor=='y'):
            puntos.append((arbol.x,arbol.y))
            return True
        
        
        if verificar(leerArchivo()[arbol.x+1][arbol.y]): #Verificar a la derecha
            arbol.agregar(arbol.x+1,arbol.y,leerArchivo()[arbol.x+1][arbol.y])
            jugar(arbol.hijos[-1])

        if verificar(leerArchivo()[arbol.x-1][arbol.y]): #Verificar a la izquierda
                arbol.agregar(arbol.x-1,arbol.y,leerArchivo()[arbol.x-1][arbol.y])
                jugar(arbol.hijos[-1])
            
        if verificar(leerArchivo()[arbol.x][arbol.y+1]): #Verificar abajo
                arbol.agregar(arbol.x,arbol.y+1,leerArchivo()[arbol.x][arbol.y+1])
                jugar(arbol.hijos[-1])
            
        if verificar(leerArchivo()[arbol.x][arbol.y-1]): #Verificar arriba
                arbol.agregar(arbol.x,arbol.y-1,leerArchivo()[arbol.x][arbol.y-1])
                jugar(arbol.hijos[-1])
            
        return False

    

print(jugar(Nodo('x',coorX('x'),coorY('x'))))



