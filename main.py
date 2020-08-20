import pygame, sys
from make_board import *
pygame.init()


def reset_game():
	window 	= pygame.display.set_mode((total_width, total_height))
	pygame.display.set_caption("Ultimate Tic-Tac-Toe")
	refresh_window(window, current_player, x_score, o_score)
	run_game()


def quit_game():
	pygame.quit()
	sys.exit(0)


def run_game():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit_game()

		#button(window, "Reset", 150,450,100,50, white,black,)

		pygame.display.update()

if __name__ == "__main__":
	reset_game()