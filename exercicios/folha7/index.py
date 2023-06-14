def ler_dados(nomefile):
    try:
        file = open(nomefile,"r")
        disc = ler_disciplinas(file)
        alunos = ler_dados_alunos(file)
        file.close()
        return (disc,alunos)
    except IOError:
        print("Ficheiro "+ nomefile + " não existe")
        return ([],{})

def ler_disciplinas(file):
    ndisc = int(file.readline())
    disciplinas = [("None",0)] # disciplina[i] fica associada ao c´odigo i
    for _ in range(ndisc):
        nome = file.readline()
        ano = int(file.readline())
        disciplinas.append((nome[:-1],ano))
    return disciplinas

def ler_dados_alunos(file):
    alunos = {}
    nalunos = int(file.readline())
    for _ in range(nalunos):
        nome = file.readline()
        linha = list(map(int,file.readline().split()))
        alunos[linha[0]] = (nome[:-1],linha[1],linha[2:])
    return alunos

def cursoAluno(codigo):


def anoAluno(codigo):
    resultado = codigo // 1000000
    return resultado


ler_dados("folha7/bdalunos.txt")