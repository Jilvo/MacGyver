#V0.1.2
#Import the labyrinth's file
balise_player=0
balise_bad_guy=0
from random import *
#print("MacGyver est situé",labyrinth.index('*'));
#for i in range(0,16):
 #   if "m" in labyrinth[i][balise_player]:
  #      print("MacGyver is in the list",i,"at the position",labyrinth[i].index("m"));
   #     break
    #else:
     #   #print("searching...");
      #  pass
    #balise_player=0
class labyrinth():
#create a class for the labyrinth  
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0
	
    def generate(self):
        with open('labyrinth.txt') as fichier:
            global structure_labyrinth
            structure_labyrinth=[]
            line = fichier.readline()
            cnt = 0
            while line:
                print([line[i:i+1] for i in range(0,len(line),1)])
                print("Line {}: {}".format((cnt+1), line.strip()))
                structure_labyrinth.append([line[i:i+1] for i in range(0,len(line),1)])
                if '\n' in line:
                    structure_labyrinth[cnt].remove('\n')
                    print("present")

                line = fichier.readline()
                cnt += 1
                
            print(structure_labyrinth)
            fichier.close()
    def find_player(self):
#find MacGyver    
        for y,lst in enumerate(structure_labyrinth):
            for x,color in enumerate(lst):
                if color == "m":
                    print("MacGyver is in ",x,"list at the", y,"position")
        
#find the bad guy
        for y,lst in enumerate(structure_labyrinth):
            for x,color in enumerate(lst):
                if color == "b":
                    print("The bad guy is in ",x,"list at the", y,"position")

    def set_the_object(self):
        structure_labyrinth[randint(1,14)][randint(1,14)]="e"
        structure_labyrinth[randint(1,14)][randint(1,14)]="n"
        structure_labyrinth[randint(1,14)][randint(1,14)]="t"
        
        print(structure_labyrinth)

        for y,lst in enumerate(structure_labyrinth):
            for x,color in enumerate(lst):
                if color == "e":
                    print("the ether is in ",x,"list at the", y,"position")
                    list_ether=[]
                    list_ether.append(x)
                    list_ether.append(y)
        for y,lst in enumerate(structure_labyrinth):
            for x,color in enumerate(lst):
                if color == "n":
                    print("the needle is in ",x,"list at the", y,"position")
                    list_needle=[]
                    list_needle.append(x)
                    list_needle.append(y)
        for y,lst in enumerate(structure_labyrinth):
            for x,color in enumerate(lst):
                if color == "t":
                    print("the tube is in ",x,"list at the", y,"position")
                    list_tube=[]
                    list_tube.append(x)
                    list_tube.append(y)
        if list_tube == list_needle or list_tube== list_ether:
            structure_labyrinth[randint(1,14)][randint(1,14)]="t"
        elif list_needle == list_ether :
            structure_labyrinth[randint(1,14)][randint(1,14)]="n"
        else:
            print("les 3 objets sont placés à des endroits différents")
            # indexes = [(i, j) for i, nl in enumerate(structure_labyrinth) for j, nle in enumerate(nl)]
            # print(*indexes, sep="\n")
            # fichier.close()

# class perso():
    
#     def init(self):
# 	    self.x=0
# 	    self.y=0

#     def deplacer(self,direction,x,y):
#         if direction == 'right':
#             self.x += 1
#             print("right")
#             print(self.x,self.y)
#         if direction == 'left':
#             self.x -= 1
#             print("left")
#             print(self.x,self.y)
#         if direction == 'up':
#             self.y -= 1
#             print("up")
#             print(self.x,self.y)
#         if direction == 'down':
#             self.y += 1
#             print("down")
#             print(self.x,self.y)


game=labyrinth('labyrinth.txt')
game.generate()
game.find_player()
game.set_the_object()
#direction = input("chose direction : ")
# deplacement=perso()
# deplacement.init()
# deplacement.deplacer(direction)
