import pygame
pygame.font.init()


# Colors
black 			= (   0,   0,   0)
white  			= ( 255, 255, 255)
paper_yellow	= ( 242, 238, 203)
red 			= ( 207,  20,  43)
light_red		= ( 181,  20,  43)
yellow 			= ( 250, 210,   1)
light_yellow	= ( 225, 210,   1)
gray  			= ( 154, 162, 151)

# Board/space dimensions
total_height	= 720
total_width		= int(total_height * 1.25)
board			= total_height
sidebar_width 	= total_width - board

# Setting initial sidebar information
current_player 	= "X"
x_score			= 0
o_score			= 0

# Initializing font-related info
button_size 	= total_height // 50
title_size 		= total_height // 30
content_size 	= title_size * 2
button_font		= pygame.font.SysFont('arial', button_size)
title_font 		= pygame.font.SysFont('arial', title_size)
content_font 	= pygame.font.SysFont('arial', content_size)

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
	pygame.draw.rect(window, paper_yellow, (0,0,board,board))
	x = local_margin
	y = local_margin
	for row in range(1,10):
		if row  in [4, 7]:
			y += global_margin + space
		elif row != 1:
			y += local_margin+ space

		for column in range(1,10):
			if column  in [4, 7]:
				x += global_margin + space
			elif column != 1:
				x += local_margin+ space

			if row in [1, 4, 7] and column in [1, 4, 7]:
				pygame.draw.rect(window, black, (x,y,3*space + 2*local_margin,3*space + 2*local_margin))

			pygame.draw.rect(window, paper_yellow, (x,y,space,space))

			if column == 9:
				x = local_margin

	# Global board's lines.
	# Left Vertical.
	pygame.draw.rect(window, black, (3.5 * local_margin + 3 * space, 0, global_margin / 2, total_height))
	# Right Vertical.
	pygame.draw.rect(window, black, (5.5 * local_margin + 6 * space + global_margin, 0, global_margin / 2, total_height))
	# Top Horizontal.
	pygame.draw.rect(window, black, (0, 3.5 * local_margin + 3 * space, total_height, global_margin / 2))
	# Bottom Horizontal.
	pygame.draw.rect(window, black, (0, 5.5 * local_margin + 6 * space + global_margin, total_height, global_margin / 2))


	# Creating text for current player title block.
	current_player_title = title_font.render('Current Player:', True, white) 
	current_player_title_rect = current_player_title.get_rect()  
	current_player_title_rect.center = (total_width - (0.5 * sidebar_width), local_margin + 0.5 * space)

	# Creating text for x score title block.
	x_score_title		= title_font.render('X Wins:', True, white) 
	x_score_title_rect = x_score_title.get_rect()
	x_score_title_rect.center = (total_width - (0.5 * sidebar_width), 3 * local_margin + 1 * global_margin + 3.5 * space)

	# Creating text for o score title block.
	o_score_title = title_font.render('O Wins:', True, white) 
	o_score_title_rect = o_score_title.get_rect()
	o_score_title_rect.center = (total_width - (0.5 * sidebar_width), 5 * local_margin + 2 * global_margin + 6.5 * space)

	# Blitting titles to screen.
	window.blit(current_player_title, current_player_title_rect)
	window.blit(x_score_title, x_score_title_rect)
	window.blit(o_score_title, o_score_title_rect)


def update_sidebar(window, current_player, x_score, o_score):
	# Updating text content for current player.
	current_player_content 				= content_font.render(current_player, True, white) 
	current_player_content_rect 		= current_player_content.get_rect()  
	current_player_content_rect.center 	= (total_width - (0.5 * sidebar_width), 2 * local_margin + 1.5 * space)

	# Updating text content for x score.
	x_score_content						= content_font.render(str(x_score), True, white) 
	x_score_content_rect 				= x_score_content.get_rect()
	x_score_content_rect.center 		= (total_width - (0.5 * sidebar_width), 4 * local_margin + 1 * global_margin + 4.5 * space)

	# Updating text content for o score.
	o_score_content						= content_font.render(str(o_score), True, white) 
	o_score_content_rect 				= o_score_content.get_rect()
	o_score_content_rect.center 		= (total_width - (0.5 * sidebar_width), 6 * local_margin + 2 * global_margin + 7.5 * space)

	# Blitting content to screen.
	window.blit(current_player_content, current_player_content_rect)
	window.blit(x_score_content, x_score_content_rect)
	window.blit(o_score_content, o_score_content_rect)


def button(window, text, x, y, w, h, color, hover_color, action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	if x+w > mouse[0] > x and y+h > mouse[1] > y:
	    pygame.draw.rect(window, hover_color,(x,y,w,h))

	    if click[0] == 1 and action != None:
	        action()         
	else:
	    pygame.draw.rect(window, color,(x,y,w,h))

	button = button_font.render(text, True, gray) 
	button_rect = button.get_rect()
	button_rect.center = ( (x+(w/2)), (y+(h/2)) )
	window.blit(button, button_rect)








