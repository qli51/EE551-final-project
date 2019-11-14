from datamain import*
import pygame
class gamedisplay():
    @staticmethod
    def draw_cell(screen,x,y,color):
        cell_rect = pygame.Rect((x * Cellwidth + Leftwidth + 1, y * Cellwidth + Topwidth + 1),(Cellwidth - 2, Cellwidth - 2))
        pygame.draw.rect(screen,color, cell_rect)

    @staticmethod
    def draw_wall(game_wall):
        for i in range(20):
            for j in range(10):
                if game_wall.area[i][j] !=Wall_blank:
                    gamedisplay.draw_cell(game_wall.screen,j,i,Color[game_wall.area[i][j]])

    @staticmethod
    def draw_game_area(screen,game_state,game_resourse):
        top_border=pygame.Rect(Leftwidth,Topwidth,2+400,2)
        pygame.draw.rect(screen,Edgecolor,top_border)
        left_border=pygame.Rect(Leftwidth,Topwidth,2,2+800)
        pygame.draw.rect(screen, Edgecolor, left_border)
        bottom_border=pygame.Rect(Leftwidth,Topwidth+800,2+400,2)
        pygame.draw.rect(screen, Edgecolor, bottom_border)
        right_border = pygame.Rect(Leftwidth+2+400,Topwidth,2,2+800)
        pygame.draw.rect(screen, Edgecolor, right_border)
        gamedisplay.draw_wall(game_state.wall)
        if game_state.stop:
            gamedisplay.draw_picture1(screen,game_resourse)
        if game_state.pause:
            gamedisplay.draw_picture2(screen,game_resourse)
        if game_state.end:
            gamedisplay.draw_picture4(screen, game_resourse)


    @staticmethod
    def draw_score(screen,score,level):
        score_label_front=pygame.font.SysFont('arial', 28)
        score_label_surface=score_label_front.render('Score',False,Edgecolor)
        score_label_position=(Leftwidth+Gamewidth+20,Topwidth)
        screen.blit(score_label_surface,score_label_position)
        score_font=pygame.font.SysFont('arial',28)
        score_surface=score_font.render(str(score),False,Scorecolor)
        score_position=(Leftwidth+Gamewidth+100,Topwidth)
        screen.blit(score_surface,score_position)
        level_label_font = pygame.font.SysFont('arial', 28)
        level_label_surface = level_label_font.render('Level', False,Edgecolor)
        level_label_position = (Leftwidth + Gamewidth+20, Topwidth+50)
        screen.blit(level_label_surface,level_label_position)
        level_font = pygame.font.SysFont('arial', 28)
        level_surface = level_font.render(str(level), False, Scorecolor)
        level_position = (Leftwidth + Gamewidth + 100, Topwidth + 50)
        screen.blit(level_surface, level_position)
        title_font = pygame.font.SysFont('stkaiti', 28)
        title_surface = title_font.render('Game point：', True, Titlecolor)
        title_position = (40,Topwidth)
        screen.blit(title_surface, title_position)
        gamectrl_label_font = pygame.font.SysFont('stkaiti', 25)
        gamectrl_label_surface = gamectrl_label_font.render('Game control', True, Titlecolor)
        gamectrl_label_position = (40, Topwidth+60)
        screen.blit(gamectrl_label_surface, gamectrl_label_position)
        man_font = pygame.font.SysFont('stkaiti', 24)
        man_down_surface = man_font.render('Start：s  End：q', True, Edgecolor)
        man_down_position = (40,  Topwidth+100)
        screen.blit(man_down_surface, man_down_position)
        man_pause_surface = man_font.render('Stop：p', True, Edgecolor)
        man_pause_position = (40,  Topwidth+140)
        screen.blit(man_pause_surface, man_pause_position)
        man_restart_surface = man_font.render('Restart：c', True, Edgecolor)
        man_restart_position = (40,  Topwidth+180)
        screen.blit(man_restart_surface, man_restart_position)
        man_music_surface = man_font.render('Stop/Resume music：m', True, Edgecolor)
        man_music_position = (40,  Topwidth+220)
        screen.blit(man_music_surface, man_music_position)
        gamectrl_label_surface = gamectrl_label_font.render('Piece control', True, Titlecolor)
        gamectrl_label_position = (40,  Topwidth+280)
        screen.blit(gamectrl_label_surface, gamectrl_label_position)
        man_down_surface = man_font.render('Trun：key top  Down：key down', True, Edgecolor)
        man_down_position = (40,  Topwidth+320)
        screen.blit(man_down_surface, man_down_position)
        man_move_surface = man_font.render('Left：key left  Right：key right',  True, Edgecolor)
        man_move_position = (40,  Topwidth+360)
        screen.blit(man_move_surface, man_move_position)
        man_speed_surface = man_font.render('Down to bootom：key f',  True, Edgecolor)
        man_speed_position = (40,  Topwidth+400)
        screen.blit(man_speed_surface, man_speed_position)

    @staticmethod
    def draw_picture1(screen,game_resourse):
        start_position=(240,Topwidth-125)
        screen.blit(game_resourse.start_image(),start_position)

    @staticmethod
    def draw_picture2(screen,game_resourse):
        start_position = (350, Topwidth-125)
        screen.blit(game_resourse.restart_image(), start_position)

    @staticmethod
    def draw_picture3(screen, game_resourse):
        start_position = (Leftwidth + Gamewidth + 20, Topwidth-125)
        screen.blit(game_resourse.stop_image(), start_position)

    @staticmethod
    def draw_picture4(screen, game_resourse):
        start_position = (420,Topwidth-125)
        screen.blit(game_resourse.end_image(), start_position)

    @staticmethod
    def draw_picture5(screen, game_resourse):
        start_position = (Leftwidth + Gamewidth + 20, Topwidth-125)
        screen.blit(game_resourse.second_image(), start_position)

