import heapq

# Define the A* algorithm


def astar(start, goal, obstacles):
    # Initialize open and closed lists
    open_list = []
    closed_list = set()
    # Add the start node to the open list
    heapq.heappush(open_list, (0, start))
    # Initialize the cost and parent dictionaries
    cost = {start: 0}
    parent = {start: None}
    # Start the search
    while open_list:
        # Get the node with the lowest cost from the open list
        current = heapq.heappop(open_list)[1]
        # If we've reached the goal, return the path
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path
        # Add the current node to the closed list
        closed_list.add(current)
        # Generate the neighbors of the current node
        for neighbor in get_neighbors(current, obstacles):
            # If the neighbor is already in the closed list, skip it
            if neighbor in closed_list:
                continue
            # Calculate the cost of moving to the neighbor
            new_cost = cost[current] + distance(current, neighbor)
            # If the neighbor is not in the open list, add it
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + distance(neighbor, goal)
                heapq.heappush(open_list, (priority, neighbor))
                parent[neighbor] = current
    # If we reach this point, there is no path to the goal
    return None

# Define a function to get the neighbors of a node


def get_neighbors(node, obstacles):
    neighbors = []
    x, y = node
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            neighbor = (x + dx, y + dy)
            if neighbor not in obstacles:
                neighbors.append(neighbor)
    return neighbors

# Define a function to calculate the distance between two nodes


def distance(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return abs(x1 - x2) + abs(y1 - y2)

# Define the main function


def main():
    # Define the start and goal nodes for each robot
    robots = {
        'R1': ((0, 0), (3, 3)),
        'R2': ((5, 5), (1, 1)),
        'R3': ((2, 2), (4, 4))
    }
    # Define the obstacles
    obstacles = {(2, 0), (2, 1), (2, 2), (2, 3)}
    # Plan the paths for each robot
    paths = {}
    for name, (start, goal) in robots.items():
        path = astar(start, goal, obstacles)
        if path is None:
            print(f'{name} could not find a path to the goal')
            return
        paths[name] = path
    # Print the paths
    for name, path in paths.items():
        print(f'{name}: {path}')


if __name__ == '__main__':
    main()
