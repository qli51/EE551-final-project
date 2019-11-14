import sys
import pygame
import random
import time
from datamain import*
from Piece import piece
from Wall import wall
from Gamedisplay import gamedisplay
from Gamestate import gamestate
from Gameresourse import gameresourse

def check_event(a):
    for item in pygame.event.get():
        if item.type == pygame.QUIT:
            sys.exit()
        elif item.type == pygame.USEREVENT:
            a.piece.move_down()
        elif item.type == pygame.KEYDOWN:
            if item.key == pygame.K_DOWN and not a.pause:
                if a.piece:
                    print('Press the down key')
                    a.piece.move_down()
            elif item.key == pygame.K_UP and not a.pause:
                if a.piece:
                    print('Press the up key')
                    a.piece.turn_one()
            elif item.key == pygame.K_LEFT and not a.pause:
                if a.piece:
                    print('Press the left key')
                    a.piece.move_left()
            elif item.key == pygame.K_RIGHT and not a.pause:
                if a.piece:
                    print('Press the right key')
                    a.piece.move_right()
            elif item.key == pygame.K_f and not a.pause:
                if a.piece:
                    a.piece.fall_down()
            elif item.key == pygame.K_s and a.stop:
                a.game_start()
            elif item.key == pygame.K_q:
                sys.exit()
            elif item.key == pygame.K_m:
                a.resouse.pause_music()
            elif item.key == pygame.K_p and not a.stop:
                if a.pause:
                    a.game_resume()
                else:
                    a.game_pause()
            elif item.key == pygame.K_r and a.end:
                a.game_restart()
            elif item.key == pygame.K_c and not a.stop:
                a.game_restart()


def main():
    pygame.init()
    screen = pygame.display.set_mode((Screenwidth, Screenheight))
    pygame.display.set_caption("Tetris")
    pygame.key.set_repeat(10,100)
    game_state=gamestate(screen)
    game_resourse=gameresourse()
    game_resourse.play_music()
    while True:
        if game_state.piece and game_state.piece.bottom:
            game_state.wall.add_wall(game_state.piece)
            game_state.eliminate_line()
            game_state.difficult_level()
            game_state.whether_end()
        check_event(game_state)
        screen.blit(game_resourse.bg_picture(),(0,0))
        gamedisplay.draw_game_area(screen,game_state,game_resourse)
        gamedisplay.draw_score(screen,score=game_state.score,level=game_state.difficult)
        if game_state.piece:
            game_state.piece.paint()
        pygame.display.update()
if __name__ == '__main__':
    main()


