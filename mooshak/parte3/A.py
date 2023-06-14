def a():
    msg = str(input())
    contador = 0

    for x in msg:
        if x == 'p' or x == 'P':
            contador += 1

    print(contador)

a()