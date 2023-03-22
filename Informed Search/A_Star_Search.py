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
