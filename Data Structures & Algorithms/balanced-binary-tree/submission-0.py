# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val               # value stored in the node
#         self.left = left             # points to the left child
#         self.right = right           # points to the right child

class Solution:
    # This function checks if a binary tree is height-balanced
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # This is a helper function that uses DFS (depth-first search)
        def dfs(root):
            # If the node is empty (base case), we say it's balanced and its height is 0
            if not root: 
                return [True, 0]  # [Is this subtree balanced?, Height of this subtree]

            # Recursively check the left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)

            # A tree is balanced if:
            # - Left subtree is balanced (left[0] == True)
            # - Right subtree is balanced (right[0] == True)
            # - Height difference between left and right is no more than 1
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            # Return whether this subtree is balanced and its height
            # Height of current node = 1 + max height of left or right child
            return [balanced, 1 + max(left[1], right[1])]

        # Start the DFS from the root and return whether the whole tree is balanced
        return dfs(root)[0]
