nota = int(input())
total = 0
aprov = 0

while nota != -1:
    if nota >= 10:
        aprov += 1
    
    total += 1

    nota = int(input())

print("%d/%d" % (aprov,total))

