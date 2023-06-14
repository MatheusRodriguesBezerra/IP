import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(%d,%d)" % (self.x,self.y)
    
    def __eq__(self,other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False    
    
    def __lt__(self,other):
        if self.x < other.x and self.y < other.y:
            return True
        else:
            return False

    def __le__(self,other):
        if self.x <= other.x and self.y <= other.y:
            return True
        else:
            return False

    def shift_up(self):
        self.y = self.y + 1
        return self
    
    def scale(self,fator):
        self.x = self.x * fator
        self.y = self.y * fator
        return self
    
    def squareDistance(self,other):
        resultado = ((self.x-other.x)**2) + ((self.y-other.y)**2)
        return resultado
    

class Circle:
    def __init__(self,Point,r):
        self.r = r
        self.x = Point[0]
        self.y = Point[1]
    
    def __str__(self):
        return "(%d,%d), r: %d" % (self.x,self.y,self.r)

    def inCirle(self,p):
        c = Point(self.x,self.y)
        ponto = Point(p[0],p[1])
        if math.sqrt(c.squareDistance(ponto)) <= self.r:
            return True
        else: 
            return False


def filtra(circ,pontos):
    
        
