n = int(input())
maior = n
menor = n

while n != 0:
    if n > maior:
        maior = n
    if n < menor:
        menor = n 
    n = int(input())

print("Maior = %d e Menor = %d" % (maior, menor))