import pygame
import game_funtions_spider as gfs

'''

13.5 – Agarrando uma bola: Crie um jogo que posicione um personagem na
parte inferior da tela; você poderá mover esse personagem para a esquerda e para
a direita. Faça uma bola aparecer em uma posição aleatória na parte superior da
tela e que caia a uma velocidade constante. Se seu personagem “agarrar” a bola
colidindo com ela, faça a bola desaparecer. Crie uma nova bola sempre que seu
personagem agarrá-la ou sempre que ela desaparecer na parte inferior da tela.

13.6 – Fim de jogo: Usando o código do Exercício 13.5 (página 370), mantenha
o controle do número de vezes que o jogador erra a bola. Quando ele errar a bola
três vezes, encerre o jogo

'''

def run_game_spider():
    '''Função principal que inicializa o jogo.'''
    while True:
        gfs.update_screen()