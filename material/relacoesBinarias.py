def somar(A,B,mlinhas,ncolunas):
    ''' somar matrizes '''
    for i in range(mlinhas):
        for j in range(ncolunas):
            A[i][j]  +=  B[i][j]

def produto(A,B,n):
    ''' retorna o produto de A por B sendo A e B matrizes quadradas'''
    C = []
    for i in range(n):
        Linha = []
        for j in range(n):
            soma = 0
            for k in range(n):
                soma += A[i][k]*B[k][j]
            Linha.append(soma)
        C.append(Linha)

    return C


def troca(A,k,p,n):
    ''' trocar a linha k com a linha p'''
    aux = A[k]     # copia o identificador da lista que A[k] aponta
    A[k] = A[p]    # copia para A[k] o identificador da lista dada por A[p]
    A[p] = aux     # copia para A[p] o identificador da lista que antes A[k] apontava
    

def reflexiva(M):
    n = len(M)   # numero de elementos do conjunto A   M é n x n
    for i in range(n):
        if M[i][i] == 0:
            return False
    return True

def simetrica(M):
    n = len(M)

    for i in range(1,n):
        for j in range(i) :
            if M[i][j] !=  M[j][i]:
                return False
    return True
      
    # M[i][j]   abaixo da diagonal .... corresponde a  M[j][i]  acima da diagonal

    # (0,0) 
    # (1,0) (1,1)
    # (2,0) (2,1) (2,2)
    # (i,0) (i,1) (i,2).... (i,i-1)  (i,i)

def antissimetrica(M):
    n = len(M)
    for i in range(1,n):
        for j in range(i) :
            if M[i][j] ==  M[j][i] and M[i][j] == 1:
                return False
    return True

# (i,j) in R  e  (j,i)  in R    ==>   i = j
# i != j   =>    (i,j) notin R  ou  (j,i) notin R


def transitiva(M):
    n = len(M)
    for i in range(n):
        for k in range(n):
            for j in range(n):
                if M[i][k] == 1 and M[k][j] == 1 and M[i][j] == 0:
                    return False
    return True


def equivalencia(M):
    return reflexiva(M) and simetrica(M) and transitiva(M)

def ordemparcial(M):
    return reflexiva(M) and antissimetrica(M) and transitiva(M)

def classesequivalencia(M):
    n = len(M)
    tratados = n*[False]
    for i in range(n):
        if tratados[i] == False:
            print("\nclasse de %d" % i)
            for j in range(i,n):
                if M[i][j] == 1:
                    print(j)
                    tratados[j] = True

def fechoReflexivo(M):
    n = len(M)
    for i in range(n):
        M[i][i] = 1

def fechoSimetrico(M):
    n = len(M)
    for i in range(n):
        for j in range(i):
            if  M[i][j]  !=   M[j][i]:
                M[i][j] = 1
                M[j][i] = 1



# RS  = { (x,z)      |    (x,y) in R e  (y,z) in S  para algum y}
# S após R
#  R:   m  x p     S : p x n
#  p  =   len( R[0])     numero de colunas da R
#  len(S) = numero de linhas da S   = p ?
#  composta tem dimensão   m x  n
#  n = len(S[0])
#  m = len(R)


def composta(R,S):
    m = len(R)
    n = len(S[0])
    p = len(R[0])
    composta =  [ [0  for j in range(n)]   for _ in range(m)]
    for i in range(m):
        for j in range(n):
            k = 0
            while k < n and composta[i][j] == 0:
                composta[i][j] += R[i][k]*S[k][j]
                k += 1

            # soma=0
            # for k in range(p):
            #     soma += R[i][k]*S[k][j]
            # if soma != 0:
            #     composta[i][j] = 1
    return composta
                 
def exemploMatriz():
    #M = [[1,1,1,0,0,0,0],[1,1,1,0,0,0,0],[1,1,1,0,0,0,0],[0,0,0,1,1,0,0],[0,0,0,1,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]]
    M = [[1,1,1,0,0,0,1],[1,1,1,0,0,0,1],[1,1,1,0,0,0,1],[0,0,0,1,1,0,0],[0,0,0,1,1,0,0],[0,0,0,0,0,1,0],[1,1,1,0,0,0,1]]
    return M

      
  
