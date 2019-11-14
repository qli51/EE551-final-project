from datamain import*
from Piece import piece
from Wall import wall
from Gameresourse import gameresourse
import pygame
import random

class gamestate():
    count=1
    def __init__(self,screen):
        self.screen=screen
        self.wall=wall(screen)
        self.resouse=gameresourse()
        self.piece=None
        self.nextpice=None
        self.timer_interval=TIMER_INTERVAL
        self.score=0
        self.stop=True
        self.pause=False
        self.end=False
        self.difficult=1

    def game_start(self):
        self.piece=piece(random.choice(Type),self.screen,self.wall)
        self.stop=False
        self.timer_interval = TIMER_INTERVAL #the time interval of timer
        self.set_timer(self.timer_interval)#start the timer

    def set_timer(self,time_interval):
        pygame.time.set_timer(pygame.USEREVENT,time_interval)

    def eliminate_line(self):
        eliminate=[]
        for i in range(20):
            if self.wall.is_full(i):
                eliminate.append(i)
        for i in eliminate:
            self.wall.copy_down(i)
        for i in range(10):
            self.wall.area[0][i]=Wall_blank
        eliminate_num=len(eliminate)
        assert (eliminate_num<=4 and eliminate_num>=0)
        if eliminate_num <= 1:
            score = eliminate_num * 100
        elif eliminate_num == 2:
            score = eliminate_num * 150
        elif eliminate_num >= 3:
            score = eliminate_num * 200
        self.score=self.score+score
        if self.difficult==1 and self.score>=500:
            self.difficult=self.difficult+1
        if self.difficult==2 and self.difficult==2000:
            self.difficult=self.difficult+1

    def game_pause(self):
        pygame.time.set_timer(pygame.USEREVENT,0)
        self.pause=True

    def game_resume(self):
        self.set_timer(self.timer_interval)
        self.pause=False

    def whether_end(self):
        for i in range(10):
            if self.wall.is_wall(i,1):
                self.end=True
                break
        if not self.end:
            self.piece=piece(random.choice(Type),self.screen,self.wall)
        else:
            pygame.time.set_timer(pygame.USEREVENT,0)

    def game_restart(self):
        for i in range(10):
            for j in range(20):
                self.wall.area[j][i]=Wall_blank
        self.score=0
        self.end=False
        self.set_timer(self.timer_interval)
        self.piece = piece(random.choice(Type), self.screen, self.wall)
        gamestate.count=gamestate.count+1

    def difficult_level(self):
        if self.difficult==2:
            pygame.time.set_timer(pygame.USEREVENT,750)
        elif self.difficult==3:
            pygame.time.set_timer(pygame.USEREVENT,500)

















