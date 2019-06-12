#5

import functools
def retornar():
    return [2,23,234,245,23,6824,32,200]

print(list(filter(lambda x:x<retornar()[0]**5,retornar())))


