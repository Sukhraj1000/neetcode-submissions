# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0  # Counter to track how many nodes we've visited so far
        stk = []  # Stack to simulate the recursion (used for in-order traversal)
        cur = root  # Start from the root of the tree

        # Continue while there's still a node to visit or stack is not empty
        while cur or stk:
            # Go as left as possible (left children are smaller in BST)
            while cur:
                stk.append(cur)  # Save the current node so we can come back to it
                cur = cur.left   # Move to the left child

            cur = stk.pop()  # Pop the node from the top of the stack (next smallest)
            n += 1  # We've now visited one more node

            if n == k:  # If this is the k-th smallest node
                return cur.val  # Return its value

            cur = cur.right  # Otherwise, move to the right subtree to continue