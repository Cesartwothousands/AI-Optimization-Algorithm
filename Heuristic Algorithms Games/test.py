import N_Queens_Problem as mp

if __name__ == "__main__":

    print("The n-queens problem")

    n = 7
    # Get a basic state
    state = mp.get_random_state(n)
    print("A random atate: " + str(state) + ", conflicting pairs: " +
          str(mp.compute_attacking_pairs(state)))

    # Call hill-descending once
    new_state = mp.hill_desending_n_queens(state, mp.compute_attacking_pairs)
    print("Final state after hill-descending: " + str(new_state) + ", conflicting pairs: "
          + str(mp.compute_attacking_pairs(new_state)))

    # Get a fully solved state for a given n
    print("A valid solution: " + str(mp.n_queens(n,
                                                 mp.get_random_state, mp.compute_attacking_pairs,
                                                 mp.hill_desending_n_queens)))
