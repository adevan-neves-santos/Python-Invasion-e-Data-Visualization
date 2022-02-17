import sys
import pygame
from bullet_lateral import BulletLateral
from pacman import Pacman
from bullet import Bullet
from alien import Alien
from star import Star
from time import sleep

def obj_hit(ai_settings,stats,screen,obj,aliens,bullets,sb):
    '''Responde ao fato de a espaçonave ter sido atingida por um alienígena.'''
    if(stats.obj_left>0):
        #Decrementa obj_left
        stats.obj_left-=1

        #Atualiza o painel de pontuações
        sb.prep_ships()

        #Esvazia a lista de alienígenas e de projéteis.
        aliens.empty()
        bullets.empty()

        #Cria uma nova frota e centraliza a espaçonave
        create_fleet(ai_settings,screen,obj,aliens)
        obj.center_obj()

        #Faz uma pausa
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)

def check_events(ai_settings,screen,obj,bullets,eh_pacman,play_button,stats,aliens,sb):
    '''Responde a eventos de pressionamento de teclas e de mouse.'''
    # Laço de eventos capturados por teclado
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            sys.exit()
        elif(event.type==pygame.MOUSEBUTTONDOWN):
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x,mouse_y,ai_settings,screen,obj,aliens,bullets,sb)
        elif(event.type==pygame.KEYDOWN):
            check_keydown_events(event,ai_settings,screen,obj,bullets,eh_pacman,stats,aliens,sb)
        elif(event.type==pygame.KEYUP):
            check_keyup_events(event,obj,eh_pacman)


def run_game(stats,ai_settings,screen,obj,aliens,bullets,sb):
    '''Inicia um novo jogo quando o jogador clicar em Play.'''
    if  not stats.game_active:
        #Oculta o cursor do mouse
        pygame.mouse.set_visible(False)

        #Reinicia os dados estatísticos
        stats.reset_stats()
        stats.game_active=True

        #Reinicia as imagens do painel de pontuação
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        #Esvazia a lista de alienígenas e de projéteis
        aliens.empty()
        bullets.empty()

        #Cria uma nova frota e centraliza a espaçonave
        create_fleet(ai_settings,screen,obj,aliens)
        obj.center_obj()


def check_play_button(stats,play_button,mouse_x,mouse_y,ai_settings,screen,obj,aliens,bullets,sb):
    '''Inicia um novo jogo quando o jogador clicar em Play.'''
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked:
        #Reinicia as configurações do jogo
        ai_settings.initialize_dynamic_settings()
        run_game(stats,ai_settings,screen,obj,aliens,bullets,sb)


def check_keydown_events(event,ai_settings,screen,obj,bullets,eh_pacman,stats,aliens,sb):
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
    elif(event.key==pygame.K_p):
        run_game(stats,ai_settings,screen,obj,aliens,bullets,sb)
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

def update_screen(ai_settings,screen,obj,aliens,bullets,constellation,play_button,stats,sb):
    '''Atualiza as imagens em tela e alterna para a nova tela.'''

    #Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)

    #Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    obj.blitme()
    aliens.draw(screen)
    constellation.draw(screen)
    #Desenha a informação de pontuação
    sb.show_score()

    # Desenha o botão d eplay, se o jogo estiver inativo
    if not stats.game_active:
        play_button.draw_button()

    #Deixa a tela mais recente visível
    pygame.display.flip()

def update_stars(constellation,screen,ai_settings):
    '''Atualiza a posição de cada estrela cadente.'''
    constellation.update()
    ##Irá apagar a estrela assim que sumir da tela
    for star in constellation.copy():
        if(star.rect.top>=ai_settings.screen_height):
            constellation.remove(star)
    if(len(constellation)==0):
        for i in range(10):
            new_star=Star(ai_settings,screen)
            constellation.add(new_star)


def update_bullets(bullets,screen,aliens,ai_settings,obj,stats,sb):
    '''Atualiza  a posição dos projéteis e remove projéteis antigos.'''
    bullets.update()
    #Apagua bullet se ele sumir da tela, economizando o processento desnecessário
    for bullet in bullets.copy():
        if((bullet.rect.bottom<=0) or (bullet.rect.right>=screen.get_rect().right)):
            bullets.remove(bullet)
    #Verifica se algum projétil atingiu os alienígenas
    #Em caso afirmativo, livra-se do projétil e do alienígena
    check_bullet_alien_collisions(ai_settings,screen,obj,aliens,bullets,stats,sb)

def check_bullet_alien_collisions(ai_settings,screen,obj,aliens,bullets,stats,sb):
    '''Responde a colisões entre projéteis e alienígenas.'''
    #Remove todo par projetil-nave quando colidem (sobrepoem)
    collision=pygame.sprite.groupcollide(bullets,aliens,True,True)

    if collision:
        for aliens in collision.values():

            stats.score+=ai_settings.aliens_points*len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)

    if(len(aliens)==0):
        #Destrói os projéteis existentes, aumenta a velocidade do jogo e cri uma nova frota

        bullets.empty()
        ai_settings.increase_speed()

        #Aumenta o nível
        stats.level+=1
        sb.prep_level()

        create_fleet(ai_settings,screen,obj,aliens)

def get_cor(cor):
    '''Retorna um código RGB da cor desejada na tela de fundo jogo.'''
    if(cor.upper()=="AZUL"):
        return (135,206,235)
    elif(cor.upper()=="VERDE"):
        return (144,238,144)
    elif(cor.upper()=="CINZA"):
        return (230,230,230)
    else:
        return (255,153,51)
    
def create_fleet(ai_settings,screen,obj,aliens):
    '''Cria uma frota completa de alienígena em uma linha.'''
    #Cria um alienígena e calcula o número de alienígenas em uma linha
    alien=Alien(ai_settings,screen)
    number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows=get_number_rows(ai_settings,obj.rect.height,alien.rect.height)

    #Cria a frota de alienígena
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def create_stars(ai_settings,screen,constellation):
    for i in range(3):
        new_star=Star(ai_settings,screen)
        constellation.add(new_star)

def get_number_aliens_x(ai_settings,alien_width):
    '''Determina o número de alienígenas que cabem em uma linha.'''
    available_space_x=ai_settings.screen_width-2*alien_width
    number_aliens_x=int(available_space_x/(2*alien_width))
    return number_aliens_x
    
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    '''Cria uma alienígena e o posiciona na linha.'''
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)

def get_number_rows(ai_settings,obj_height,alien_height):
    '''Determina o número de linhas com alienígenas que cabem na tela.'''
    available_space_y=(
        ai_settings.screen_height -
        (3*alien_height)-obj_height
    )
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows

def check_aliens_bottom(ai_settings,stats,screen,obj,aliens,bullets,sb):
    '''Verifica se algum alienígena alcançou a parte inferior da tela.'''
    screen_rect=screen.get_rect()

    for alien in aliens.sprites():
        if(alien.rect.bottom>=screen_rect.bottom):
            #Trata esse caso do mesmo modo que é feito quando a espaçonave é atinginda.
            obj_hit(ai_settings,stats,screen,obj,aliens,bullets,sb)
            break

def update_aliens(ai_settings,aliens,obj,stats,screen,bullets,sb):
    '''
    Verifica se a frota está em uma das bordas
      e então atualiza as posições de todos os alienígenas da frota.
    '''
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    #Verifica se houve colisões entre alienígenas e a espaçonave
    if pygame.sprite.spritecollideany(obj,aliens):
        obj_hit(ai_settings,stats,screen,obj,aliens,bullets,sb)
    
    #Verifica se algum alienígena atingiu a parte inferior da tela
    check_aliens_bottom(ai_settings,stats,screen,obj,aliens,bullets,sb)

def check_fleet_edges(ai_settings,aliens):
    '''Responde apropriadamente se alguma alineígena alcançou a borda.'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    '''Faz toda a frota descer e muda a sua direção.'''
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1

def check_high_score(stats,sb):
    '''Verifica se há uma pontuação máxima.'''
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        sb.prep_high_score()
