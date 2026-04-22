"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}  # Dictionary to map original node -> cloned node
        
        def dfs(node):
            if node in visited:
                return visited[node]  # If already cloned, return the clone

            copy = Node(node.val)  # Create a new copy of the current node
            visited[node] = copy  # Mark it as visited
            for neighbor in node.neighbors:  # Corrected here
                copy.neighbors.append(dfs(neighbor))  # Recursively clone neighbors
            return copy
        
        return dfs(node) if node else None  # Start DFS if node exists