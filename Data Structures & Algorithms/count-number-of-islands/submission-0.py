import collections  # Importing collections module to use deque for efficient queue operations

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:  # If the input grid is empty or None, return 0 (no islands)
            return 0

        rows, cols = len(grid), len(grid[0])  # Get the number of rows and columns in the grid
        visit = set()  # This will store the coordinates of cells we've already visited
        islands = 0  # Counter to keep track of how many islands we've found

        def bfs(r, c):  # Breadth-First Search starting from cell (r, c)
            q = collections.deque()  # Use deque as a queue for BFS
            visit.add((r, c))  # Mark the starting cell as visited
            q.append((r, c))  # Add the starting cell to the queue

            while q:  # While there are still cells to explore
                row, col = q.popleft()  # Remove the next cell from the queue
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # Define 4 possible directions: down, up, right, left

                for dr, dc in directions:  # Loop through each direction
                    r, c = row + dr, col + dc  # Calculate new cell's row and column
                    # Check if the new cell is within bounds and is land ('1') and not visited yet
                    if (r in range(rows) and 
                        c in range(cols) and
                        grid[r][c] == '1' and
                        (r, c) not in visit):
                        q.append((r, c))  # Add the new land cell to the queue
                        visit.add((r, c))  # Mark the new cell as visited

        # Loop through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell is land ('1') and hasn't been visited yet
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)  # Run BFS to visit the entire island
                    islands += 1  # Increase the island counter by 1

        return islands  # Return the total number of islands found
