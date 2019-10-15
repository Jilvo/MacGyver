#V 0.5 pygame
#import modules
import pygame
from pygame.locals import *
from constantes import *
from main import *
#init
pygame.init()
screen = pygame.display.set_mode((cote_screen, cote_screen))


# fond = pygame.image.load("MacGyver/ressources/background.jpg").convert()
#set the objects and stuff
ether= pygame.image.load(image_ether).convert_alpha()
tube= pygame.image.load(image_tube).convert_alpha()
needle= pygame.image.load(image_needle).convert_alpha()
wall = pygame.image.load(image_wall).convert_alpha()
macgyver = pygame.image.load(image_macgyver).convert_alpha()
badguy = pygame.image.load(image_badguy).convert_alpha()

x=list_badguy[0]*taille_sprite
y=list_badguy[1]*taille_sprite
# wall= pygame.image.load(image_wall).convert_alpha

for y,lst in enumerate(structure_labyrinth):
	for x,color in enumerate(lst):
		if color =="*":
			a=x*taille_sprite
			b=y*taille_sprite
			screen.blit(wall,(a,b))
		if color =="b":
			a=x*taille_sprite
			b=y*taille_sprite
			screen.blit(badguy,(a,b))
		if color =="m":
			a=x*taille_sprite
			b=y*taille_sprite
			position_perso = macgyver.get_rect()
			position_perso.center=a,b
			screen.blit(macgyver, position_perso)
			# screen.blit(macgyver,(a,b))
			pygame.display.flip()
		if color =="n":
			a=x*taille_sprite
			b=y*taille_sprite
			screen.blit(needle,(a,b))
		if color =="t":
			a=x*taille_sprite
			b=y*taille_sprite
			screen.blit(tube,(a,b))
		if color =="e":
			a=x*taille_sprite
			b=y*taille_sprite
			screen.blit(ether,(a,b))
		pygame.display.flip()

		

#set the object

#Chargement et collage du personnage


# def score_board(score,ether,needle,tube)
# 	if score==0

# 	if 

continuer = 1
while continuer:
	for event in pygame.event.get():	#Attente des événements
		if event.type == QUIT:
			continuer = 0
		if event.type == KEYDOWN:
			if event.key == K_DOWN:	#Si "flèche bas"
				#On descend le perso
				deplacement.deplacer('down')
				position_perso = position_perso.move(0,taille_sprite)
				pygame.display.flip()
		if event.type == KEYDOWN:
			if event.key == K_UP:	#Si "flèche bas"
				#On descend le perso
				deplacement.deplacer('up')
				position_perso = position_perso.move(0,-taille_sprite)
				pygame.display.flip()
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:	#Si "flèche bas"
				#On descend le perso
				deplacement.deplacer('right')
				position_perso = position_perso.move(taille_sprite,0)
				pygame.display.flip()
		if event.type == KEYDOWN:
			if event.key == K_LEFT:	#Si "flèche bas"
				#On descend le perso
				deplacement.deplacer('left')
				position_perso = position_perso.move(-taille_sprite,0)
				pygame.display.flip()
		pygame.display.flip()
	screen.blit(macgyver, position_perso)
	# screen.blit(macgyver, position_perso)
	pygame.display.flip()
