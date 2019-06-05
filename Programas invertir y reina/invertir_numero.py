import math

def invertirNumero(numero):
    if(numero==0):
        return 0
    else:
        #return obtenerUnidades(numero)+(invertirNumero(numero%10**exponente(numero)))
        return convertirUnidadesA(obtenerUnidades(numero),10**exponente(numero))

def obtenerUnidades(numero):
    return (numero%10**(exponente(numero)+1)-numero%10**exponente(numero))/10**exponente(numero)

def convertirUnidadesA(numero,potencia):
    return numero*(10**potencia)

def exponente(numero):
    return int(math.log10(numero))
def nuevoExponete(numero):
    if(numero==0):
        return 0
    else:
        return int(math.log10(numero))-1

print(invertirNumero(int(input("digite un numero a invertir: \n"))))
#print(obtenerUnidades(int(input("digite un numero a invertir: \n"))))

