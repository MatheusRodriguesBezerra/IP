def c():
    total,n = map(int,input().split())
    totalinicial = total
    i = 0
    lista = []

    while i < n:
        vproduto = int(input())
        nproduto = str(input())
        if vproduto <= total:
            total = total - vproduto
            lista.append(nproduto)
        i = i + 1

    totalfinal = totalinicial - total
    
    for x in lista:
        print(x)

    print("%d %d" % (totalfinal, total))

c()
