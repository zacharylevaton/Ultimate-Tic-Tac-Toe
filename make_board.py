import pygame
pygame.font.init()


# Colors
white  = ( 255, 255, 255)
green  = ( 115, 166,  87)

# Board/space dimensions
total_height	= 720
total_width		= 900
board			= total_height
sidebar_width 	= total_width - board

# Setting initial sidebar information
current_player 	= "X"
x_score			= 0
o_score			= 0

# Initializing font-related info
title_font = pygame.font.SysFont('arial', 22)
content_font = pygame.font.SysFont('arial', 30)

""" 
Setting board elements' dimensions based on board size
2 * global_margin + 8 * local_margin + 9 * space = board size
"""
global_margin	= board / 24
local_margin	= board / 48
space			= board / 12

def refresh_window(window, current_player, x_score, o_score):
	make_board(window)
	update_sidebar(window, current_player, x_score, o_score)

def make_board(window):
	pygame.draw.rect(window, green, (0,0,board,board))
	x = local_margin
	y = local_margin
	for row in range(1,10):
		if row  == 4 or row == 7:
			y += global_margin + space
		elif row != 1:
			y += local_margin+ space

		for column in range(1,10):
			if column  == 4 or column == 7:
				x += global_margin + space
			elif column != 1:
				x += local_margin+ space

			pygame.draw.rect(window, white, (x,y,space,space))

			if column == 9:
				x = local_margin

def update_sidebar(window, current_player, x_score, o_score):
	#pygame.draw.rect(window, white, (board, 0, sidebar_width, total_height))

	current_player_title = title_font.render('Current Player:', True, white) 
	x_score_title		= title_font.render('X Score:', True, white) 
	o_score_title = title_font.render('O Score:', True, white) 

	current_player_title_rect = current_player_title.get_rect()  
	x_score_title_rect = x_score_title.get_rect()
	o_score_title_rect = o_score_title.get_rect()

	current_player_title_rect.center = (total_width - (0.5 * sidebar_width), local_margin + 0.5 * space)
	x_score_title_rect.center = (total_width - (0.5 * sidebar_width), 3 * local_margin + 0.5 * global_margin + 3 * space)
	o_score_title_rect.center = (total_width - (0.5 * sidebar_width), 5 * local_margin + 1.5 * global_margin + 6 * space)

	window.blit(current_player_title, current_player_title_rect)
	window.blit(x_score_title, x_score_title_rect)
	window.blit(o_score_title, o_score_title_rect)









