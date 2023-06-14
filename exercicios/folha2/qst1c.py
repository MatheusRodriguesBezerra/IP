nota = int(input())
total = 0
soma = 0

while nota != -1:
    if nota >= 10:
        soma += nota
        total += 1
    
    nota = int(input())

media = soma / total

print("%.2f" % (media))