import game_functions as gf
class Settings():
    '''Uma classe que armazena as configurações do jogo.'''
    def __init__(self,cor="azul"):
        '''Inicializa as configurações estáticas do jogo.'''

        #Configurações da tela
        self.screen_width=900#1200
        self.screen_height=500#700
        #Cor RGB da tela no jogo
        self.bg_color=gf.get_cor(cor)

        #Configurações do personagem
        self.person_limit=3

        #Configurações de projéteis
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=3

        #Configurações dos alienígenas
        self.fleet_drop_speed=10
        
        # A taxa com que a velocidade do jogo aumenta
        self.speedup_scale=1.1
        # A taxa com que os pontos para cada alienígena aumentam
        self.score_scale=1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Inicializa as configurações que mudam no decorrer do jogo.'''
        self.person_speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=1
        self.aliens_points=50

        # fleet_direction igual 1 significa á dirreita; -1 significa à esquerda.
        self.fleet_direction=1

        

    def increase_speed(self):
        '''Aumenta configurações de velocidade.'''
        self.person_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        #Pontuação
        self.aliens_points=int(self.aliens_points*self.score_scale)