import pygame 
from make_board import *
pygame.init()


window 	= pygame.display.set_mode((board,board))
pygame.display.set_caption("Ultimate Tic-Tac-Toe")

make_board(window)

while True:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit(0)

	pygame.display.update()