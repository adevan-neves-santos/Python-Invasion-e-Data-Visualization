import pygame

class Ship():
    def __init__(self,screen,path_image='adevanAlienInvasion/imagens/ship.bmp'):
        '''Inicializa a espaçonave e define sua posição atual.'''
        self.screen=screen

        #Carrrega a imagem da espaçonave e obtém o seu rect (retângulo)
        self.image=pygame.image.load(path_image)
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #Flag que indica movimento  para à direita
        self.moving_right=False

        #Flag que indica movimento  para à esquerda
        self.moving_left=False

        #Inicia cada espaçonave na parte inferior central da tela
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

    def blitme(self):
        '''Desenha a espaçonave em sua posição atual.'''
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        '''Atualiza a posição da espaçonave de acordo com a flag de movimento.'''
        if self.moving_right:
            self.rect.centerx+=1
        if self.moving_left:
            self.rect.centerx-=1
        