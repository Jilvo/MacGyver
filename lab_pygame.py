"""import modules"""
import pygame
from pygame.locals import *
from constantes import *
from main import *
"""V1.1--This Module is in charge of creating a visible
version for the player with graphism ,HUD... """
#init
pygame.init()
screen = pygame.display.set_mode((COTE_SCREEN, COTE_SCREEN))

#set the objects and stuff

ether = pygame.image.load(IMAGE_ETHER).convert_alpha()
tube = pygame.image.load(IMAGE_TUBE).convert_alpha()
needle = pygame.image.load(IMAGE_NEEDLE).convert_alpha()
wall = pygame.image.load(IMAGE_WALL).convert_alpha()
macgyver_img = pygame.image.load(IMAGE_MACGYVER).convert_alpha()
badguy = pygame.image.load(IMAGE_BADGUY).convert_alpha()
floor = pygame.image.load(IMAGE_FLOOR).convert_alpha()
win_img = pygame.image.load(IMAGE_WIN).convert_alpha()
lose_img = pygame.image.load(IMAGE_LOSE).convert_alpha()
image_icon_img = pygame.image.load(IMAGE_ICON).convert_alpha()
pygame.display.set_icon(image_icon_img)
pygame.display.set_caption(TITLE_SCREEN)

def display(structure_labyrinth):
	for y, lst in enumerate(structure_labyrinth):
		for x, abs_m in enumerate(lst):
			if abs_m == "*":
				pos_x = x*SIZE_SPRITE
				pos_y = y*SIZE_SPRITE
				screen.blit(wall, (pos_x, pos_y))
			if abs_m == "0":
				pos_x = x*SIZE_SPRITE
				pos_y = y*SIZE_SPRITE
				screen.blit(floor, (pos_x, pos_y))
			if abs_m == "b":
				pos_x = x*SIZE_SPRITE
				pos_y = y*SIZE_SPRITE
				screen.blit(floor, (pos_x, pos_y))
				screen.blit(badguy, (pos_x, pos_y))
			if abs_m == "m":
				pos_x = x*SIZE_SPRITE
				pos_y = y*SIZE_SPRITE
				screen.blit(floor, (pos_x, pos_y))
				position_perso = macgyver_img.get_rect()
				position_perso = pos_x, pos_y
				screen.blit(macgyver_img, (pos_x, pos_y))
				pygame.display.flip()
			if abs_m == "n":
				pos_x = x*SIZE_SPRITE
				pos_y = y*SIZE_SPRITE
				screen.blit(floor, (pos_x, pos_y))
				screen.blit(needle, (pos_x, pos_y))
			if abs_m == "t":
				pos_x = x*SIZE_SPRITE
				pos_y = y*SIZE_SPRITE
				screen.blit(floor, (pos_x, pos_y))
				screen.blit(tube, (pos_x, pos_y))
			if abs_m == "e":
				pos_x = x*SIZE_SPRITE
				pos_y = y*SIZE_SPRITE
				screen.blit(floor, (pos_x, pos_y))
				screen.blit(ether, (pos_x, pos_y))
			pygame.display.flip()

#set the scoreboard:
def score_board():
	myfont = pygame.font.SysFont("comicsansms", 30)
	text = "Le score actuel est : " + str(macgyver_perso.score.value)
	score_display = myfont.render(text, 1, (255, 163, 172))
	screen.blit(wall, (280, 0))
	screen.blit(score_display, (0, 0))
	pygame.display.flip()

follow_the_game = 1
display(game.structure)
score_board()
while follow_the_game:
	for event in pygame.event.get():
		if event.type == QUIT:
			follow_the_game = 0
		if event.type == KEYDOWN:
			if event.key == K_DOWN:
				old_position = (macgyver_perso.pos_x*SIZE_SPRITE, macgyver_perso.pos_y*SIZE_SPRITE)
				as_picked_an_item = macgyver_perso.move_macgyver('down')
				screen.blit(floor, old_position)
				position_perso = (macgyver_perso.pos_x*SIZE_SPRITE, macgyver_perso.pos_y*SIZE_SPRITE)
				screen.blit(macgyver_img, position_perso)
				pygame.display.flip()
				if as_picked_an_item: 
					score_board()
		if event.type == KEYDOWN:
			if event.key == K_UP:
				old_position = (macgyver_perso.pos_x*SIZE_SPRITE, macgyver_perso.pos_y*SIZE_SPRITE)
				as_picked_an_item = macgyver_perso.move_macgyver('up')
				screen.blit(floor, old_position)
				position_perso = (macgyver_perso.pos_x*SIZE_SPRITE, macgyver_perso.pos_y*SIZE_SPRITE)
				screen.blit(macgyver_img, position_perso)
				pygame.display.flip()
				if as_picked_an_item:
					score_board()
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				old_position = (macgyver_perso.pos_x*SIZE_SPRITE, macgyver_perso.pos_y*SIZE_SPRITE)
				as_picked_an_item = macgyver_perso.move_macgyver('right')
				screen.blit(floor, old_position)
				position_perso = (macgyver_perso.pos_x*SIZE_SPRITE, macgyver_perso.pos_y*SIZE_SPRITE)
				screen.blit(macgyver_img, position_perso)
				pygame.display.flip()
				if as_picked_an_item:
					score_board()
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				old_position = (macgyver_perso.pos_x*SIZE_SPRITE, macgyver_perso.pos_y*SIZE_SPRITE)
				as_picked_an_item = macgyver_perso.move_macgyver('left')
				screen.blit(floor, old_position)
				position_perso = (macgyver_perso.pos_x*SIZE_SPRITE, macgyver_perso.pos_y*SIZE_SPRITE)
				screen.blit(macgyver_img, position_perso)
				pygame.display.flip()
				if as_picked_an_item:
					score_board()
		pygame.display.flip()
		if macgyver_perso.score.is_finished and macgyver_perso.score.is_win:
			screen.blit(win_img, (0, 0))
		elif macgyver_perso.score.is_finished and not macgyver_perso.score.is_win:
			screen.blit(lose_img, (0, 0))
	pygame.display.flip()
