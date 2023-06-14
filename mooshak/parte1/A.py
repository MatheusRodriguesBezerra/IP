def a():
    andar, elev1, elev2 = map(int,input().split())
    diffelev1 = abs(elev1-andar)
    diffelev2 = abs(elev2-andar)
    if (abs(elev1) >= 100) and (abs(elev2) >= 100):
        print("0")
    elif elev1 == elev2:
        print("1")
    elif (diffelev1 == diffelev2) and (elev1 > elev2):
        print("1")
    elif (diffelev1 == diffelev2) and (elev1 < elev2):
        print("2")
    elif diffelev1 > diffelev2:
        print("2")
    else:
        print("1")

a()



