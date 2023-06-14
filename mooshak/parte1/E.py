def e():
    t, n = map(int,input().split())
    maxk = 0
    i = 0
    minmoderada = t-2
    maxmoderada = t+2
    l = []
    while i < n:
        temp = int(input())
        if temp >= minmoderada and temp <= maxmoderada:
            maxk = maxk + 1
        else:
            l.append(maxk)
            maxk = 0
        if i + 1 == n:
            l.append(maxk) 
        i = i + 1
    resultado = max(l)
    if resultado == 1:
        print("Temperaturas moderadas apenas em dias isolados")
    elif resultado == 0:
        print("Sem registo de temperaturas moderadas")
    else:
        print("Durante %d dias consecutivos, temperaturas moderadas" % (resultado))

e()