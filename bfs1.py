from collections import deque
def bfs(graph, start):
    visited = set()        
    queue = deque([start])   
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')  
            visited.add(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print("BFS traversal starting from node A:")
bfs(graph,'A')
