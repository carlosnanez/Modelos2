def contarPares(lista):
    if lista==[]:
        return 0
    else:
        return len ([x for x in lista if x%2==0])
print(contarPares([2,4,6,2,5,3,5,4,1,6]))        
    
