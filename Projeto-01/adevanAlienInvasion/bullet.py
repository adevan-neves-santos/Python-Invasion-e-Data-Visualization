import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Uma classe que administra projéteis disparados pelo personagem.'''

    def __init__(self, ai_settings,screen,obj):
        super().__init__()
        self.screen=screen
        #Cria um retângulo para o projétil em (0,0) e, em seguida, define
        # a posição correta
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx=obj.rect.centerx
        self.rect.top=obj.rect.top

        #Armazena a posição do projétil como um valor decimal
        self.y=float(self.rect.y)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    def update(self):
        '''Move o projeto para cima da tela.'''

        #Atualiza a posição decimal do projétil
        self.y-=self.speed_factor
        #Atualiza a posição do rect
        self.rect.y=self.y
    
    def draw_bullet(self):
        '''Desenha o projétil na tela.'''
        pygame.draw.rect(self.screen,self.color,self.rect)