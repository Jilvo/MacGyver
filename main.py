#V0.1.2
#Import the labyrinth's file
balise_player=0
balise_bad_guy=0
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
            structure_labyrinth=[]
            structure_lign=[]
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

class perso():
    
    def init(self):
	    self.x=0
	    self.y=0

    def deplacer(self,direction,x,y):
        if direction == 'right':
            self.x += 1
            print("right")
            print(self.x,self.y)
        if direction == 'left':
            self.x -= 1
            print("left")
            print(self.x,self.y)
        if direction == 'up':
            self.y -= 1
            print("up")
            print(self.x,self.y)
        if direction == 'down':
            self.y += 1
            print("down")
            print(self.x,self.y)


game=labyrinth('labyrinth.txt')
game.generate()
direction = input("chose direction : ")
deplacement=perso()
deplacement.init()
deplacement.deplacer(direction)
