"""
Compute the value brought by a given move by placing a new token for player at (row, column). The value is the number of opponent pieces getting flipped by the move. 

A move is valid if for the player, the location specified by (row, column) is (1) empty and (2) will cause some pieces from the other player to flip. The return value for the function should be the number of pieces hat will be moved. If the move is not valid, then the value 0 (zero) should be returned. Note here that row and column both start with index 0. 
"""


def get_move_value(state, player, row, column):
    flipped = 0
    opponent = ''
    # Your implementation goes here

    # Choose opponent
    if player == "W":
        opponent = "B"
    elif player == "B":
        opponent = "W"
    else:
        print('get_move_value: Wrong Player Input', state, player, row, column)

    # Check the cell is already occupied
    if state[row][column] == 'B' or state[row][column] == 'W':
        return 0

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                  (1, 1), (-1, 1), (1, -1), (-1, -1)]

    for direction in directions:
        current_flipped = 0
        r = row
        c = column

        while True:
            r += direction[0]
            c += direction[1]

            if r < 0 or c < 0 or r >= len(state) or c >= len(state):
                current_flipped = 0
                break

            if state[r][c] == ' ':
                current_flipped = 0
                break

            elif state[r][c] == player:
                break

            elif state[r][c] == opponent:
                current_flipped += 1

        flipped += current_flipped

    # If no tokens are flipped, the move is invalid
    if flipped == 0:
        return 0
    else:
        return flipped


"""
Execute a move that updates the state. A new state should be crated. The move must be valid. Note that the new state should be a clone of the old state and in particular, should not share memory with the old state. 
"""


def execute_move(state, player, row, column):
    new_state = None
    opponent = ''
    flipped = get_move_value(state, player, row, column)
    # Your implementation goes here

    # Choose opponent
    if player == 'W':
        opponent = 'B'
    elif player == 'B':
        opponent = 'W'

    if flipped == 0:
        return state

    new_state = [list(row) for row in state]
    new_state[row][column] = player

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                  (1, 1), (-1, 1), (1, -1), (-1, -1)]

    for direction in directions:
        current_flipped = 0
        r = row
        c = column

        while True:
            r += direction[0]
            c += direction[1]

            if r < 0 or c < 0 or r >= len(state) or c >= len(state):
                current_flipped = 0
                break

            elif state[r][c] == ' ':
                current_flipped = 0
                break

            elif state[r][c] == player:
                for i in range(1, current_flipped+1):
                    # Flip the opponent's tokens
                    new_state[row + i*direction[0]
                              ][column + i*direction[1]] = player

                current_flipped = 0
                break

            elif state[r][c] == opponent:
                current_flipped += 1

    return new_state


"""
A method for counting the pieces owned by the two players for a given state. The return value should be two tuple in the format of  (blackpeices, white pieces), e.g.,

    return (4, 3)

"""


def count_pieces(state):
    blackpieces = 0
    whitepieces = 0
    # Your implementation goes here

    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == 'B':
                blackpieces += 1
            elif state[i][j] == 'W':
                whitepieces += 1

    return (blackpieces, whitepieces)


"""
Check whether a state is a terminal state. 
"""


def is_terminal_state(state, state_list=None):
    terminal = False
    # Your implementation goes here

    for i in range(len(state)):
        for j in range(len(state)):
            if get_move_value(state, 'W', i, j) != 0 or get_move_value(state, 'B', i, j) != 0:
                return terminal

    return not terminal


"""
The minimax algorithm. Your implementation should return the best value for the given state and player, as well as the next immediate move to take for the player. 
"""


def minimax(state, player):
    value = 0
    row = -1
    column = -1

    def get_opponent(player):
        opponent = ''
        # Choose opponent
        if player == 'W':
            opponent = 'B'
        elif player == 'B':
            opponent = 'W'
        else:
            print('minimax: Wrong Player Input')

        return opponent

    # Your implementation goes here

    value = -10000000 if player == "B" else 10000000

    for r in range(len(state)):
        for c in range(len(state)):
            move_value = get_move_value(state, player, r, c)
            if move_value > 0:
                new_state = execute_move(state, player, r, c)
                maxmin, row, column = minimax(
                    new_state, "B" if player == "W" else "W")

                if (player == 'B' and maxmin > value) or (player == 'W' and maxmin < value):
                    value = maxmin
                    row = r
                    column = c

    # Change player
    if row == -1 and column == -1:
        player = get_opponent(player)
        value, row, column = minimax(state, player)

    return (value, row, column)


"""
This method should call the minimax algorithm to compute an optimal move sequence that leads to an end game. 
"""


def full_minimax(state, player, depth):
    value = 0
    move_sequence = []

    def get_opponent(player):
        opponent = ''

        # Choose opponent
        if player == 'W':
            opponent = 'B'
        elif player == 'B':
            opponent = 'W'
        else:
            print('minimax: Wrong Player Input')

        return opponent

    # Your implementation goes here

    if depth == 0 or is_terminal_state(state):
        return (count_pieces(state)[0]-count_pieces(state)[1], [(player, -1, -1)])

    value = -10000000 if player == "B" else 10000000

    for r in range(len(state)):
        for c in range(len(state)):
            move_value = get_move_value(state, player, r, c)
            if move_value > 0:
                new_state = execute_move(state, player, r, c)
                #player = get_opponent(player)
                maxmin, step = full_minimax(
                    new_state, "B" if player == "W" else "W", depth-1)

                if (player == 'B' and maxmin > value) or (player == 'W' and maxmin < value):
                    value = maxmin
                    move_sequence = [(player, r, c)] + step

    if move_sequence == []:
        player = get_opponent(player)
        value, move_sequence = full_minimax(state, player, depth-1)

    return (value, move_sequence)


"""
The minimax algorithm with alpha-beta pruning. Your implementation should return the
best value for the given state and player, as well as the next immediate move to take
for the player. 
"""


def minimax_ab(state, player, alpha=-10000000, beta=10000000):
    value = 0
    row = -1
    column = -1

    def get_opponent(player):
        opponent = ''

        # Choose opponent
        if player == 'W':
            opponent = 'B'
        elif player == 'B':
            opponent = 'W'
        else:
            print('minimax: Wrong Player Input')

        return opponent

    # Your implementation goes here

    if is_terminal_state(state):
        return (count_pieces(state)[0]-count_pieces(state)[1], [(player, -1, -1)])

    value = -10000000 if player == "B" else 10000000

    for i in range(len(state)):
        for j in range(len(state)):
            move_value = get_move_value(state, player, i, j)
            if move_value > 0:

                new_state = execute_move(state, player, i, j)
                maxmin,  row, column = minimax_ab(
                    new_state, "B" if player == "W" else "W")

            if maxmin > value and player == 'B' or maxmin < value and player == 'W':
                value = maxmin
                row, column = i, j
            alpha = max(alpha, value) if player == 'B' else alpha
            beta = min(beta, value) if player == 'W' else beta
            if alpha >= beta:
                break

    if row == -1 and column == -1:
        player = get_opponent(player)
        value, row, column = minimax_ab(state, player)

    return (value, row, column)


"""
This method should call the minimax_ab algorithm to compute an optimal move sequence
that leads to an end game, using alpha-beta pruning.
"""


def full_minimax_ab(state, player, depth):
    value = 0
    move_sequence = []
    alpha = -10000000
    beta = 10000000

    def get_opponent(player):
        opponent = ''

        # Choose opponent
        if player == 'W':
            opponent = 'B'
        elif player == 'B':
            opponent = 'W'
        else:
            print('minimax: Wrong Player Input')

        return opponent

    # Your implementation goes here

    if depth == 0 or is_terminal_state(state):
        return (count_pieces(state)[0]-count_pieces(state)[1], [(player, -1, -1)])

    value = -10000001 if player == "B" else 10000001

    cut = False
    for r in range(len(state)):
        for c in range(len(state)):
            move_value = get_move_value(state, player, r, c)
            if move_value > 0:

                new_state = execute_move(state, player, r, c)
                maxmin, step = full_minimax_ab(
                    new_state, "B" if player == "W" else "W", depth-1)

                if player == 'B':
                    if maxmin > value:
                        value = maxmin
                        move_sequence = [(player, r, c)] + step

                    if value >= beta:
                        cut = True
                        break

                    alpha = max(alpha, value)

                else:
                    if maxmin < value:
                        value = maxmin
                        move_sequence = [(player, r, c)] + step

                    if value <= alpha:
                        cut = True
                        break

                    beta = min(beta, value)

        if cut == True:
            break

    if move_sequence == []:
        player = get_opponent(player)
        value, move_sequence = full_minimax_ab(state, player, depth-1)

    return (value, move_sequence)
