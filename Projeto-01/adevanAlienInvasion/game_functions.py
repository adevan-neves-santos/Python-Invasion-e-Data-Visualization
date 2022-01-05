import sys

import sys
import pygame
from bullet_lateral import BulletLateral
from pacman import Pacman
from bullet import Bullet

def check_events(ai_settings,screen,obj,bullets,eh_pacman):
    '''Responde a eventos de pressionamento de teclas e de mouse.'''
    # Laço de eventos capturados por teclado
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            sys.exit()
        elif(event.type==pygame.KEYDOWN):
            check_keydown_events(event,ai_settings,screen,obj,bullets,eh_pacman)
        elif(event.type==pygame.KEYUP):
            check_keyup_events(event,obj,eh_pacman)

def check_keydown_events(event,ai_settings,screen,obj,bullets,eh_pacman):
    '''Responde a pressionamentos de tecla.'''
    if(event.key==pygame.K_RIGHT):
        # Move a espaçonave para a direita
        obj.moving_right=True
    elif(event.key==pygame.K_LEFT):
        # Move a espaçonave para a esquerda
        obj.moving_left=True
    elif(event.key==pygame.K_UP and(eh_pacman)):
        #Ao verificar que o personagem é uma instância de pacman, posso tranquilamente
        #editar o atributo de moving_up
        obj.moving_up=True
    elif(event.key==pygame.K_DOWN and (eh_pacman)):
        obj.moving_down=True
    elif(event.key==pygame.K_SPACE):
        fire_bullet(ai_settings,screen,obj,bullets,eh_pacman)
    elif(event.key==pygame.K_3 and (eh_pacman)):
        fire_bullet2(ai_settings,screen,obj,bullets,eh_pacman)
    elif(event.key==pygame.K_q):
        sys.exit()

def fire_bullet(ai_settings,screen,obj,bullets,eh_pacman):
    '''Dispara um projétil se o limite ainda não foi alcançado.'''
    #Cria um novo projétil e o adiciona ao grupo de projéteis, limitado apenas
    #pelo número máximo de projéteis em tela
    if(len(bullets)<ai_settings.bullets_allowed):
        new_bullet=Bullet(ai_settings,screen,obj)
        bullets.add(new_bullet)

def fire_bullet2(ai_settings,screen,obj,bullets,eh_pacman):
    '''Dispara um projétil lateral para a direita se o limite ainda não foi alcançado.'''
    #Cria um novo projétil e o adiciona ao grupo de projéteis, limitado apenas
    #pelo número máximo de projéteis laterais, que é 2.
    if(len(bullets)<2):
        new_bullet=BulletLateral(ai_settings,screen,obj)
        bullets.add(new_bullet)

                
def check_keyup_events(event,obj,eh_pacman):
    '''Responde a soltamentos de tecla.'''
    if event.key==pygame.K_RIGHT:
        obj.moving_right=False
    elif(event.key==pygame.K_LEFT):
        obj.moving_left=False
    elif(event.key==pygame.K_UP and(eh_pacman)):
        #Ao verificar que o personagem é uma instância de pacman, posso tranquilamente
        #editar o atributo de moving_up
        obj.moving_up=False
    elif(event.key==pygame.K_DOWN and (eh_pacman)):
        obj.moving_down=False

def update_screen(ai_settings,screen,obj,bullets):
    '''Atualiza as imagens em tela e alterna para a nova tela.'''

    #Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)

    #Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    obj.blitme()

    #Deixa a tela mais recente visível
    pygame.display.flip()

def update_bullets(bullets,screen):
    '''Atualiza  a posição dos projéteis e remove projéteis antigos.'''
    bullets.update()
    #Apagua bullet se ele sumir da tela, economizando o processento desnecessário
    for bullet in bullets.copy():
        if((bullet.rect.bottom<=0) or (bullet.rect.right>=screen.right)):
            bullets.remove(bullet)

def get_cor(cor):
    '''Retorna um código RGB da cor desejada na tela de fundo jogo.'''
    if(cor.upper()=="AZUL"):
        return (135,206,235)
    elif(cor.upper()=="VERDE"):
        return (144,238,144)
    elif(cor.upper()=="CINZA"):
        return (230,230,230)
    else:
        return (255,228,100)