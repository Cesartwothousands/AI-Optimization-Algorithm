import mp520 as mp
import time


def _print_game_state(state):
    for i in range(0, len(state)):
        print(state[i])


def _get_empty_state(n):
    # Initialize the state (2D array)
    state = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            row.append(" ")
        state.append(row)
    return state


def _get_default_start_game_state_4():
    state = _get_empty_state(4)

    state[1][1] = state[2][2] = "B"
    state[1][2] = state[2][1] = "W"

    return state


def _get_start_game_state_4_8():
    state = _get_empty_state(4)

    state[1][0] = state[1][1] = state[1][2] = state[1][3] = "B"
    state[2][0] = state[2][1] = state[2][2] = state[2][3] = "W"

    return state


def _get_default_start_game_state_5():
    state = _get_empty_state(5)

    state[0][0] = state[1][1] = state[3][4] = state[4][3] = "W"
    state[1][0] = state[0][1] = state[3][3] = state[4][4] = "B"

    return state


if __name__ == "__main__":
    p1 = "B"
    p2 = "W"

    # Retrieve a initial game state for the special 4 x 4 game.
    # Note that this is NOT the default 4 x 4 game
    game_state = _get_start_game_state_4_8()

    # Get a fully solved state for a given n
    print("Printing the initial game state for a 4 x 4 game:")
    _print_game_state(game_state)
    print()

    # Get game value
    print("The state of the game is: " + str(mp.count_pieces(game_state)))
    print()

    # Test move values
    print(
        "Game value if black places on (3, 2): "
        + str(mp.get_move_value(game_state, p1, 3, 2))
    )
    print(
        "Game value if white places on (0, 2): "
        + str(mp.get_move_value(game_state, p2, 0, 2))
    )
    print()

    # Make a move
    print("State after executing the move of (3, 3) for player one")
    _print_game_state(mp.execute_move(game_state, p1, 3, 3))
    print()

    # Compute best game play with minimax
    start_time = time.time()
    print("Running full minimax: ")
    print(mp.full_minimax(game_state, p1))
    elapsed_time = time.time() - start_time
    print("Elapsed time: " + str(elapsed_time))
    print()

    # Compute best game play with alpha-beta pruning
    start_time = time.time()
    print("Running full minimax w/ alpha-beta pruning: ")
    print(mp.full_minimax_ab(game_state, p1))
    elapsed_time = time.time() - start_time
    print(("Elapsed time: " + str(elapsed_time)))
