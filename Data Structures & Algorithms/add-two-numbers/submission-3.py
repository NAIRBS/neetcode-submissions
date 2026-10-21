# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
 
class Solution: # 21st Oct Revision
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2, count1, count2 = 0, 0, 0, 0
        while l1:
            num1 += l1.val * 10**count1
            count1 += 1
            l1 = l1.next
        while l2:
            num2 += l2.val * 10**count2
            count2 += 1
            l2 = l2.next
        result = num1 + num2
        output = ListNode(0)
        curr = output
        if result == 0: 
            return ListNode(0) # Edge case handling
        while result > 0:
            curr.next = ListNode(result % 10)
            result //= 10 
            curr = curr.next
        return output.next