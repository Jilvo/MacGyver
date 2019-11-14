""" V1.1--Main file who will be imported other file and run them"""
from maze_charging import Labyrinth
from perso import Perso
from lab_pygame import run


game = Labyrinth('labyrinth.txt')
game.generate()
game.set_the_object()
MAC_X, MAC_Y, list_macgyver = game.find_player()
macgyver_perso = Perso(MAC_X, MAC_Y, game.structure, list_macgyver)
run(game, macgyver_perso)
