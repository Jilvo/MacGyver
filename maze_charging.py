"""Import the ramdom module for put the object in the maze"""
from random import randint
"""V1.1--This Module is in charge of charging the labyrinth by"""
"""reading the .txt ,find the player and set the objects """
class Labyrinth():
    """create a class for the labyrinth"""
    def __init__(self, file):
        self.file = file
        self.structure = []

    def generate(self):
        """Generate the labyrinth by reading the .txt and add this to a list of list """
        with open('labyrinth.txt') as file:
            structure_labyrinth = []
            line = file.readline()
            cnt = 0
            while line:
                print([line[i:i+1] for i in range(0, len(line), 1)])
                print("Line {}: {}".format((cnt+1), line.strip()))
                structure_labyrinth.append([line[i:i+1] for i in range(0, len(line), 1)])
                if '\n' in line:
                    structure_labyrinth[cnt].remove('\n')
                line = file.readline()
                cnt += 1
            print(structure_labyrinth)
            self.structure = structure_labyrinth

    def find_player(self):
        """find the player and put the position in a list"""
        list_macgyver = []
        for column, lst in enumerate(self.structure):
            for lign, abs_m in enumerate(lst):
                if abs_m == "m":
                    # print("MacGyver is in ",y,"list at the", x,"position")
                    mac_x = lign
                    mac_y = column
                    list_macgyver.append(lign)
                    list_macgyver.append(column)
        return(mac_x, mac_y, list_macgyver)

    def set_the_object(self):
        """set_the_object"""
        char = {}
        char['ether'] = 'e'
        char['needle'] = 'n'
        char['tube'] = 't'
        list_item = []
        for i in char.values():
            while True:
                rand_x = randint(1, 13)
                rand_y = randint(1, 13)
                if self.structure[rand_x][rand_y] == '0':
                    self.structure[rand_x][rand_y] = i
                    print(i, rand_x, rand_y)
                    break
        list_item.append(char)
        print(list_item)
