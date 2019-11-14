from datamain import*
from Gamedisplay import gamedisplay
class wall():
    def __init__(self,screen):
        self.screen=screen
        self.area=[]
        line=[Wall_blank]*10
        for i in range(20):
            self.area.append(line.copy())

    def print(self):
        print("y",len(self.area),"x",len(self.area[0]))
        for i in self.area:
            print(i)

    def add_wall(self,piece):
        shape_turn=PIECE[piece.shape][piece.turn]
        for i in range(len(shape_turn)):
            for j in range(len(shape_turn[0])):
                if shape_turn[i][j]=='1':
                    self.set_cell(piece.x+j,piece.y+i,piece.shape)

    def set_cell(self,x,y,label):
        self.area[y][x]=label

    def is_wall(self,x,y):
        if self.area[y][x] != Wall_blank:
            return True
        return False

    def is_full(self,row):
        for i in range(10):
            if self.area[row][i]==Wall_blank:
                return False
        return True

    def copy_down(self,row):
        for i in range(row,0,-1):
            for j in range(10):
                self.area[i][j]=self.area[i-1][j]







