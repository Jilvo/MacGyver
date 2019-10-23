from loading import *

class Perso():
    def __init__(self,pos_x,pos_y,structure_lab):
        self.position_perso = (pos_x,pos_y)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.labyrinth = structure_lab 
        self.score = 0

    def deplacer(self,direction):
        # x=list_macgyver[0]
        # y=list_macgyver[1]
        # case_x=0
        # case_y=0
        # print(list_macgyver)
        if direction == 'right':
            print(self.labyrinth[y][x+1])
            if self.labyrinth[y][x+1]!='*':
                if self.labyrinth[y][x+1] =='b':
                    if self.score!=3:
                        Score.lose(self)
                    elif self.score==3:
                        Score.win(self)
                if self.labyrinth[y][x+1] =='e':
                    print('ether')
                    self.score=self.score+1
                if self.labyrinth[y][x+1] =='t':
                    print('tube')
                    self.score=self.score+1
                if self.labyrinth[y][x+1] =='n':
                    print('needle')
                    self.score=self.score+1
                self.labyrinth[y][x]="0"
                list_macgyver[0] += 1
                x+=1
                self.labyrinth[y][x]="m"
                print("right")
                self.pos_x=self.pos_x +1
        if direction == 'left':
            print(self.labyrinth[y][x-1])
            if self.labyrinth[y][x-1]!='*':
                if self.labyrinth[y][x-1] =='b':
                    if self.score!=3:
                        Score.lose(self)
                    elif self.score==3:
                        Score.win(self)
                if self.labyrinth[y][x-1] =='e':
                    print('ether')
                    self.score=self.score+1
                if self.labyrinth[y][x-1] =='t':
                    print('tube')
                    self.score=self.score+1
                if self.labyrinth[y][x-1] =='n':
                    print('needle')
                    self.score=self.score+1
                self.labyrinth[y][x]="0"
                list_macgyver[0] -= 1
                x-=1
                print(x)
                self.labyrinth[y][x]="m"
                print("left")
                self.pos_x=self.pos_x -1
        if direction == 'up':
            print(self.labyrinth[y-1][x])
            if self.labyrinth[y-1][x]!='*':
                if self.labyrinth[y-1][x] =='b':
                    if self.score!=3:
                        Score.lose(self)
                    elif self.score==3:
                        Score.win(self)
                if self.labyrinth[y-1][x] =='e':
                    print('ether')
                    self.score=self.score+1
                if self.labyrinth[y-1][x] =='t':
                    print('tube')
                    self.score=self.score+1
                if self.labyrinth[y-1][x] =='n':
                    print('needle')
                    self.score=self.score+1
                self.labyrinth[y][x]="0"
                list_macgyver[1] -= 1
                y-=1
                self.labyrinth[y][x]="m"
                print("up")
                self.pos_y=self.pos_y -1
        if direction == 'down':
            print(self.labyrinth[y+1][x])
            if self.labyrinth[y+1][x]!='*':
                if self.labyrinth[y+1][x] =='b':
                    if self.score!=3:
                        Score.lose(self)
                    elif self.score==3:
                        Score.win(self)
                if self.labyrinth[y+1][x] =='e':
                    print('ether')
                    self.score=self.score+1
                if self.labyrinth[y+1][x] =='t':
                    print('tube')
                    self.score=self.score+1
                if self.labyrinth[y+1][x] =='n':
                    print('needle')
                    self.score=self.score+1
                self.labyrinth[y][x]="0"
                list_macgyver[1] += 1
                y+=1
                self.labyrinth[y][x]="m"
                print("down")
                self.pos_y=self.pos_y +1
        
            
            
            
        