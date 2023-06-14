import math


def abs(x):
    return abs(x)

def grau_rad(n):
    x = math.pi * (n / 180)
    return x

def posicao(a,b,c,d):
    if (a == c) and (b == d):
        return "coincidente"
    elif (a < c) and (b < d):
        return "direita acima"
    elif (a < c) and (b > d):
        return "direita baixo"
    elif (a > c) and (b < d):
        return "esquerda acima"
    elif (a > c) and (b > d):
        return "esquerda baixo"
    else: 
        return "coincidente"

print(posicao(4,-1,-1,2))
    
    