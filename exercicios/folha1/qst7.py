a,b = map(int,input().split())
raio = int(input())
c,d = map(int,input().split())

distancia = ((c - a) * (c - a)) + ((d - b) * (d - b))

if (raio * raio) >= distancia:
    print("(%d, %d): no interior" % (c, d))
else:
    print("(%d, %d): no exterior" % (c, d))

