def b():
    dna = str(input())
    l = []
    while dna != '#':
        l.append(dna)
        dna = str(input())

    nl = [l[0]]
    size = 0
    for n in l:
        size = size + 1

    i = 1

    while i < size:
        if l[i] == 'a' and l[i-1] == 'c':
            nl.append('t')
        if l[i] == 'a' and l[i-1] == 't':
            nl.append('c')
        if l[i] == 'c' and l[i-1] == 'a':
            nl.append('t')
        if l[i] == 'c' and l[i-1] == 't':
            nl.append('a')
        if l[i] == 't' and l[i-1] == 'a':
            nl.append('c')
        if l[i] == 't' and l[i-1] == 'c':
            nl.append('a')
        if l[i] == l[i-1]:
            nl.append(l[i])
        i = i + 1
    
    for j in nl:
        print(j)

b()



