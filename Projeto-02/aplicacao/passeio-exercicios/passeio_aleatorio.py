from random import choice

class Passeio_Aleatorio():
    '''Classe que representa um passeio aleatório com pontos.'''
    def __init__(self,numero_pontos=5000):
        self.numero_pontos=numero_pontos
        self.x_valores=[0]
        self.y_valores=[0]

    def getPasso(self):
        return choice([-2,-1,0,1,2,3,4])
    def getSentido(self):
        return choice([-1,1])

    def getCaminho(self):
        a=self.getPasso()
        b=self.getSentido()
        return a*b

    def calcular_passeio(self):

        while(len(self.x_valores)<self.numero_pontos):

            mov_x=self.getCaminho()
            mov_y=self.getCaminho()

            if(mov_x==0 and mov_y==0):
                continue
            proximo_x=self.x_valores[-1]+mov_x
            proximo_y=self.y_valores[-1]+mov_y

            self.x_valores.append(proximo_x)
            self.y_valores.append(proximo_y)