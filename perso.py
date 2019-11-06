from maze_charging import *
from score import *
"""V1.0--This Module is in charge of moving MacGyver and tell if we pick an object """
class Perso():
    def __init__(self, pos_x, pos_y, structure_lab, list_macgyver):
        self.position_perso = (pos_x, pos_y)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.labyrinth = structure_lab 
        self.score = Score()
        self.list_macgyver = list_macgyver


    def move_macgyver(self, direction):
        x = self.list_macgyver[0]
        y = self.list_macgyver[1]
        as_picked_an_item = False
        # print(list_macgyver)
        if direction == 'right':
            print(self.labyrinth[y][x+1])
            if self.labyrinth[y][x+1] != '*':
                if self.labyrinth[y][x+1] == 'b':
                    if self.score.value != 3:
                        self.score.lose()
                    elif self.score.value == 3:
                        self.score.win()
                as_picked_an_item = self.pick_an_object(x+1, y)
                self.labyrinth[y][x] = "0"
                self.list_macgyver[0] += 1
                x += 1
                self.labyrinth[y][x] = "m"
                print("right")
                self.pos_x = self.pos_x + 1
        if direction == 'left':
            print(self.labyrinth[y][x-1])
            if self.labyrinth[y][x-1] != '*':
                if self.labyrinth[y][x-1] == 'b':
                    if self.score.value != 3:
                        self.score.lose()
                    elif self.score.value == 3:
                        self.score.win()
                as_picked_an_item = self.pick_an_object(x-1, y)
                self.labyrinth[y][x] = "0"
                self.list_macgyver[0] -= 1
                x -= 1
                print(x)
                self.labyrinth[y][x] = "m"
                print("left")
                self.pos_x = self.pos_x -1
        if direction == 'up':
            print(self.labyrinth[y-1][x])
            if self.labyrinth[y-1][x] != '*':
                if self.labyrinth[y-1][x] == 'b':
                    if self.score.value != 3:
                        self.score.lose()
                    elif self.score.value == 3:
                        self.score.win()
                as_picked_an_item = self.pick_an_object(x, y-1)
                self.labyrinth[y][x] = "0"
                self.list_macgyver[1] -= 1
                y -= 1
                self.labyrinth[y][x] = "m"
                print("up")
                self.pos_y = self.pos_y -1
        if direction == 'down':
            print(self.labyrinth[y+1][x])
            if self.labyrinth[y+1][x] != '*':
                if self.labyrinth[y+1][x] == 'b':
                    if self.score.value != 3:
                        self.score.lose()
                    elif self.score.value == 3:
                        self.score.win()
                as_picked_an_item = self.pick_an_object(x, y+1)
                self.labyrinth[y][x] = "0"
                self.list_macgyver[1] += 1
                y += 1
                self.labyrinth[y][x] = "m"
                print("down")
                self.pos_y = self.pos_y +1
        return as_picked_an_item
    
    def pick_an_object(self, x, y):
        if self.labyrinth[y][x] == 'e':
            print('ether')
            # self.score=self.score+1
            self.score.increm_value()
            return True
        if self.labyrinth[y][x] == 't':
            print('tube')
            self.score.increm_value()
            return True
        if self.labyrinth[y][x] == 'n':
            print('needle')
            self.score.increm_value()
            return True
        return False
        

    