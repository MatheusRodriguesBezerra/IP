qtde = int(input())
n = int(input())
m = int(input())
soma = 0
state = 0

if n > m:
    state = -1
    while soma < qtde-2:
        n = m
        m = int(input())

        if n <= m:
            state = 0
        soma += 1
elif n < m:
    state = 1
    while soma < qtde-2:
        n = m 
        m = int(input())

        if n >= m:
            state = 0
        soma += 1

if state == 0:
    print("Nada com nada")
elif state == 1:
    print("Estritamente crescente")
else:
    print("Estritamente decrescente")
