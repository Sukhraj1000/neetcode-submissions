# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val          # value of the node
#         self.left = left        # left child
#         self.right = right      # right child

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]  # A list used to store the maximum diameter found so far. List is used to allow modification inside dfs function.

        def dfs(root):
            if not root:  # If the current node is null, return -1 (no edge below it)
                return -1

            left = dfs(root.left)   # Recursively find height of left subtree
            right = dfs(root.right) # Recursively find height of right subtree

            # Diameter at this node = number of edges between left and right child (+2)
            res[0] = max(res[0], 2 + left + right)

            # Return height of current node (1 + max height of left/right subtree)
            return 1 + max(left, right)

        dfs(root)        # Start DFS traversal from the root
        return res[0]    # Return the maximum diameter found
