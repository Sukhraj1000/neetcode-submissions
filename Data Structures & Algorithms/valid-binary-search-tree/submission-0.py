# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
         # Helper function to check if the current node is within valid range
        def valid(node, left, right):
            if not node:
                return True  # An empty node is always valid
            
            # If the node value breaks the BST rule, return False
            if not (node.val > left and node.val < right):
                return False
            
            # Recursively check the left and right subtrees
            # For left subtree, update the max allowed value to current node's value
            # For right subtree, update the min allowed value to current node's value
            return (valid(node.left, left, node.val) and 
                    valid(node.right, node.val, right))

        # Start the recursion with the entire number range allowed
        return valid(root, float("-inf"), float("inf"))