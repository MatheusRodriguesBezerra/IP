k = int(input())
n = int(input())
soma = 0


while k != 0:
    if n > 0 and n % k == 0:
        soma += n
     
    n = int(input())

print(soma)