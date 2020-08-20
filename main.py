import pygame, sys
from make_board import *
pygame.init()


def quit_game():
	pygame.quit()
	sys.exit(0)

def reset_game():
	# Reset Here
	pass

def run_game():
	window 	= pygame.display.set_mode((total_width, total_height))
	pygame.display.set_caption("Ultimate Tic-Tac-Toe")
	refresh_window(window, current_player, x_score, o_score)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit_game()

		b_height 	= sidebar_width // 2
		b_width 	= sidebar_width // 3
		b_x			= board
		b_y 		= total_height - sidebar_width // 3
		button(window, "Reset", b_x, b_y, b_height, b_width, yellow, light_yellow, reset_game)
		button(window, "Quit", b_x + sidebar_width // 2, b_y, b_height, b_width, red, light_red, quit_game)

		pygame.display.update()

if __name__ == "__main__":
	run_game()