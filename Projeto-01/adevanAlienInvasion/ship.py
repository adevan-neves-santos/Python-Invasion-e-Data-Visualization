import pygame
from pygame.sprite import Sprite
import os

class Ship(Sprite):
    def __init__(self,screen,ai_settings,path_image=os.path.join('adevanAlienInvasion','imagens','ship.bmp')):
        super().__init__()
        '''Inicializa a espaçonave e define sua posição atual.'''
        self.screen=screen

        self.ai_settings=ai_settings

        #Carrrega a imagem da espaçonave e obtém o seu rect (retângulo)
        self.image=pygame.image.load(path_image)
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()

        #Flag que indica movimento  para à direita
        self.moving_right=False

        #Flag que indica movimento  para à esquerda
        self.moving_left=False

        #Inicia cada espaçonave na parte inferior central da tela
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        #Armazena um valor decimal para o centro da nave
        self.center=float(self.rect.centerx)

    def blitme(self):
        '''Desenha a espaçonave em sua posição atual.'''
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        '''Atualiza a posição da espaçonave de acordo com o centro de movimento.'''
        if (self.moving_right and (self.rect.right<self.screen_rect.right)):
            self.center+=self.ai_settings.person_speed_factor
        if (self.moving_left and (self.rect.left>0)):
            self.center-=self.ai_settings.person_speed_factor
    
        self.rect.centerx=self.center
        
    def center_obj(self):
        '''Centraliza a espaçonave na tela.'''
        self.center=self.screen_rect.centerx