#V0.7
#Import the labyrinth's file
balise_player=0
balise_bad_guy=0
import pygame
from random import randint
from constantes import *
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
        self.structure = []
	
    def generate(self):
        with open('macgyver/labyrinth.txt') as fichier:
            
            structure_labyrinth=[]
            line = fichier.readline()
            cnt = 0
            while line:
                print([line[i:i+1] for i in range(0,len(line),1)])
                print("Line {}: {}".format((cnt+1), line.strip()))
                structure_labyrinth.append([line[i:i+1] for i in range(0,len(line),1)])
                if '\n' in line:
                    structure_labyrinth[cnt].remove('\n')
                    #print("present")

                line = fichier.readline()
                cnt += 1
                
            print(structure_labyrinth)
            fichier.close()
            self.structure=structure_labyrinth
    def find_player(self):
#find MacGyver    
        for y,lst in enumerate(self.structure):
            for x,abs_m in enumerate(lst):
                if abs_m == "m":
                    # print("MacGyver is in ",y,"list at the", x,"position")
                    global list_macgyver
                    mac_x=x
                    mac_y=y
                    list_macgyver=[]
                    list_macgyver.append(x)
                    list_macgyver.append(y)
        return (mac_x,mac_y)

        

#find the bad guy
        # for y,lst in enumerate(self.structure):
        #     for x,abs_m in enumerate(lst):
        #         if abs_m == "b":
        #             #  print("The bad guy is in ",y,"list at the", x,"position")
        #             global list_badguy
        #             list_badguy=[]
        #             list_badguy.append(x)
        #             list_badguy.append(y)
        #             pass
                    

    def set_the_object(self):

        # char={}
            # char['ether']='e'
            # char['needle']='n'
            # char['tube']='t'
            # global list_item
            # list_item=[]
            
            # for item,char_item in char.items():
            #     rand_x=randint(1,13)
            #     rand_y=randint(1,13)
            #     self.structure[rand_nd_x][ray]=char_item
            #     obj=(item,char_item,rand_x,rand_y)
            #     list_item.append(obj)
            # print(list_item)
        char={}
        char['ether']='e'
        char['needle']='n'
        char['tube']='t'
        global list_item
        list_item=[]
        
        for i in char.values():
            rand_x=randint(1,13)
            rand_y=randint(1,13)
            if self.structure[rand_x][rand_y]=='0':
                self.structure[rand_x][rand_y]=i
            else:
                rand_x=randint(1,13)
                rand_y=randint(1,13)
                if self.structure[rand_x][rand_y]=='0':
                    self.structure[rand_x][rand_y]=i

                
        

        # self.structure[randint(1,13)][randint(1,13)]="e"
        # self.structure[randint(1,13)][randint(1,13)]="n"
        # self.structure[randint(1,13)][randint(1,13)]="t"
        # global list_object
        # list_object=[]
        # # print(self.structure)

        # for y,lst in enumerate(self.structure):
        #     for x,abs_m in enumerate(lst):
        #         if abs_m == "e":
        #             # print("the ether is in ",y,"list at the", x,"position")
        #             list_ether=[]
        #             list_ether.append(x)
        #             list_ether.append(y)
        #             list_object.append(list_ether)
        # for y,lst in enumerate(self.structure):
        #     for x,abs_m in enumerate(lst):
        #         if abs_m == "n":
        #             # print("the needle is in ",y,"list at the", x,"position")
        #             list_needle=[]
        #             list_needle.append(x)
        #             list_needle.append(y)
        #             list_object.append(list_needle)
        # for y,lst in enumerate(self.structure):
        #     for x,abs_m in enumerate(lst):
        #         if abs_m == "t":
        #             # print("the tube is in ",y,"list at the", x,"position")
        #             list_tube=[]
        #             list_tube.append(x)
        #             list_tube.append(y)
        #             list_object.append(list_tube)
        # if list_tube == list_needle or list_tube== list_ether:
        #     self.structure[randint(1,14)][randint(1,14)]="t"
        # elif list_needle == list_ether :
        #     self.structure[randint(1,14)][randint(1,14)]="n"
        # elif list_needle or list_ether or list_tube =="t":
        #     pass
        # else:
        #     print("les 3 objets sont placés à des endroits différents")
        #     # indexes = [(i, j) for i, nl in enumerate(self.structure) for j, nle in enumerate(nl)]
        #     # print(*indexes, sep="\n")
        #     # fichier.close()
        # print(list_object)
        

class Score():
    def __init__(self):
        self.score= 0

   # def replace_value(self,list_macgyver):
    # def scoring(self):
    #     return score
    def win(self):
        print("you win")
        screen = pygame.image.load("MacGyver/ressources/win.png")

    def lose(self):
        print("you lose")
        screen = pygame.image.load("MacGyver/ressources/lose.jpg")
        

class Perso(Score):
    def __init__(self,pos_x,pos_y,structure_lab):
        self.position_perso = (pos_x,pos_y)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.labyrinth = structure_lab 
        self.score = 0

    def deplacer(self,direction):
        x=list_macgyver[0]
        y=list_macgyver[1]
        # case_x=0
        # case_y=0
        print(list_macgyver)
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
        
            
            
            
        


            
        # print(x,y)
        # print(self.labyrinth)
        pygame.display.flip()

set_the_score=Score()
# score=set_the_score.scoring
game=labyrinth('labyrinth.txt')
game.generate()
game.set_the_object()
mac_x,mac_y=game.find_player()
macgyver_perso = Perso(mac_x,mac_y,game.structure)

# while True:
#     direction = input("chose direction : ") 
#     deplacement=perso()
#     deplacement.deplacer(direction)
#     deplacement.scoring(list_macgyver,list_object)




    # with open('MacGyver/labyrinth.txt') as fichier:

# 	def afficher(screen):
# 			wall = pygame.image.load(image_wall).convert()
# 			macgyver = pygame.image.load(image_macgyver).convert()
# 			needle= pygame.image.load(image_needle).convert()
# 			ether= pygame.image.load(image_ether).convert()
# 			tube= pygame.image.load(image_tube).convert()
# 			badguy= pygame.image.load(image_guard).convert()

# 			for y,lst in enumerate(fichier):
# 				for x,abs_m in enumerate(lst):
# 					position_x= lst*taille_sprite
# 					position_y= abs_m*taille_sprite
# 					if abs_m == "*":
# 						screen.blint(wall,(position_x,position_y))
# 					elif abs_m == "m":
# 						screen.blint(macgyver,(position_x,position_y))
# 					elif abs_m == "b":
# 						screen.blint(badguy,(position_x,position_y))
# 					elif abs_m == "n":
# 						screen.blint(needle,(position_x,position_y))
# 					elif abs_m == "t":
# 						screen.blint(tube,(position_x,position_y))
# 					elif abs_m == "e":
# 						screen.blint(ether,(position_x,position_y))
#                   elif abs_m == "0":
# 						screen.blint(floor,(position_x,position_y))	

#BOUCLE INFINIE