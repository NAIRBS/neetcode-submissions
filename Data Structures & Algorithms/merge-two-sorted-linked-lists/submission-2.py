# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: # 15th Oct Revision
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # Make dummy the start pointer so can return that
        current = dummy
        while list1 and list2: # Add minimum of either list and iterate through that
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next # Move through the generated list
        current.next = list1 or list2 # At the end, add the last missing element from the lists
        return dummy.next # Return the start pointer header moved to the actual head
        