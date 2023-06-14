def datas_max(ano,regs):
    listaDeRegistos = []
    for registo in regs:
        anoDaCaminhada = registo.get_data() // 10000
        if anoDaCaminhada > ano:
            listaDeRegistos.append(registo.get_data())
    return listaDeRegistos