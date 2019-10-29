#V0.1
#Import the labyrinth's file
import pygame
from random import randint
from constantes import *
from score import *
from maze_charging import *
from perso import *

set_the_score=Score()
# score=set_the_score.scoring
game=labyrinth('labyrinth.txt')
game.generate()
game.set_the_object()
mac_x,mac_y,list_macgyver=game.find_player()
macgyver_perso = Perso(mac_x,mac_y,game.structure,list_macgyver)

