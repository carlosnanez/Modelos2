def leerArchivo():
    return[x.split() for x in open("laberinto.txt").readlines()]


def recorrer(posx,posy,matriz):
    if(matriz[posx][posy]=='y'):
        return true
    matriz[posx][posy]=1 #Asignacion 
    print(str(posx) +" "+ str(posy) +" "+ str(len(matriz)) + " " +str(len(matriz[0])))
    if(posy<len(matriz) and posy>0) and (posx<len(matriz[0]) and posx>0):
        if(matriz[posx][posy+1]==0):
            if(recorrer(posx,posy+1,matriz)):
                return True
        elif(matriz[posx+1][posy]==0):
            if(recorrer(posx+1,posy,matriz)):
                return True
        elif(matriz[posx][posy-1]==0):
            if(recorrer(posx,posy-1,matriz)):
                return True
        elif(matriz[posx-1][posy]==0):
            if(recorrer(posx-1,posy,matriz)):
                return True
    return False

def coorX(valor):
        return leerArchivo().index(buscarValor(leerArchivo(),valor))

def coorY(valor):
        return buscarValor(leerArchivo(),valor).index(valor)

def buscarValor(matriz,valor):
        if(len(matriz)==0): return False
        if(buscarLista(matriz[0],valor)==True):
                return matriz[0]
        else: return buscarValor(matriz[1:],valor)

def buscarLista(lista,valor):
        if(len(lista)==0): return False
        if(lista[0]==valor):
                return True
        else: return buscarLista(lista[1:],valor)
        
#print(recorrer(coorX("x"),coorY("x"),leerArchivo()))
print(recorrer(2,2,leerArchivo()))
    
