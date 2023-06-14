def d():
    h1,m1 = map(int,input().split())
    h2,m2 = map(int,input().split())

    totalminutos1 = (h1 * 60) + m1
    totalminutos2 = (h2 * 60) + m2

    difftotal = totalminutos2 - totalminutos1
    diffhoras = difftotal // 60
    diffminutos = difftotal % 60

    if difftotal < 60 and difftotal == 1:
        print("Passaram apenas 1 minuto!\nDe facto!")
    elif difftotal < 60 and difftotal != 1:
        print("Passaram apenas %d minutos!\nDe facto!" % (difftotal))
    elif diffhoras == 1 and diffminutos != 1:
        print("Passaram apenas %d minutos!\nQueres dizer, 1 hora e %d minutos?!" % (difftotal, diffminutos))
    elif diffhoras != 1 and diffminutos == 1:
        print("Passaram apenas %d minutos!\nQueres dizer, %d horas e 1 minuto?!" % (difftotal, diffhoras))
    elif diffhoras == 1 and diffminutos == 1:
        print("Passaram apenas %d minutos!\nQueres dizer, 1 hora e 1 minuto?!" % (difftotal))    
    else:
        print("Passaram apenas %d minutos!\nQueres dizer, %d horas e %d minutos?!" % (difftotal, diffhoras, diffminutos))

d()