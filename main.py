import pygame 
from make_board import *
pygame.init()


window 	= pygame.display.set_mode((total_width, total_height))
pygame.display.set_caption("Ultimate Tic-Tac-Toe")

refresh_window(window, current_player, x_score, o_score)

while True:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit(0)

	pygame.display.update()