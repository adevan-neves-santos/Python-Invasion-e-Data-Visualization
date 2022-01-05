import pygame 

from bullet import Bullet

class BulletLateral(Bullet):
    '''Uma classe que administra disparos laterais dadoa pelo pacman.'''
    def __init__(self, ai_settings, screen, obj):
        super().__init__(ai_settings, screen, obj)
        self.rect.y=obj.rect.y
        self.rect.x=obj.rect.x
        self.rect.right=self.obj.rect.right
        #Armazena a posição do projétil como um valor decimal
        self.y=float(self.rect.y)
        self.x=float(self.rect.x)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    def update(self):
        '''Move o projeto para à direita da tela.'''

        #Atualiza a posição decimal do projétil
        self.x+=self.speed_factor
        #Atualiza a posição do rect
        self.rect.x=self.x