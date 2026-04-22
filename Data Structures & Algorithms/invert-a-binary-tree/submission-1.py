# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val          # value stored in the node
#         self.left = left        # pointer to the left child
#         self.right = right      # pointer to the right child

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None  # Base case: if the node is empty, nothing to invert

        # Swap the left and right child of the current node
        tmp = root.left              # temporarily store the left child
        root.left = root.right       # assign right child to left
        root.right = tmp             # assign stored left child to right

        # Recursively call the same function to invert the left and right subtrees
        self.invertTree(root.left)   # invert the new left subtree
        self.invertTree(root.right)  # invert the new right subtree

        return root  # Return the root after its subtrees have been inverted
