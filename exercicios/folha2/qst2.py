qtd = int(input())
n = int(input())

total = 1
soma = 0

while total < qtd:
    if ((n % 2 == 0) or (n % 3 == 0)) and (n % 6 != 0):
        soma += 1
    
    total += 1

    n = int(input())

print("Numero de multiplos ou de 2 ou de 3 = %d" % (soma))