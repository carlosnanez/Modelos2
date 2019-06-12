#2

def retornar():
    return [23,22,246,568,42,56,864,4668,682,345,63]

print(list(filter(lambda x:x%2==0,retornar())))
