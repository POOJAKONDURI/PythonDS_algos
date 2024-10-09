
'''

    @Author:pooja
    @Date:09-10-2024
    @last modified by:
    @last modified time:
    @title:traversing graph using DFS

'''


def dfs(graph, start_node):
    visited = set()  # To keep track of visited nodes
    stack = [start_node]  # Stack to manage explore
    while stack:
        # Pop a node from the top of the stack
        node = stack.pop()
        
        # If the node hasn't been visited, visit it
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # Push all unvisited neighbors onto the stack
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    dfs(graph, 'A')  
if __name__ == "__main__":
    main()