import game_functions as gf
class Settings():
    '''Uma classe que armazena as configurações do jogo.'''
    def __init__(self,cor="azul"):
        self.screen_width=1200
        self.screen_height=700
        #Cor RGB da tela no jogo
        self.bg_color=gf.get_cor(cor)

        #Configurações do personagem
        self.person_speed_factor=1.5

        #Configurações de projéteis
        self.bullet_speed_factor=1
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=3
