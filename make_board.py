import pygame
pygame.font.init()


# Colors
white  = ( 255, 255, 255)
green  = ( 115, 166,  87)

# Board/space dimensions
total_board_height	= 720
total_board_width	= 900
board				= total_board_height

# Setting initial sidebar information
current_player 		= "X"
x_score				= 0
o_score				= 0

""" 
Setting board elements' dimensions based on board size
2 * global_margin + 8 * local_margin + 9 * space = board size
"""
global_margin	= board / 24
local_margin	= board / 48
space			= board / 12

def update_sidebar(current_player, x_score, o_score):


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



