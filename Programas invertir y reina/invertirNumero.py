import math

def ope(num):
    print(num)
    if(num/10<1):
        return num
    else:
        return (((num/10)-(num//10))*10 + ope(num//10)/10)
    




def sumar(numero):
    if(numero==0):
        return numero
    else:
        return (numero-numero%10**exponente(numero))/(10**exponente(numero))+sumar(numero%10**exponente(numero))

def exponente(numero):
    return int(math.log10(numero))

def pru(num):
    if(num==0):
        break 
    print(pru(num%10))
     
#print("El resultado es: ",sumar(int(input("Ingrese un numero \n"))))
pru(int(input()))
