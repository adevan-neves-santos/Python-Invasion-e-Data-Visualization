import pygame
from pygame.sprite import Sprite
from random import randint
import os

class Star(Sprite):
    '''Representa uma estrela no céu.'''
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        #Carrega a imagem da estrela e define seu atributo rect
        self.image=pygame.image.load(os.path.join('adevanAlienInvasion','imagens','star.bmp'))
        self.rect=self.image.get_rect()

        #O início de cada estrela será aleatório, limitado apenas
        #tamanho da tela em x e y
        self.rect.right=randint(self.rect.width,self.ai_settings.screen_width)
        self.rect.bottom=randint(self.rect.height,self.ai_settings.screen_height)

    def blitme(self):
        '''Desenha a estrela em sua posição física'''
        self.screen.blit(self.image,self.rect)

    def update(self):
        '''Atualiza o movimento da estrela cadente.'''
        self.rect.y+=1