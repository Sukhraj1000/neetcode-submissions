# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # This function checks if two trees (p and q) are exactly the same
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Base case: if both p and q are None (empty), they are the same
        if not p and not q:
            return True

        # If one is None and the other isn’t, or values don’t match → not the same
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check:
        # - are the left subtrees the same?
        # - are the right subtrees the same?
        # Only return True if **both** sides match
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))


        