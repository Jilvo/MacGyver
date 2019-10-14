#V0.4
#Import the labyrinth's file
balise_player=0
balise_bad_guy=0

from random import randint
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
        with open('macgyver/labyrinth.txt') as fichier:
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
                    #print("present")

                line = fichier.readline()
                cnt += 1
                
            print(structure_labyrinth)
            fichier.close()
    def find_player(self):
#find MacGyver    
        for y,lst in enumerate(structure_labyrinth):
            for x,color in enumerate(lst):
                if color == "m":
                    # print("MacGyver is in ",y,"list at the", x,"position")
                    global list_macgyver
                    list_macgyver=[]
                    list_macgyver.append(x)
                    list_macgyver.append(y)
        
#find the bad guy
        for y,lst in enumerate(structure_labyrinth):
            for x,color in enumerate(lst):
                if color == "b":
                    #  print("The bad guy is in ",y,"list at the", x,"position")
                    global list_badguy
                    list_badguy=[]
                    list_badguy.append(x)
                    list_badguy.append(y)
                    pass
                    

    def set_the_object(self):
        structure_labyrinth[randint(1,13)][randint(1,13)]="e"
        structure_labyrinth[randint(1,13)][randint(1,13)]="n"
        structure_labyrinth[randint(1,13)][randint(1,13)]="t"
        global list_object
        list_object=[]
        # print(structure_labyrinth)

        for y,lst in enumerate(structure_labyrinth):
            for x,color in enumerate(lst):
                if color == "e":
                    # print("the ether is in ",y,"list at the", x,"position")
                    list_ether=[]
                    list_ether.append(x)
                    list_ether.append(y)
                    list_object.append(list_ether)
        for y,lst in enumerate(structure_labyrinth):
            for x,color in enumerate(lst):
                if color == "n":
                    # print("the needle is in ",y,"list at the", x,"position")
                    list_needle=[]
                    list_needle.append(x)
                    list_needle.append(y)
                    list_object.append(list_needle)
        for y,lst in enumerate(structure_labyrinth):
            for x,color in enumerate(lst):
                if color == "t":
                    # print("the tube is in ",y,"list at the", x,"position")
                    list_tube=[]
                    list_tube.append(x)
                    list_tube.append(y)
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
        print(list_object)
        

class perso():

    def deplacer(self,direction):
        x=list_macgyver[0]
        y=list_macgyver[1]
        # case_x=0
        # case_y=0
        print(list_macgyver)
        if direction == 'right':
            if structure_labyrinth[x+1][y]!='*':
                structure_labyrinth[y][x]="0"
                list_macgyver[0] += 1
                x+=1
                structure_labyrinth[y][x]="m"
                print("right")
        if direction == 'left':
            if structure_labyrinth[x-1][y]!='*':
                structure_labyrinth[y][x]="0"
                list_macgyver[0] -= 1
                x-=1
                print(x)
                structure_labyrinth[y][x]="m"
                print("left")
        if direction == 'up':
            if structure_labyrinth[x][y-1]!='*':
                structure_labyrinth[y][x]="0"
                list_macgyver[1] -= 1
                y-=1
                structure_labyrinth[y][x]="m"
                print("up")
        if direction == 'down':
            if structure_labyrinth[x][y+1]!='*':
                structure_labyrinth[y][x]="0"
                list_macgyver[1] += 1
                y+=1
                structure_labyrinth[y][x]="m"
                print("down")

            
        print(x,y)
        print(structure_labyrinth)
        
    
   # def replace_value(self,list_macgyver):
    def scoring(self,list_macgyver,list_object):
        score=0
        print(list_macgyver)
        #print(list_object)
        if list_macgyver == list_object[0]:
            score+=1
            print("Le score est passé a : ",score,"grace au ether")
            
        if list_macgyver == list_object[1]:
            score+=2
            print("Le score est passé a : ",score,"grace au needle")
        if list_macgyver == list_object[2]:
            score+=3
            print("Le score est passé a : ",score,"grace au tube")
    


game=labyrinth('labyrinth.txt')
game.generate()
game.set_the_object()
game.find_player()

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
# 				for x,color in enumerate(lst):
# 					position_x= lst*taille_sprite
# 					position_y= color*taille_sprite
# 					if color == "*":
# 						screen.blint(wall,(position_x,position_y))
# 					elif color == "m":
# 						screen.blint(macgyver,(position_x,position_y))
# 					elif color == "b":
# 						screen.blint(badguy,(position_x,position_y))
# 					elif color == "n":
# 						screen.blint(needle,(position_x,position_y))
# 					elif color == "t":
# 						screen.blint(tube,(position_x,position_y))
# 					elif color == "e":
# 						screen.blint(ether,(position_x,position_y))
#                   elif color == "0":
# 						screen.blint(floor,(position_x,position_y))	

#BOUCLE INFINIE