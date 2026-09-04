# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1: return head

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # 1. Check if there are k nodes left to reverse
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next # Less than k nodes left, we are done

            groupNext = kth.next

            # 2. Reverse the k nodes
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # 3. Connect with the previous and next parts of the list
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp