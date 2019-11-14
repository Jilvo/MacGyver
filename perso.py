"""V1.1--This Module is in charge of moving MacGyver and tell if we pick an object
-Import maze and score """
from score import Score

class Perso():
    """Class for the deplacement of the player and tell to class score to increm the score """
    def __init__(self, pos_x, pos_y, structure_lab, list_macgyver):
        self.position_perso = (pos_x, pos_y)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.labyrinth = structure_lab
        self.score = Score()
        self.list_macgyver = list_macgyver

    def move_macgyver(self, direction):
        """This fonction is in charge of the deplacement """
        actual_x = self.list_macgyver[0]
        actual_y = self.list_macgyver[1]
        as_picked_an_item = False
        # print(list_macgyver)
        if direction == 'right':
            print(self.labyrinth[actual_y][actual_x+1])
            if self.labyrinth[actual_y][actual_x+1] != '*':
                if self.labyrinth[actual_y][actual_x+1] == 'b':
                    if self.score.value != 3:
                        self.score.lose()
                    elif self.score.value == 3:
                        self.score.win()
                as_picked_an_item = self.pick_an_object(actual_x+1, actual_y)
                self.labyrinth[actual_y][actual_x] = "0"
                self.list_macgyver[0] += 1
                actual_x += 1
                self.labyrinth[actual_y][actual_x] = "m"
                print("right")
                self.pos_x = self.pos_x + 1
        if direction == 'left':
            print(self.labyrinth[actual_y][actual_x-1])
            if self.labyrinth[actual_y][actual_x-1] != '*':
                if self.labyrinth[actual_y][actual_x-1] == 'b':
                    if self.score.value != 3:
                        self.score.lose()
                    elif self.score.value == 3:
                        self.score.win()
                as_picked_an_item = self.pick_an_object(actual_x-1, actual_y)
                self.labyrinth[actual_y][actual_x] = "0"
                self.list_macgyver[0] -= 1
                actual_x -= 1
                print(actual_x)
                self.labyrinth[actual_y][actual_x] = "m"
                print("left")
                self.pos_x = self.pos_x -1
        if direction == 'up':
            print(self.labyrinth[actual_y-1][actual_x])
            if self.labyrinth[actual_y-1][actual_x] != '*':
                if self.labyrinth[actual_y-1][actual_x] == 'b':
                    if self.score.value != 3:
                        self.score.lose()
                    elif self.score.value == 3:
                        self.score.win()
                as_picked_an_item = self.pick_an_object(actual_x, actual_y-1)
                self.labyrinth[actual_y][actual_x] = "0"
                self.list_macgyver[1] -= 1
                actual_y -= 1
                self.labyrinth[actual_y][actual_x] = "m"
                print("up")
                self.pos_y = self.pos_y -1
        if direction == 'down':
            print(self.labyrinth[actual_y+1][actual_x])
            if self.labyrinth[actual_y+1][actual_x] != '*':
                if self.labyrinth[actual_y+1][actual_x] == 'b':
                    if self.score.value != 3:
                        self.score.lose()
                    elif self.score.value == 3:
                        self.score.win()
                as_picked_an_item = self.pick_an_object(actual_x, actual_y+1)
                self.labyrinth[actual_y][actual_x] = "0"
                self.list_macgyver[1] += 1
                actual_y += 1
                self.labyrinth[actual_y][actual_x] = "m"
                print("down")
                self.pos_y = self.pos_y + 1
        return as_picked_an_item
    def pick_an_object(self, actual_x, actual_y):
        """Look the object we pick tell to class score to increm the score """
        if self.labyrinth[actual_y][actual_x] == 'e':
            print('ether')
            # self.score=self.score+1
            self.score.increm_value()
            return True
        if self.labyrinth[actual_y][actual_x] == 't':
            print('tube')
            self.score.increm_value()
            return True
        if self.labyrinth[actual_y][actual_x] == 'n':
            print('needle')
            self.score.increm_value()
            return True
        return False
        