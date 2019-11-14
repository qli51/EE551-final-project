import pygame
from datamain import*
from Gamedisplay import gamedisplay
class piece():
    def __init__(self,shape,screen,game_wall):
        self.x=3
        self.y=0
        self.turn=0
        self.shape=shape
        self.screen=screen
        self.bottom=False
        self.game_wall=game_wall

    def draw_cell(self,x,y):
        gamedisplay.draw_cell(self.screen,x,y,Color[self.shape])

    def paint(self):
        shape_template=PIECE[self.shape]
        shape_trun=shape_template[self.turn]
        for a in range(len(shape_trun)):
            for b in range(len(shape_trun[0])):
                if(shape_trun[a][b]=='1'):
                    self.draw_cell(self.x+b,self.y+a)

    def can_right(self):
        shape_kind=PIECE[self.shape]
        shape_true=shape_kind[self.turn]
        for a in range(len(shape_true)):
            for b in range(len(shape_true[0])):
                if (shape_true[a][b] == '1'):
                    if self.x+b>=9 or self.game_wall.is_wall(self.x+b+1,self.y+a)==True:
                        return False
                    else:
                        continue
        return True

    def can_left(self):
        shape_kind = PIECE[self.shape]
        shape_true = shape_kind[self.turn]
        for a in range(len(shape_true)):
            for b in range(len(shape_true[0])):
                if (shape_true[a][b] == '1'):
                    if self.x + b <=0 or self.game_wall.is_wall(self.x+b-1,self.y+a)==True:
                        return False
                    else:
                        continue
        return True

    def can_down(self):
        shape_kind = PIECE[self.shape]
        shape_true = shape_kind[self.turn]
        for a in range(len(shape_true)):
            for b in range(len(shape_true[0])):
                if (shape_true[a][b] == '1'):
                    if self.y + a >=19 or self.game_wall.is_wall(self.x+b,self.y+a+1)==True:
                        return False
                    else:
                        continue
        return True

    def move_right(self):
        if self.can_right():
            self.x = self.x + 1

    def move_left(self):
        if self.can_left():
            self.x = self.x - 1

    def move_down(self):
        if self.can_down():
            self.y = self.y + 1
        else:
            self.bottom=True

    def fall_down(self):
        while not self.bottom:
            self.move_down()

    def turn_one(self):
        shape_max_len=len(PIECE[self.shape])
        if self.can_turn():
            self.turn = (self.turn + 1) % shape_max_len

    def can_turn(self):
        shape_max_len = len(PIECE[self.shape])
        turn = (self.turn + 1) % shape_max_len
        shape_kind=PIECE[self.shape]
        shape_true=shape_kind[turn]
        for i in range(len(shape_true)):
            for j in range(len(shape_true[0])):
                if (shape_true[i][j]=='1'):
                    if (self.x+j<0 or self.x+j>9) or (self.y+i<0 or self.y+i>19):
                        return False
        return True





