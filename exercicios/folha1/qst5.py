a,b,c = map(int,input().split())


if ((b * b) - 4 * a * c) > 0 and a != 0:
    print("raizes distintas")
elif ((b * b) - 4 * a * c) == 0 and a != 0:
    print("raizes duplas")
else:
    print("nao existe raizes")