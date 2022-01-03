from random import choice

class Passeio_Aleatorio():
    '''Classe que representa um passeio aleatório com pontos.'''
    def __init__(self,numero_pontos=5000):
        self.numero_pontos=numero_pontos
        self.x_valores=[0]
        self.y_valores=[0]

    def calcular_passeio(self):

        while(len(self.x_valores)<self.numero_pontos):

            passo_x=choice([0,1,2,3,4])
            sentido_x=choice([1,-1])
            mov_x=passo_x*sentido_x

            passo_y=choice([0,1,2,3,4])
            sentido_y=choice([1,-1])
            mov_y=passo_y*sentido_y

            if(mov_x==0 and mov_y==0):
                continue
            proximo_x=self.x_valores[-1]+mov_x
            proximo_y=self.y_valores[-1]+mov_y

            self.x_valores.append(proximo_x)
            self.y_valores.append(proximo_y)