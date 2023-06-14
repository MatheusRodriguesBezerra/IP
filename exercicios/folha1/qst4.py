a,b,c = map(int,input().split())

if (a + b > c) and (a + c > b) and (c + b > a):
    if (a == b == c):
        print("(%d, %d, %d) define triangulo equilatero" % (a, b, c))
    elif (a == b) or (b == c) or (a == c):
        print("(%d, %d, %d) define triangulo isoceles" % (a, b, c))
    else:
        print("(%d, %d, %d) define triangulo escaleno" % (a, b, c))
else:
    print("(%d, %d, %d) não define triangulo" % (a, b, c))
    