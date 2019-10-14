#V 0.1 pygame
#import modules
import pygame
from pygame.locals import *
from constantes import *
from main import *
#init
pygame.init()
screen = pygame.display.set_mode((cote_screen, cote_screen))

#Chargement et collage du fond
fond = pygame.image.load("MacGyver/ressources/background.jpg").convert()

#set the guard
badguy = pygame.image.load(image_badguy).convert_alpha()
x=list_badguy[0]*taille_sprite
y=list_badguy[1]*taille_sprite
#set the wall
# wall= pygame.image.load(image_wall).convert_alpha

# for y,lst in enumerate(structure_labyrinth):
# 	for x,color in enumerate(lst):
# 		if color =="*":
# 			x=color*taille_sprite
# 			y=lst*taille_sprite
# 			screen.blint(wall,(x,y))
# 	pygame.display.flip()

#set the object
ether= pygame.image.load(image_ether).convert_alpha()
tube= pygame.image.load(image_tube).convert_alpha()
needle= pygame.image.load(image_needle).convert_alpha()
wall = pygame.image.load(image_wall).convert_alpha()
#Chargement et collage du personnage
perso = pygame.image.load("MacGyver/ressources/macgyver.png").convert_alpha()
position_perso = perso.get_rect()

screen.blit(perso, position_perso)
Score=1
#Rafraîchissement de l'écran
# def display_labyrinth(structure_labyrinth):
#     for y,lst in enumerate(structure_labyrinth):
#         for x,color in enumerate(lst):
#             if color == "*":
# 			    screen.blit(wall,(structure_labyrinth[i]*taille_sprite,structure_labyrinth[i][j]*taille_sprite))
# 		    else:
# 		        pass	


continuer = 1
while continuer:
	for event in pygame.event.get():	#Attente des événements
		if event.type == QUIT:
			continuer = 0
		if event.type == KEYDOWN:
			if event.key == K_DOWN:	#Si "flèche bas"
				#On descend le perso
				position_perso = position_perso.move(0,taille_sprite)
		if event.type == KEYDOWN:
			if event.key == K_UP:	#Si "flèche bas"
				#On descend le perso
				position_perso = position_perso.move(0,-taille_sprite)
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:	#Si "flèche bas"
				#On descend le perso
				position_perso = position_perso.move(taille_sprite,0)
		if event.type == KEYDOWN:
			if event.key == K_LEFT:	#Si "flèche bas"
				#On descend le perso
				position_perso = position_perso.move(-taille_sprite,0)
		
	
	#Re-collage
	screen.blit(fond, (0,0))	
	screen.blit(badguy,(x,y))
	screen.blit(perso, position_perso)
	screen.blit(ether, (list_object[0][0]*taille_sprite,list_object[0][1]*taille_sprite))
	screen.blit(needle, (list_object[1][0]*taille_sprite,list_object[1][1]*taille_sprite))
	screen.blit(tube, (list_object[2][0]*taille_sprite,list_object[2][1]*taille_sprite))
	
	#Rafraichissement
	pygame.display.flip()
