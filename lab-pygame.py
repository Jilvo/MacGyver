#V 0.8 pygame
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
macgyver_img = pygame.image.load(image_macgyver).convert_alpha()
badguy = pygame.image.load(image_badguy).convert_alpha()
floor = pygame.image.load(image_floor).convert_alpha()
win_img = pygame.image.load(image_win).convert_alpha
lose_img = pygame.image.load(image_lose).convert_alpha

# wall= pygame.image.load(image_wall).convert_alpha
def display(structure_labyrinth):
	
	for y,lst in enumerate(structure_labyrinth):
		for x,abs_m in enumerate(lst):
			if abs_m =="*":
				pos_x=x*taille_sprite
				pos_y=y*taille_sprite
				screen.blit(wall,(pos_x,pos_y))
			if abs_m =="0":
				pos_x=x*taille_sprite
				pos_y=y*taille_sprite
				screen.blit(floor,(pos_x,pos_y))
			if abs_m =="b":
				pos_x=x*taille_sprite
				pos_y=y*taille_sprite
				screen.blit(floor,(pos_x,pos_y))
				screen.blit(badguy,(pos_x,pos_y))
			if abs_m =="m":
				pos_x=x*taille_sprite
				pos_y=y*taille_sprite
				screen.blit(floor,(pos_x,pos_y))
				position_perso = macgyver_img.get_rect()
				position_perso=pos_x,pos_y
				# screen.blit(macgyver_img, position_perso)
				screen.blit(macgyver_img,(pos_x,pos_y))
				pygame.display.flip()
			if abs_m =="n":
				pos_x=x*taille_sprite
				pos_y=y*taille_sprite
				screen.blit(floor,(pos_x,pos_y))
				screen.blit(needle,(pos_x,pos_y))
			if abs_m =="t":
				pos_x=x*taille_sprite
				pos_y=y*taille_sprite
				screen.blit(floor,(pos_x,pos_y))
				screen.blit(tube,(pos_x,pos_y))
			if abs_m =="e":
				pos_x=x*taille_sprite
				pos_y=y*taille_sprite
				screen.blit(floor,(pos_x,pos_y))
				screen.blit(ether,(pos_x,pos_y))
			pygame.display.flip()

		

#set the object

#Chargement et collage du personnage

#set the scoreboard:
def score_board():
	myfont = pygame.font.SysFont("comicsansms", 30)
	text="Le score actuel est : " + str(macgyver_perso.score)
	score_display = myfont.render(text, 1, (255, 163, 172))
	screen.blit(score_display, (0,0))

# def score_board(score,ether,needle,tube)
# 	if score==0

# 	if 

continuer = 1
display(game.structure)
while continuer:
	# if score_img==True:
	# 	screen.blit(win_img,(0,0))
	# elif score_img==False:
	# 	screen.blit(lose_img,(0,0))
	for event in pygame.event.get():	#Attente des événements	
		if event.type == QUIT:
			continuer = 0
		if event.type == KEYDOWN:
			if event.key == K_DOWN:	#if "down arrow"
				old_position=(macgyver_perso.pos_x*taille_sprite,macgyver_perso.pos_y*taille_sprite)
				macgyver_perso.deplacer('down')
				screen.blit(floor,old_position)
				position_perso= (macgyver_perso.pos_x*taille_sprite,macgyver_perso.pos_y*taille_sprite)
				screen.blit(macgyver_img, position_perso)
				pygame.display.flip()
				score_board()	
		if event.type == KEYDOWN:
			if event.key == K_UP:	#if "up arrow"
				old_position=(macgyver_perso.pos_x*taille_sprite,macgyver_perso.pos_y*taille_sprite)
				macgyver_perso.deplacer('up')
				screen.blit(floor,old_position)
				position_perso= (macgyver_perso.pos_x*taille_sprite,macgyver_perso.pos_y*taille_sprite)
				screen.blit(macgyver_img, position_perso)
				pygame.display.flip()
				score_board()
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:	#if "right arrow"
				old_position=(macgyver_perso.pos_x*taille_sprite,macgyver_perso.pos_y*taille_sprite)
				macgyver_perso.deplacer('right')
				screen.blit(floor,old_position)
				position_perso= (macgyver_perso.pos_x*taille_sprite,macgyver_perso.pos_y*taille_sprite)
				screen.blit(macgyver_img, position_perso)
				pygame.display.flip()
				score_board()
		if event.type == KEYDOWN:
			if event.key == K_LEFT:	#if "left arrow"
				old_position=(macgyver_perso.pos_x*taille_sprite,macgyver_perso.pos_y*taille_sprite)
				macgyver_perso.deplacer('left')
				screen.blit(floor,old_position)
				position_perso= (macgyver_perso.pos_x*taille_sprite,macgyver_perso.pos_y*taille_sprite)
				screen.blit(macgyver_img, position_perso)
				pygame.display.flip()
				score_board()
		pygame.display.flip()
		
	# print(pos_x,pos_y)
	# screen.blit(macgyver_img, position_perso)
	pygame.display.flip()
