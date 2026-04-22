# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []  # This will store the final result — a list of levels, each level is a list of node values

        q = collections.deque()  # We use a queue (deque) for BFS traversal
        q.append(root)  # Start with the root node in the queue

        while q:  # Keep going while there are nodes in the queue
            qLen = len(q)  # Number of nodes at the current level
            level = []  # Temporary list to store values at this level

            for i in range(qLen):  # Process all nodes at the current level
                node = q.popleft()  # Remove the node from the queue

                if node:  # Only proceed if the node is not None
                    level.append(node.val)  # Add the node's value to the current level list
                    q.append(node.left)  # Add the left child to the queue (can be None)
                    q.append(node.right)  # Add the right child to the queue (can be None)

            if level:  # If we collected any values for this level, add it to the result
                res.append(level)

        return res  # Return the full list of levels