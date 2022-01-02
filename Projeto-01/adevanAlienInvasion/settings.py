import game_functions as gf
class Settings():
    '''Uma classe que armazena as configurações do jogo.'''
    def __init__(self,cor="azul"):
        self.screen_width=700
        self.screen_height=600
        #Cor RGB da tela no jogo
        self.bg_color=gf.get_cor(cor)
