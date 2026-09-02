# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: # Sounds like a pretty good time for a STACK!
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack_1, stack_2, stack_res = [], [], []
        num1, num2, res = 0, 0, 0
        while l1:
            stack_1.append(l1.val)
            l1 = l1.next
        while l2:
            stack_2.append(l2.val)
            l2 = l2.next  
        while stack_1: num1 = num1 * 10 + stack_1.pop()
        while stack_2: num2 = num2 * 10 + stack_2.pop()
        res = num1 + num2
        if res == 0: 
            stack_res.append(0)
        else:
            while res > 0: # Convert 975 to 5, 7, 9
                stack_res.append(res%10)
                res = res//10   
        dummy = ListNode(0)
        current = dummy
        for i in stack_res:
            current.next = ListNode(i)
            current = current.next
        return dummy.next