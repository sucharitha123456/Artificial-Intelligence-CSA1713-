import heapq
dirs = [(-1,0), (1,0), (0,-1), (0,1)]
class Node:
    def __init__(self, position, g, h, parent=None):
        self.position = position 
        self.g = g                
        self.h = h                
        self.f = g + h            
        self.parent = parent     
    def __lt__(self, other): 
        return self.f < other.f
def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def astar(grid, start, goal):
    open_list = []
    closed_set = set()
    start_node = Node(start, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)
    while open_list:
        current = heapq.heappop(open_list)
        if current.position == goal:
            path = []
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Reverse path
        closed_set.add(current.position)
        for d in dirs:
            neighbor_pos = (current.position[0] + d[0], current.position[1] + d[1])
            if (0 <= neighbor_pos[0] < len(grid) and
                0 <= neighbor_pos[1] < len(grid[0]) and
                grid[neighbor_pos[0]][neighbor_pos[1]] == 0 and
                neighbor_pos not in closed_set):
                g_cost = current.g + 1
                h_cost = heuristic(neighbor_pos, goal)
                neighbor = Node(neighbor_pos, g_cost, h_cost, current)
                if all(neighbor.position != n.position or neighbor.f < n.f for n in open_list):
                    heapq.heappush(open_list, neighbor)
    return None 
grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (4, 4)
path = astar(grid, start, goal)
print("Path found by A*:", path)
