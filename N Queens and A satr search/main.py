import mp520 as mp

def _get_test_graph_admissible():
    _graph = dict()
    _graph[1] = [1, False, 0, 0, 7, [(2, 1), (3, 4)], {2:1, 3:4}]
    _graph[2] = [2, False, 0, 0, 6, [(3, 2), (4, 5), (5, 12)], {3:2, 4:5, 5:12}]
    _graph[3] = [3, False, 0, 0, 2, [(4, 2)], {4:2}]
    _graph[4] = [4, False, 0, 0, 1, [(5, 3)], {5:3}]
    _graph[5] = [5, False, 0, 0, 0, [], {}]
    return _graph

def _get_test_graph_consistent():
    _graph = dict()
    _graph[1] = [1, False, 0, 0, 7, [(2, 1), (3, 4)], {2:1, 3:4}]
    _graph[2] = [2, False, 0, 0, 6, [(3, 2), (4, 5), (5, 12)], {3:2, 4:5, 5:12}]
    _graph[3] = [3, False, 0, 0, 4, [(4, 2)], {4:2}]
    _graph[4] = [4, False, 0, 0, 2, [(5, 3)], {5:3}]
    _graph[5] = [5, False, 0, 0, 0, [], {}]
    return _graph

def _retrieve_solution(graph, goal_node_id):
    path = []
    cost = 0
    # Your code here #
    current_node = graph[goal_node_id]
    path.insert(0, current_node[0])
    while current_node[2] != 0:
        prev_node = graph[current_node[2]]
        current_node = prev_node
        path.insert(0, current_node[0])
    cost = graph[goal_node_id][3] 
    return (cost, path)

def _heuristic_function(graph, node_id):
    return graph[node_id][4]

def _heuristic_zero(graph, node_id):
    return 0

'''
Generic graph search skeleton 
'''
def _graph_search(graph, start_node_id, goal_node_id, _add_to_queue, is_queue_empty, _pop, _heuristic, a = 1, b = 1):
    #Counting the expansion
    expansion_count = 0
    
    _add_to_queue(start_node_id, 0, 0 + _heuristic(graph, start_node_id)*b, True)
    # Go through the queue unless empty 
    while is_queue_empty() == False:
        # Pop the first node (id) out of the queue
        (node_id, parent_node_id) = _pop()
        node = graph[node_id]

        # Check whether the node is already visited
        if node[1] == True:
            continue

        # Set node to be visited
        expansion_count = expansion_count + 1
        node[1] = True
        node[2] = parent_node_id
        if node_id != start_node_id:
            node[3] = graph[parent_node_id][3] + graph[parent_node_id][6][node_id]
        
        # Check whether we are at goal
        if node[0] == goal_node_id:
            (cost, path) = _retrieve_solution(graph, goal_node_id)
            return (expansion_count, cost, path)

        # Work with the neighbors 
        for n in range(0, len(node[5])):
            nbr = node[5][n]
            if graph[nbr[0]][1] == False:
                _add_to_queue(nbr[0], node_id, graph[node_id][6][nbr[0]]*a + _heuristic(graph, nbr[0])*b)
        
    return (-1, 0, 0)


if __name__ == "__main__":
    print ("Graph search result dump")

    # DFS
    graph = _get_test_graph_admissible()
    (expansion_count, cost, path) = _graph_search(graph, 1, 5, mp.add_to_queue_DFS,
        mp.is_queue_empty_DFS, mp.pop_front_DFS, _heuristic_zero)
    print ("DFS path: " + str(path) + ", cost: " + str(cost) + ", #expansions: " \
        + str(expansion_count))

    # BFS
    graph = _get_test_graph_admissible()
    (expansion_count, cost, path) = _graph_search(graph, 1, 5, mp.add_to_queue_BFS,
        mp.is_queue_empty_BFS, mp.pop_front_BFS, _heuristic_zero)
    print ("BFS path: " + str(path) + ", cost: " + str(cost) + ", #expansions: " \
        + str(expansion_count))

    # UC
    graph = _get_test_graph_admissible()
    (expansion_count, cost, path) = _graph_search(graph, 1, 5, mp.add_to_queue_UC,
        mp.is_queue_empty_UC, mp.pop_front_UC, _heuristic_zero)
    print ("UC path: " + str(path) + ", cost: " + str(cost) + ", #expansions: " \
        + str(expansion_count))

    # A* admissible 
    graph = _get_test_graph_admissible()
    (expansion_count, cost, path) = _graph_search(graph, 1, 5, mp.add_to_queue_ASTAR,
        mp.is_queue_empty_ASTAR, mp.pop_front_ASTAR, _heuristic_function)
    print ("A* (admissible) path: " + str(path) + ", cost: " + str(cost) \
          + ", #expansions: " + str(expansion_count))

    # A* consistent 
    graph = _get_test_graph_consistent()
    (expansion_count, cost, path) = _graph_search(graph, 1, 5, mp.add_to_queue_ASTAR,
        mp.is_queue_empty_ASTAR, mp.pop_front_ASTAR, _heuristic_function)
    print ("A* (consistent) path: " + str(path) + ", cost: " + str(cost)  \
          + ", #expansions: " + str(expansion_count))

    print
    print ("The n-queens problem" )

    n = 7 
    # Get a basic state
    state = mp.get_random_state(n)
    print ("A random atate: " + str(state) + ", conflicting pairs: " + str(mp.compute_attacking_pairs(state)))

    # Call hill-descending once 
    new_state = mp.hill_desending_n_queens(state, mp.compute_attacking_pairs)
    print ("Final state after hill-descending: " + str(new_state) + ", conflicting pairs: " \
          + str(mp.compute_attacking_pairs(new_state)))

    # Get a fully solved state for a given n    
    print ("A valid solution: " + str(mp.n_queens(n,
        mp.get_random_state, mp.compute_attacking_pairs,mp.hill_desending_n_queens)))

    

