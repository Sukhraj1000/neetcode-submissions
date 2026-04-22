# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers:
        # `prev` will eventually point to the new head (reversed list)
        # `curr` is the pointer for iterating through the original list
        prev, curr = None, head

        # Iterate through the linked list until we reach the end
        while curr:
            # Temporarily store the next node (so we don't lose it after reversing the pointer)
            temp = curr.next

            # Reverse the current node's pointer so it points to the previous node
            curr.next = prev

            # Move `prev` and `curr` one step forward
            prev = curr       # `prev` becomes the current node
            curr = temp       # `curr` moves to the next node (stored in temp)

        # After the loop, `prev` points to the new head of the reversed list
        return prev
