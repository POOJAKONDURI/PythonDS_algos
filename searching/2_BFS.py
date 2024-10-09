

'''

    @Author:pooja
    @Date:09-10-2024
    @last modified by:
    @last modified time:
    @title:program to traverse using BFS

'''


from collections import deque

def bfs(graph, start_node):
    visited = set()  # To keep track of visited nodes
    queue = deque([start_node])  # Queue to manage exploration
    
    visited.add(start_node)
    
    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()
        print(node, end=" ")
        
        # Explore all unvisited neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')  # Output: A B C D E F
