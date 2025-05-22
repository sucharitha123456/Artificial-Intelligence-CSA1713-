from collections import deque
def water_jug_bfs(x, y, z):
    visited = set()
    queue = deque()
    queue.append((0, 0))
    visited.add((0, 0))
    while queue:
        a, b = queue.popleft()
        print(f"Jug A: {a} | Jug B: {b}")
        if a == z or b == z:
            print("Target reached!")
            return True
        next_states = [
            (x, b),    
            (a, y),    
            (0, b),    
            (a, 0),    
            (0, a + b) if a + b <= y else (a - (y - b), y), 
            (a + b, 0) if a + b <= x else (x, b - (x - a)), 
        ]
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
    print("No solution.")
    return False
water_jug_bfs(4,3,2)
