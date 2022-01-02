from ship import Ship
import pygame
class Pacman(Ship):
    '''Pacman faz tudo que Ship faz, porém começa no centro da tela e pode atirar para esquerda ou direita
    ,assim como se mover para direita e esquerad também.'''
    def __init__(self,screen):
        super().__init__(screen,'adevanAlienInvasion/imagens/pacman.bmp')
        #Colocar o retângulo no centro da tela
        self.rect.centerx=self.screen_rect.centerx
        self.rect.centery=self.screen_rect.centery
        