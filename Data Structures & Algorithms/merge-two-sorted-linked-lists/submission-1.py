# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node that acts as the start of the merged list
        # `node` will be used to build the new list step-by-step
        dummy = node = ListNode()

        # Loop until we reach the end of either list1 or list2
        while list1 and list2:
            # Compare values at the current nodes of both lists
            if list1.val < list2.val:
                # If list1's value is smaller, link it to the merged list
                node.next = list1
                # Move list1 pointer forward
                list1 = list1.next
            else:
                # Otherwise, link list2's node
                node.next = list2
                # Move list2 pointer forward
                list2 = list2.next

            # Move the current node of the merged list forward
            node = node.next

        # At this point, one of the lists is fully traversed.
        # Simply attach the remaining part of the other list (if any)
        node.next = list1 or list2

        # Return the head of the merged list (skip dummy)
        return dummy.next
