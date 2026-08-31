# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# _, _, _, _, _
# l, _, r, _, _
# _, _, l, _, r << where 2-1 = n!

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # Use dummy node to offset everything by 1 👍
        left = dummy
        right = dummy
        for i in range(n): # Move right n amount
            right = right.next
        while right and right.next: # While right has not hit null yet (or the next one)
            left = left.next # If starting out, skip the first iteration
            right = right.next
        left.next = left.next.next
        return dummy.next # Return dummy node in case linked list is now empty!    