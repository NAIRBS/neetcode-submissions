# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: # 19th Oct Revision
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        left, right = dummyNode, dummyNode
        for i in range(n + 1): # Move just before the node to be removed...
            right = right.next
        while right: # Move both until right reaches the end (None)
            left = left.next
            right = right.next
        left.next = left.next.next # Bypass the target node
        return dummyNode.next # In case original head was removed
        