class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # If there are no nodes, by default it's a valid tree (nothing to validate)
        if not n:
            return True
        
        # Create an adjacency list for the undirected graph
        adj = { i:[] for i in range(n)}  # Example: if n=3 → {0: [], 1: [], 2: []}
        for n1, n2 in edges:
            # Because it's an undirected graph, add each node to the other's list
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()  # To keep track of visited nodes and avoid cycles

        # Depth-First Search function to detect cycles and traverse the graph
        def dfs(i, prev):
            if i in visit:
                # If we revisit a node that is not the parent, there's a cycle → not a valid tree
                return False
            visit.add(i)  # Mark node as visited

            # Explore all connected nodes (neighbors)
            for j in adj[i]:
                if j == prev:
                    # Skip the node we just came from to avoid false cycle detection
                    continue
                if not dfs(j, i):
                    # If any recursive call detects a cycle, it's not a valid tree
                    return False
            return True  # No cycle found from this path

        # The graph is a valid tree if:
        # 1. There's no cycle (dfs returns True)
        # 2. All nodes are connected (we visited all of them)
        return dfs(0, -1) and n == len(visit)
