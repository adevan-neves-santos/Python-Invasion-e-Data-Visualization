import pygame

class Spider_Man():
    '''Esta classe representa o personagem principal do jogo, um boneco de spider-man'''
    def __init__(self):
        self.image=pygame.image.load('adevanAlienInvasion/imagens/spider-man.bmp')
        self.rect=self.image.get_rect()
        