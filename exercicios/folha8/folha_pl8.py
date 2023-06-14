class Fraction:
    def __init__(self, num, denom):
        if denom == 0:
            raise ZeroDivisionError("denominador zero")
        if denom < 0:
            denom = -denom
            num = -num
        d = mdc(abs(num),denom)
        self.num = num//d
        self.denom = denom//d

    def __str__(self):             # define a operação str(.)
        # fraccao irredutivel com denominador 1 se o valor for inteiro
        if self.denom == 1:
            return str(self.num)
        return '%d/%d' % (self.num, self.denom)
    
    def __add__(self,other):       # define a operação +
        r = Fraction(self.num*other.denom + self.denom*other.num,
                 self.denom*other.denom)
        return r
    
    def __mul__(self, other):     # define a operação *
        r = Fraction(self.num*other.num, self.denom*other.denom)
        return r

    def __sub__(self,other):       # define a operação -
        sym_other = Fraction(-other.num,other.denom)
        return self + sym_other

    def __truediv__(self,other):   # define a operação / 
        if other.num == 0:
            raise ZeroDivisionError('Divisão por zero')
        return self*Fraction(other.denom,other.num)
        
    def __eq__(self,other):        # define a operação == 
        return self.num*other.denom == self.denom*other.num

    def __lt__(self,other):        # define a operação < 
        return self.num*other.denom < self.denom*other.num

    def __le__(self,other):        # define a operação <=
        return self.num*other.denom <= self.denom*other.num

def mdc(a,b):
    if b == 0:
        if a == 0:
            raise ValueError("mdc(%d,%d) indefinido" % (a,b))
        return a
    return mdc(b, a%b)

class Point:
    '''ponto no plano com coordenadas do tipo Fraction'''
    
    def __init__(self,x,y,nome=''):
        self.x = x
        self.y = y
        self.nome = nome

    def __str__(self):
        return "(%s,%s)" % (str(self.x),str(self.y))

    def __eq__(self,other):
        '''retorna True se são têm as mesmas coordenadas'''
        return self.x == other.x and self.y == other.y

    def __lt__(self,other):
        '''retorna True se self é estritamente menor na ordem lexicográfica'''
        return self.x < other.x or (self.y < other.y and self.x == other.x)
    
    def __le__(self,other):
        '''retorna True se self é menor ou igual na ordem lexicográfica'''
        return self == other or self < other

    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)   # no name

    def __sub__(self,other):
        return Point(self.x-other.x,self.y-other.y)   # no name
    
    def shift_up(self):
        '''efetua um deslocamento do ponto de uma posição na vertical'''
        self.y += Fraction(1,1)

    def scale(self,fator):
        '''multiplica as coordenadas pelo fator do tipo Fraction indicado'''
        self.x  *= fator
        self.y  *= fator

    def squaredistance(self,other):
        '''retorna o quadrado da distância entre os dois pontos'''
        return (other.x-self.x)*(other.x-self.x)+(other.y-self.y)*(other.y-self.y)
    
class Circle:
    ''' a circle with Point c as center and Fraction r as ray '''
    def __init__(self,c,r):
        self.center = c
        self.ray = r

    def inCircle(self,p):
        return self.center.squaredistance(p) <= self.ray*self.ray

#--- Polygon não pedido --------------------------
class Polygon:
    def __init__(self,listVerts):
        self.verts = copy.deepcopy(listVerts)
#--------------------------------------------------



# Exercício 2 - Folha 8
        
def str2Fraction(x):
    if '/' in x:
        num,den = x.split('/')
        return Fraction(int(num),int(den))
    return Fraction(int(x),1)

def calcula(expr):
    termos = expr.split('+')
    soma = Fraction(0,1)
    for x in termos:
        soma += str2Fraction(x)
    return soma


def posnumero(expr,i):
    if i >= len(expr) or not digito(expr[i]):
        raise ValueError("expr[%d] não dígito" % i)
    while i < len(expr) and digito(expr[i]):
        i += 1
    return i-1    # posição de último dígito do número

def digito(c):
    return ord(c) >= ord('0') and ord(c) <= ord('9')

def isolar(expr):
    # expr bem formada e sem denominadores com sinais
    lista = []
    i = 0
    while i < len(expr):
        # proximo racional em expr
        s = ''
        if expr[i] == '+':
            i += 1
        elif expr[i] == '-':
            s ='-'
            i += 1
        j = posnumero(expr,i) + 1
        if j < len(expr) and expr[j] == '/':
            j = posnumero(expr,j+1) + 1
        s = s + expr[i:j]
        lista.append(s)
        i = j
    return lista

def soma_algebrica(expr):
    termos = isolar(expr)
    soma = Fraction(0,1)
    for x in termos:
        soma = soma + str2Fraction(x)
    return soma
