"""
Runs functions related to Tic Tac Toe game.

OUTPUT: Ultimate Tic Tac Toe Game!
"""
from uttt_function import *
from display import display_board
from tutorial import uttt_tutorial 


def UTTT():
	# Asking if the player would like a tutorial
	uttt_tutorial()

	# Game Begins
	while True:
	    current_board = {
	        "A": [" ", " ", " ", " ", " ", " ", " ", " ", " "],
	        "B": [" ", " ", " ", " ", " ", " ", " ", " ", " "],
	        "C": [" ", " ", " ", " ", " ", " ", " ", " ", " "],
	        "D": [" ", " ", " ", " ", " ", " ", " ", " ", " "],
	        "E": [" ", " ", " ", " ", " ", " ", " ", " ", " "],
	        "F": [" ", " ", " ", " ", " ", " ", " ", " ", " "],
	        "G": [" ", " ", " ", " ", " ", " ", " ", " ", " "],
	        "H": [" ", " ", " ", " ", " ", " ", " ", " ", " "],
	        "I": [" ", " ", " ", " ", " ", " ", " ", " ", " "]
	    }
	    outcome_decided = {
	        "A": [False, " "],
	        "B": [False, " "],
	        "C": [False, " "],
	        "D": [False, " "],
	        "E": [False, " "],
	        "F": [False, " "],
	        "G": [False, " "],
	        "H": [False, " "],
	        "I": [False, " "]
	    }
	    chosen_spot = "  "

	    print("Let's begin playing!")
	    first_move = choose_first()
	    player_turn = choose_mark(first_move)

	    while True:
	        # X's Turn
	        display_board(current_board)
	        print("\nPlayer", player_turn[0], "is up!")
	        chosen_spot = choose_spot(chosen_spot, current_board, outcome_decided)
	        current_board = place_marker(current_board, chosen_spot, "X")

	        outcome_decided = local_outcome_check(chosen_spot, current_board, "X", outcome_decided)
	        if outcome_decided[chosen_spot[0]][1] == "X":
	            print("Player", player_turn[0], "has won local game", chosen_spot[0], "!\n")
	        if global_outcome_check(outcome_decided, "X"):
	            display_board(current_board)
	            print("~~~~~Player", player_turn[0], "has won the game!~~~~~\n")
	            break

	        # O's Turn
	        display_board(current_board)
	        print("\nPlayer", player_turn[1], "is up!")
	        chosen_spot = choose_spot(chosen_spot, current_board, outcome_decided)
	        current_board = place_marker(current_board, chosen_spot, "O")

	        outcome_decided = local_outcome_check(chosen_spot, current_board, "O", outcome_decided)
	        if outcome_decided[chosen_spot[0]][1] == "O":
	            print("Player", player_turn[1], "has won local game", chosen_spot[0], "!\n")
	        if global_outcome_check(outcome_decided, "X"):
	            display_board(current_board)
	            print("~~~~~Player", player_turn[1], "has won the game!~~~~~\n")
	            break

	    if not replay():
	        break

if __name__ = "__main__":
	UTTT()