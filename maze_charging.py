from random import randint
class labyrinth():
#create a class for the labyrinth  
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = []
        self.list_macgyver=[]
	
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
                    mac_x=x
                    mac_y=y
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