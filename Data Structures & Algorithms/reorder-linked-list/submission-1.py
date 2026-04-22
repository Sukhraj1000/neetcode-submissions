# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Edge case: if the list is empty or has one element, do nothing
        if not head or not head.next:
            return

        # Step 1: Find the middle of the linked list using slow and fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next         # Move slow by 1
            fast = fast.next.next   # Move fast by 2

        # Step 2: Reverse the second half of the list
        second = slow.next          # Second half starts after the middle
        prev = None                 # Initialize previous pointer for reversal
        slow.next = None            # Cut off the first half of the list
        while second:
            tmp = second.next       # Store next node
            second.next = prev      # Reverse the pointer
            prev = second           # Move prev forward
            second = tmp            # Move to the next node

        # Step 3: Merge the two halves alternately
        first, second = head, prev  # First points to start of first half, second to reversed second half
        while second:
            tmp1 = first.next       # Store next node in first half
            tmp2 = second.next      # Store next node in second half
            first.next = second     # Link first node to next from second half
            second.next = tmp1      # Link second node to next in first half
            first, second = tmp1, tmp2  # Move both pointers forward
