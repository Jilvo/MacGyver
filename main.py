#V0.1.2
#Import the labyrinth's file
balise_player=0
balise_bad_guy=0
score=0
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
                    print("MacGyver is in ",y,"list at the", x,"position")
                    global list_macgyver
                    list_macgyver=[]
                    list_macgyver.append(y)
                    list_macgyver.append(x)
        
#find the bad guy
        for y,lst in enumerate(structure_labyrinth):
            for x,color in enumerate(lst):
                if color == "b":
                    print("The bad guy is in ",y,"list at the", x,"position")
                    

    def set_the_object(self):
        structure_labyrinth[randint(1,14)][randint(1,14)]="e"
        structure_labyrinth[randint(1,14)][randint(1,14)]="n"
        structure_labyrinth[randint(1,14)][randint(1,14)]="t"
        global list_object
        list_object=[]
        print(structure_labyrinth)

        for y,lst in enumerate(structure_labyrinth):
            for x,color in enumerate(lst):
                if color == "e":
                    print("the ether is in ",y,"list at the", x,"position")
                    list_ether=[]
                    list_ether.append(y)
                    list_ether.append(x)
                    list_object.append(list_ether)
        for y,lst in enumerate(structure_labyrinth):
            for x,color in enumerate(lst):
                if color == "n":
                    print("the needle is in ",y,"list at the", x,"position")
                    list_needle=[]
                    list_needle.append(y)
                    list_needle.append(x)
                    list_object.append(list_needle)
        for y,lst in enumerate(structure_labyrinth):
            for x,color in enumerate(lst):
                if color == "t":
                    print("the tube is in ",y,"list at the", x,"position")
                    list_tube=[]
                    list_tube.append(y)
                    list_tube.append(x)
                    list_object.append(list_tube)
        if list_tube == list_needle or list_tube== list_ether:
            structure_labyrinth[randint(1,14)][randint(1,14)]="t"
        elif list_needle == list_ether :
            structure_labyrinth[randint(1,14)][randint(1,14)]="n"
        else:
            print("les 3 objets sont placés à des endroits différents")
            # indexes = [(i, j) for i, nl in enumerate(structure_labyrinth) for j, nle in enumerate(nl)]
            # print(*indexes, sep="\n")
            # fichier.close()
        

#class perso():

    def deplacer(self,direction):
        x=list_macgyver[0]
        y=list_macgyver[1]
        print(list_macgyver)
        if direction == 'right':
            structure_labyrinth[y][x]="0"
            list_macgyver[0] += 1
            x+=1
            structure_labyrinth[y][x]="m"
            print("right")
        if direction == 'left':
            structure_labyrinth[y][x]="0"
            list_macgyver[0] -= 1
            x-=1
            print(x)
            structure_labyrinth[y][x]="m"
            print("left")
        if direction == 'up':
            structure_labyrinth[y][x]="0"
            list_macgyver[1] -= 1
            y-=1
            structure_labyrinth[y][x]="m"
            print("up")
        if direction == 'down':
            structure_labyrinth[y][x]="0"
            list_macgyver[1] += 1
            y+=1
            structure_labyrinth[y][x]="m"
            print("down")
        
            
        print(x,y)
        print(structure_labyrinth)
   # def replace_value(self,list_macgyver):
    def scoring(self,list_macgyver,list_object):
        print(list_macgyver)
        print(list_object)
        for i in list_object:
            for j in i:
                if list_macgyver == list_object[2]:
                    score+=1
                    print("Le score est passé a : ",score)
    


print("Le Score est de :",score)
game=labyrinth('labyrinth.txt')
game.generate()
game.find_player()
game.set_the_object()
direction = input("chose direction : ")
game.deplacer(direction)
game.scoring(list_macgyver,list_object)
# deplacement=perso()
# deplacement.init()
# deplacement.deplacer(direction)
