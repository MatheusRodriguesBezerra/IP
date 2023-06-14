n = int(input("Valor de n (positivo)? ")) # input com output de mensagem
x = int(input("Valor de x (nao nulo)? "))
c = 0
cm = 0
while c < n:
    c += 1
    y = int(input("Valor de y? "))
    if y%x == 0:
        cm += 1
print("%d em %d" %(cm,n))