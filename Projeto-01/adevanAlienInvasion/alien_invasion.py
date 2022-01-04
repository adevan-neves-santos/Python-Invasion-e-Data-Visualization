import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pacman import Pacman
from input_output import ler_dados
from pygame.sprite import Group
from bullet import Bullet

def run_game(dados):
    # Inicializa as configurações em segundo plano
    pygame.init()
    ai_settings=Settings(dados["corFundo"])

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion de Adevan Neves!! Bem vindo {}".format(dados["nomeJogador"]))
    #Flag para saber com qual tipo de personagem estamos trabalhando
    eh_pacman=False

    #Cria uma espaçonave
    if(dados["nomePersonagem"].lower()=='pacman'):
        person=Pacman(screen,ai_settings)
        eh_pacman=True
    else:
        person=Ship(screen,ai_settings)

    #Cria um grupo na qual serão armazenados os projéteis
    bullets=Group()

    # Inicializa o laço principal do jogo
    while True:
        gf.check_events(ai_settings,screen,person,bullets,eh_pacman)
        person.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,person,bullets)

dados=ler_dados()
run_game(dados)