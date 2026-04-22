class Solution:
     def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Each row, column, and 3x3 box will store numbers we've already seen
        cols = collections.defaultdict(set)     # Tracks numbers in each column
        rows = collections.defaultdict(set)     # Tracks numbers in each row
        squares = collections.defaultdict(set)  # Tracks numbers in each 3x3 square (box)

        # Loop through each row (0 to 8)
        for r in range(9):
            # Loop through each column (0 to 8)
            for c in range(9):
                # If the current cell is empty, skip it
                if board[r][c] == '.':
                    continue

                # Check if this number already exists:
                # - in the same column
                # - in the same row
                # - in the same 3x3 square
                if (board[r][c] in cols[c] or 
                    board[r][c] in rows[r] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False  # If it exists, it's not a valid Sudoku

                # If number is not found, we add it to:
                cols[c].add(board[r][c])                 # Add to this column's set
                rows[r].add(board[r][c])                 # Add to this row's set
                squares[(r // 3, c // 3)].add(board[r][c])  # Add to the correct 3x3 box

        # If we checked every cell and found no issues, the board is valid
        return True