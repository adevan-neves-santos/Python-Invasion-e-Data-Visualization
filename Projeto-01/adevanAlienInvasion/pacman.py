from ship import Ship
import pygame
import os
class Pacman(Ship):
    '''Pacman faz tudo que Ship faz, porém começa no centro da tela e pode atirar para esquerda ou direita
    ,assim como se mover para direita e esquerad também.'''
    def __init__(self,screen,ai_settings):
        super().__init__(screen,ai_settings,os.path.join('adevanAlienInvasion','imagens','pacman.bmp'))
        '''Colocar o retângulo no centro da tela
        Fiz esta mudança para poder continuar com o preenchimento da tela por aliens
        self.rect.centerx=self.screen_rect.centerx
        self.rect.centery=self.screen_rect.centery'''

        #flag de movimento para cima
        self.moving_up=False
        
        #flag de movimento para baixo
        self.moving_down=False

        #Atributo centro y para movimentar verticalmente a nave
        self.centery=float(self.rect.centery)
    
    def update(self):
        '''Atualiza a posição da espaçonave de acordo com o centro de movimento.'''
        if (self.moving_right and (self.rect.right<self.screen_rect.right)):
            self.center+=self.ai_settings.person_speed_factor
        if (self.moving_left and (self.rect.left>0)):
            self.center-=self.ai_settings.person_speed_factor
        else:
            '''Significa que o pac está se movendo ou para cima ou para baixo.'''
            if(self.moving_up and (self.rect.top>0)):
                self.centery-=self.ai_settings.person_speed_factor
            if(self.moving_down and (self.rect.bottom<self.screen_rect.bottom)):
                self.centery+=self.ai_settings.person_speed_factor
    
        self.rect.centerx=self.center
        self.rect.centery=self.centery
    def center_obj(self):
        '''Centraliza o pacman na tela.'''
        self.centerx=self.screen_rect.centerx
        self.centery=self.screen_rect.height-self.rect.height