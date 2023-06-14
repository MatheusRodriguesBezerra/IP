def d():
    n = int(input())
    soma = 0
    i = 0
    gavetas = []
    while i < n:
        gaveta = str(input())
        gavetas.append(gaveta)
        i = i + 1
    i = 1
    if gavetas[0] == 'o':
        soma = soma + 1
    while i < n:
        if gavetas[i] == 'o':
            soma = soma + 1
        elif gavetas[i] == '#' and gavetas[i-1] == 'o':
            soma = soma + 1
        i = i + 1
    resultado = n - soma
    print(resultado)


d()