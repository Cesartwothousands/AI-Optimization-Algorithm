import random

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For n-queens problem 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''

'''
Compute a random state 
'''


def get_random_state(n):
    state = []
    # Your code here

    for i in range(n):
        location = random.randint(1, n)
        state.append(location)

    return state


'''
Compute pairs of queens in conflict 
'''


def compute_attacking_pairs(state):
    number_attacking_pairs = 0
    # Your code here

    n = len(state)

    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] == state[j] or abs(state[i]-state[j]) == abs(i-j):
                number_attacking_pairs += 1

    return number_attacking_pairs


'''
The basic hill-climing algorithm for n queens
'''


def hill_desending_n_queens(state, comp_att_pairs):
    final_state = []
    # Your code here

    #n = len(state)
    current_state = state
    current_fun = comp_att_pairs(current_state)

    while (1):
        neighbors = []

        for i in range(len(state)):
            for j in range(1, len(state)+1):
                if j != current_state[i]:
                    neighbor = list(current_state)
                    neighbor[i] = j
                    neighbors.append(neighbor)

        if not neighbors:
            return state

        best_neighbor = current_state
        best_fun = current_fun

        for neighbor in neighbors:
            neighbor_fun = comp_att_pairs(neighbor)

            if neighbor_fun < best_fun:
                best_neighbor = neighbor
                best_fun = neighbor_fun

        if best_fun >= current_fun:
            final_state = current_state
            return final_state

        current_state = best_neighbor
        current_fun = best_fun


'''
Hill-climbing algorithm for n queens with restart
'''


def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
    final_state = []
    # Your code here

    state = []

    while (1):
        state = get_rand_st(n)
        final_state = hill_descending(state, comp_att_pairs)
        if comp_att_pairs(final_state) == 0:
            return final_state
