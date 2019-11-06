import pygame
from random import randint
from constantes import *
from score import *
from maze_charging import *
from perso import *
""" V1.0--Main file who will be imported other file and run them"""

set_the_score = Score()
game = Labyrinth('labyrinth.txt')
game.generate()
game.set_the_object()
mac_x, mac_y, list_macgyver = game.find_player()
macgyver_perso = Perso(mac_x, mac_y, game.structure, list_macgyver)

