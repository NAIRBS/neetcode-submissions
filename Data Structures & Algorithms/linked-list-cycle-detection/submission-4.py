# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: # 17th Oct Revision
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()
        dummyNode = head
        while dummyNode:
            if dummyNode in hashset: return True
            else: hashset.add(dummyNode)
            dummyNode = dummyNode.next
        return False