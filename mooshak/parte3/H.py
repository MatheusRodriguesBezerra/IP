def h():
    n = int(input())
    a, b = map(int,input().split())
    inicio = a
    fim = b
    i = 1
    while i < n:
        a, b = map(int,input().split())
        if a > inicio:
            inicio = a
        if b < fim:
            fim = b
        i = i + 1
    if inicio > fim:
        print("impossivel")
    elif inicio == fim:
        print(inicio)
    else:
        media = (inicio + fim) / 2
        if (media // 1) == media:
            print(media)
        else:
            resultado = media // 1
            print("%d e meia" % (resultado))

h()