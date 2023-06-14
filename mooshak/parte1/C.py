def c():
    n = int(input())
    azul = 0
    amarelo = 0
    verde = 0
    while n != -1:
        if n >= 1 and n <= 10:
            azul = azul + 1
        if n >= 11 and n <= 23:
            verde = verde + 1
        if n >= 24 and n <= 40:
            amarelo = amarelo + 1
        n = int(input())
    print("azul: %d\namarelo: %d\nverde: %d" % (azul, amarelo, verde))

c()