def b():
    duracao = int(input())
    a,b = map(int,input().split())
    c,d = map(int,input().split())

    inicio = max(a,c)
    fim = min(b,d)
    horafinal = fim - duracao

    if duracao > (fim - inicio) or fim <= inicio:
        print("Impossivel")
    elif duracao == (fim - inicio):
        print(inicio)
    else:
        print("%d %d" % (inicio, horafinal))

b()
