import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pacman import Pacman
from input_output import ler_dados

def run_game(dados):
    # Inicializa as configurações em segundo plano
    pygame.init()
    ai_settings=Settings(dados["corFundo"])

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion de Adevan Neves!! Bem vindo {}".format(dados["nomeJogador"]))

    #Cria uma espaçonave
    if(dados["nomePersonagem"].lower()=='pacman'):
        person=Pacman(screen,ai_settings)
    else:
        person=Ship(screen,ai_settings)

    # Inicializa o laço principal do jogo
    while True:
        gf.check_events(person)
        person.update()
        gf.update_screen(ai_settings,screen,person)

dados=ler_dados()
run_game(dados)