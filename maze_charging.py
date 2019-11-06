from random import randint
"""V1.0--This Module is in charge of charging the labyrinth
by read the .txt ,find the player and set the objects """
class Labyrinth():
#create a class for the labyrinth  
    def __init__(self, file):
        self.file = file
        self.structure = []
	
    def generate(self):
        with open('labyrinth2.txt') as file:
            structure_labyrinth = []
            line = file.readline()
            cnt = 0
            while line:
                print([line[i:i+1] for i in range(0,len(line), 1)])
                print("Line {}: {}".format((cnt+1), line.strip()))
                structure_labyrinth.append([line[i:i+1] for i in range(0,len(line), 1)])
                if '\n' in line:
                    structure_labyrinth[cnt].remove('\n')
                line = file.readline()
                cnt += 1      
            print(structure_labyrinth)
            file.close()
            self.structure = structure_labyrinth
 #find MacGyver 
    def find_player(self):
        list_macgyver = []    
        for y, lst in enumerate(self.structure):
            for x, abs_m in enumerate(lst):
                if abs_m == "m":
                    # print("MacGyver is in ",y,"list at the", x,"position")
                    mac_x = x
                    mac_y = y
                    list_macgyver.append(x)
                    list_macgyver.append(y)
        return(mac_x, mac_y, list_macgyver)
# set_the_object
    def set_the_object(self):
        char = {}
        char['ether'] = 'e'
        char['needle'] = 'n'
        char['tube'] = 't'
        list_item = []
        for i in char.values():
            rand_x = randint(1, 13)
            rand_y = randint(1, 13)
            if self.structure[rand_x][rand_y] == '0':
                self.structure[rand_x][rand_y] = i
            else:
                rand_x = randint(1, 13)
                rand_y = randint(1, 13)
                if self.structure[rand_x][rand_y] == '0':
                    self.structure[rand_x][rand_y] = i
            print(list_item)
