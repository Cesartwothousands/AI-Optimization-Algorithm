import random
import heapq

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For Search Algorithms 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''

'''
BFS add to queue 
'''

BFS_queue = []
DFS_stack = []
priority_queue = []


class Node:
    def __init__(self, node_id, parent_node_id, cost):
        self.node_id = node_id
        self.parent_node_id = parent_node_id
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


def add_to_queue_BFS(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    if initialize:
        BFS_queue.clear()
    BFS_queue.append((node_id, parent_node_id))
    return


'''
BFS add to queue 
'''


def is_queue_empty_BFS():
    # Your code here
    return len(BFS_queue) == 0


'''
BFS pop from queue
'''


def pop_front_BFS():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    (node_id, parent_node_id) = BFS_queue.pop(0)
    return node_id, parent_node_id


'''
DFS add to queue 
'''


def add_to_queue_DFS(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    if initialize:
        DFS_stack.clear()
    DFS_stack.append((node_id, parent_node_id))
    return


'''
DFS add to queue 
'''


def is_queue_empty_DFS():
    # Your code here
    return len(DFS_stack) == 0


'''
DFS pop from queue
'''


def pop_front_DFS():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    (node_id, parent_node_id) = DFS_stack.pop()
    return node_id, parent_node_id


'''
UC add to queue 
'''


def add_to_queue_UC(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    if initialize:
        priority_queue.clear()
    heapq.heappush(priority_queue, Node(node_id, parent_node_id, cost))
    return


'''
UC add to queue 
'''


def is_queue_empty_UC():
    # Your code here
    return len(priority_queue) == 0


'''
UC pop from queue
'''


def pop_front_UC():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    node = heapq.heappop(priority_queue)
    (node_id, parent_node_id) = node.node_id, node.parent_node_id
    return node_id, parent_node_id


'''
A* add to queue 
'''


def add_to_queue_ASTAR(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    if initialize:
        priority_queue.clear()
    heapq.heappush(priority_queue, Node(node_id, parent_node_id, cost))
    return


'''
A* add to queue 
'''


def is_queue_empty_ASTAR():
    # Your code here
    return len(priority_queue) == 0


'''
A* pop from queue
'''


def pop_front_ASTAR():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    node = heapq.heappop(priority_queue)
    (node_id, parent_node_id) = node.node_id, node.parent_node_id
    return node_id, parent_node_id


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
