#12.4 – Teclas: Em um arquivo Pygame, crie uma tela vazia. No laço de eventos,
#exiba o atributo event.key sempre que o evento pygame.KEYDOWN for detectado.
#Execute o programa e pressione várias teclas para ver como o Pygame responde

import pygame
import sys

def run_game():
    pygame.init()
    screen=pygame.display.set_mode((700,800))
    pygame.display.set_caption("Bem vindo ao teste de teclas .")

    while True:
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                sys.exit()
            elif(event.type==pygame.KEYDOWN):
                print(event.key)
        screen.fill((144,238,144))
        pygame.display.flip()

run_game()      