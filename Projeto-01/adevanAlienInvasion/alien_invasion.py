import pygame
from pygame import sprite
import game_functions as gf
from settings import Settings
from ship import Ship
from pacman import Pacman
from input_output import ler_dados
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game(dados):
    # Inicializa as configurações em segundo plano
    pygame.init()
    ai_settings=Settings(dados["corFundo"])
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion de Adevan Neves!! Bem vindo {}".format(dados["nomeJogador"]))
    #Flag para saber com qual tipo de personagem estamos trabalhando
    eh_pacman=False

    #Cria uma instância para armazenar dados estatísticos do jogo
    stats=GameStats(ai_settings)

    #Cria o botão Ṕlay
    play_button=Button(ai_settings,screen,"Play")


    #Cria um personagem, seja espaçonave, seja pacman
    if(dados["nomePersonagem"].lower()=='pacman'):
        person=Pacman(screen,ai_settings)
        eh_pacman=True
    else:
        person=Ship(screen,ai_settings)

    #Cria painel de pontução
    sb=Scoreboard(ai_settings,screen,stats,eh_pacman)

    #Cria um grupo de estrelas cadente
    constellation=Group()

    #Cria um grupo de alienígenas para administrar
    aliens=Group()

    #Cria um grupo na qual serão armazenados os projéteis
    bullets=Group()

    #Cria a frota de alienígena
    gf.create_fleet(ai_settings,screen,person,aliens)

    #Cria as estrelas cadente
    gf.create_stars(ai_settings,screen,constellation)

    # Inicializa o laço principal do jogo
    while True:
        gf.check_events(ai_settings,screen,person,bullets,eh_pacman,play_button,stats,aliens,sb)
        if stats.game_active:

            person.update()
            gf.update_bullets(bullets,screen,aliens,ai_settings,person,stats,sb)
            gf.update_stars(constellation,screen.get_rect(),ai_settings)
            gf.update_screen(ai_settings,screen,person,aliens,bullets,constellation,play_button,stats,sb)
            gf.update_aliens(ai_settings,aliens,person,stats,screen,bullets,sb)

dados=ler_dados()
run_game(dados)