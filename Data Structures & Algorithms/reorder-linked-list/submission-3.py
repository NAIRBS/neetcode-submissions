# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: # 19th Oct Revision
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        stack = []
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        while second:
            stack.append(second)
            second = second.next

        while stack:
            nextNode = curr.next
            top = stack.pop()
            curr.next = top
            top.next = nextNode
            curr = nextNode