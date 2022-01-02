import sys

import sys
import pygame

def check_events(obj):
    '''Responde a eventos de pressionamento de teclas e de mouse.'''
    # Laço de eventos capturados por teclado
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            sys.exit()
        elif(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_RIGHT):
                # Move a espaçonave para a direita
                obj.moving_right=True
            elif(event.key==pygame.K_LEFT):
                # Move a espaçonave para a esquerda
                obj.moving_left=True
        elif(event.type==pygame.KEYUP):
            if event.key==pygame.K_RIGHT:
                obj.moving_right=False
            if(event.key==pygame.K_LEFT):
                obj.moving_left=False
                

def update_screen(ai_settings,screen,ship):
    '''Atualiza as imagens em tela e alterna para a nova tela.'''

    #Redesenha a tela a cada passgem pelo laço
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Deixa a tela mais recente visível
    pygame.display.flip()

def get_cor(cor):
    if(cor.upper()=="AZUL"):
        return (135,206,235)
    elif(cor.upper()=="VERDE"):
        return (144,238,144)
    elif(cor.upper()=="CINZA"):
        return (230,230,230)
    else:
        return (255,228,225)