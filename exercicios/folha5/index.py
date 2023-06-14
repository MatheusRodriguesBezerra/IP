import math

def somadivprops(n):
    if n==1:
        soma = 1
    else:
        soma = 1 + n
        if n%2 == 0:
            soma = soma + 2 + (n//2)
            variacao = 1
        else:
            variacao = 2
        d = 3
    while d*d < n:
        if n%d == 0: 
            soma = soma + d + (n//d)
        d = d + variacao
    if d*d == n: 
        soma = soma + d 
    return soma

def perfeito(n):
    if n==1:
        return True
    else:
        if int(somadivprops(n)) > (n+1):
            return False
        else: 
            return True

def imprimeperfeitos(a,b):
    while a <= b:
        if perfeito(a) == True:
            print(a)
        a = a + 1

def media_arit(x):
    length = 0
    soma = 0
    for valores in x:
        length = length + 1
        soma = soma + valores

    if length == 0:
        resultado = 0
    else:
        resultado = soma / length
    return resultado

def desvio_padrao(x):
    media = media_arit(x)
    length = 0
    for valores in x:
        length = length + 1

    i = 0
    somatorio = 0
    while i <= length-1:
        s = (x[i] - media) ** 2
        somatorio = somatorio + s
        i = i + 1

    resultado = math.sqrt((1/(length-1)) * somatorio)
    return resultado
    
def media_geom(x):
    length = 0
    mult = 1
    for valor in x:
        length = length + 1
        mult = mult * valor

    resultado = math.pow(mult, 1/length)
    return resultado

#def  prod_interno(x,y):

def lerseqfiltra():
    x = int(input())
    lista = []
    while x != 0:
        if x > 0:
            lista.append(x)
        x = int(input())
    print(lista)

def posicao(x,v):
    resultado = -1
    length = 0
    for _ in v:
        length = length + 1
    
    i = 0
    while (i < length) and (resultado == -1):
        if v[i] == x:
            resultado = i
        i = i + 1

    return resultado

def posMin(v):
    if v == []:
        return -1
    else:
        vminimo = v[0]
        iminimo = 0
        i = 1
        while i < len(v):
            if v[i] < vminimo:
                vminimo = v[i]
                iminimo = i
            i = i + 1
        return iminimo

def capicua(x):
    lista1 = x
    n = len(x)
    lista2 = []
    i = 0
    while i < n:
        lista2.append(lista1[n-i-1])
        i = i + 1

    if lista1 == lista2:
        return True
    else:
        return False

#def equiMedia(x):

def rotacao(v):
    lista = []
    lista.append(v[-1])
    i = 0
    while i < len(v)-1:
        lista.append(v[i]) 
        i = i + 1
    return lista

        
        
            

