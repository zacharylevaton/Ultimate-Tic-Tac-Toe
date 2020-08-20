import random


def choose_first():
    """
    Uses the random module to pick if player 1 or 2 will go first.
    :return: Prints which player will choose their mark. Returns the associated player number.
    """
    first_move = random.randint(1,2)
    print("Player", first_move, "will begin by choosing their mark...")
    return first_move


def choose_mark(first_move):
    """
    Prompts user to choose X or O as their mark, and returns the resulting turn order.
    :param first_move: Player number deciding the mark.
    :return: List with turn order: 1 then 2, or 2 then 1.
    """
    player_turn = str(input("Please Choose X or O: ")).upper()

    while player_turn != "X" and player_turn != "O":
        player_turn = str(input("Your choice must be an X or an O\nPlease Choose X or O: ")).upper()

    if player_turn == "X":
        if first_move == 2:
            return [2,1]
        else:
            return [1,2]
    elif first_move == 1:
        return [2,1]
    else:
        return [1,2]

import random


def choose_spot(chosen_spot, current_board, outcome_decided):
    """
    This function prompts the user for a spot to place their mark. Checks spot's validity and correct placement.
    The function also calls other functions to check that the local game has not been decided. It returns the
    current players spot choice
    :param chosen_spot: The spot chosen by the previous player.
    :param current_board: Current board
    :param outcome_decided: Current state of local boards(Tie, Loss, Win)
    :return: Updated spot that current player has chosen.
    """
    global_map = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "F", "7": "G", "8": "H", "9": "I", }
    original_spot = chosen_spot

    while True:
        if (chosen_spot == "  ") or outcome_decided[global_map[chosen_spot[1]]][0]:
            chosen_spot = input("Please choose any spot on the board: ").upper()
        else:
            local_game = global_map[chosen_spot[1]]
            chosen_spot = input("Please choose an open spot in board " + local_game + ": ").upper()
            while not correct_local_game(local_game, chosen_spot) or not spot_is_valid(chosen_spot):
                if not spot_is_valid(chosen_spot):
                    chosen_spot = input("You must choose a valid spot: ").upper()
                else:
                    chosen_spot = input("Your choice must be in " + local_game + ": ").upper()

        if outcome_decided[chosen_spot[0]][0] == True:
            print("That game has already been decided.\n")
            chosen_spot = "  "
        elif spot_taken(chosen_spot, current_board):
            print("That spot is currently occupied.\n")
            chosen_spot = original_spot
        else:
            break

    return chosen_spot


def correct_local_game(local_game, updated_spot):
    """
    This function determines if the updated current player's spot is in the correct local game
    :param local_game: A-I, determined by previous player's spot
    :param chosen_spot: The current player's spot
    :return: True or False if current player's spot is in correct local game
    """
    if len(updated_spot) != 2:
        return False
    elif updated_spot == "  " or local_game != updated_spot[0]:
        return False
    else:
        return True


def global_outcome_check(outcome_decided, mark):
    """

    :param outcome_decided: Decided outcome of global games
    :param mark: X or O depending on current player
    :return: True or False is global game has been won
    """
    # All winning positions
    wins = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], ["A", "D", "G"], ["B", "E", "H"], ["C", "F", "H"], ["A", "E", "I"], ["C", "E", "G"]]

    for i in wins:
        # Global win check
        if outcome_decided[i[0]][1] == mark and outcome_decided[i[1]][1] == mark and outcome_decided[i[2]][1] == mark:
            return True
    return False



def local_outcome_check(chosen_spot, current_board, mark, outcome_decided):
    """
    This function decides if the current player's move results in a tie, win or nothing.
    :param chosen_spot: Current player's spot.
    :param current_board: Current board.
    :param mark: X or O depending on current player.
    :param outcome_decided: Dictionary tracking global game outcomes and assigned player
    :return: Current global game outcomes
    """
    # All winning positions
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    game = chosen_spot[0]

    # Local tie check
    if not " " in current_board[chosen_spot[0]]:
        outcome_decided[chosen_spot[0]] = [True, "T"]
        return outcome_decided

    # Local win check
    for i in wins:
        if current_board[game][i[0]] == mark and current_board[game][i[1]] == mark and current_board[game][i[2]] == mark:
            outcome_decided[chosen_spot[0]] = [True, mark]
            return outcome_decided

    else:
        return outcome_decided


def place_marker(current_board, chosen_spot, mark):
    """
    This function places the marker on the current board and return the updated board
    :param current_board: Current board
    :param chosen_spot: Spot chosen by current player
    :param mark: X or O depending on player
    :return: Updated board
    """
    # E5 and F5 do the same thing
    current_board[chosen_spot[0]][int(chosen_spot[1]) - 1] = mark
    return current_board


def replay():
    """
    Asks user if they would like to replay, Y or N
    :return: True or False if player would like to play again
    """
    x = str(input("Please type Y or N if you would like to play again: "))
    while x.upper() != "Y" and x.upper() != "N":
        x = str(input("You must type Y or N.\nPlease type Y or N if you would like to play again: "))
    if x.upper() == "Y":
        return True
    else:
        return False


def spot_taken(updated_spot, current_board):
    """
    Takes in the current player's spot choice and sees if that space is taken on the board.
    :param updated_spot: Current player's spot choice.
    :param current_board: Current board.
    :return: True or False if player's spot choice is occupied.
    """
    game = updated_spot[0]
    spot = int(updated_spot[1]) - 1
    return "X" == current_board[game][spot] or "O" == current_board[game][spot]


def spot_is_valid(spot):
    """
    Returns True or False to determine if entered spot is valid(A9 or C7, not AA or 99)
    :param spot: User inputted spot A-I, 1-9
    :return: True or False if spot is valid
    """
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if len(spot) != 2:
        return False
    elif spot == "  " or not spot[0] in letters or not spot[1] in numbers:
        return False
    else:
        return True