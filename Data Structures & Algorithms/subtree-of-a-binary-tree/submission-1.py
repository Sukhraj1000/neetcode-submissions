# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val            # value stored at the node
#         self.left = left          # pointer to the left child node
#         self.right = right        # pointer to the right child node

class Solution:
    # This function checks if subroot is a subtree of root
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        
        # If subroot is None (empty), it's always a subtree
        if not subroot:
            return True
        
        # If main tree (root) is empty but subroot isn't, subroot can't be a subtree
        if not root:
            return False
        
        # If the current part of root and subroot are the same tree, return True
        if self.sameTree(root, subroot):
            return True
        
        # Otherwise, keep checking the left and right branches of root
        return (self.isSubtree(root.left, subroot) 
                or self.isSubtree(root.right, subroot))

    # Helper function to check if two trees are exactly the same
    def sameTree(self, root, subroot):
        # If both trees are empty, they are the same
        if not root and not subroot:
            return True
        
        # If both nodes exist and values match, check both subtrees
        if root and subroot and root.val == subroot.val:
            return (self.sameTree(root.left, subroot.left) and
                    self.sameTree(root.right, subroot.right))
        
        # Otherwise, the trees are not the same
        return False
