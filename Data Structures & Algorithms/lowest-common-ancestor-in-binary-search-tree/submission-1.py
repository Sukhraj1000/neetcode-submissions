# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
     # Function to find the Lowest Common Ancestor (LCA) of nodes p and q in a BST
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root  # Start the search from the root node

        while cur:  # While we haven't reached the end of the tree
            # If both p and q are greater than current node, LCA must be in the right subtree
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # If both p and q are less than current node, LCA must be in the left subtree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                # This is the split point — one node is on the left and one is on the right,
                # or we've found one of the nodes (which can also be the LCA)
                return cur
        
        