from random import randint

class Dado:
    '''Esta classe representa o comportamento de um dado de n lados.'''
    def __init__(self,numero_lados=6):
        self.numero_lados=numero_lados
    def jogar(self):
        '''Ao jogar um dado, você recebe a face exposta aleatória.'''
        face=randint(1,self.numero_lados)
        return face