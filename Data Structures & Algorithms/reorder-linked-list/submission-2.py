# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # stack = []
        # currentNode = head
        # count = 0
        # while currentNode:
        #     stack.append(currentNode)
        #     count += 1
        #     currentNode = currentNode.next
        # currentNode = head
        # for i in range(count//2): # Move x between 1 > x > 2, 1.next = x, x.next = 2
        #     ne3t = currentNode.next
        #     currentNode.next = stack.pop() # 1.next = x
        #     currentNode = currentNode.next # move to x
        #     currentNode.next = ne3t # x.next set to 2
        #     currentNode = currentNode.next # Move to the next node
        # currentNode.next = None
        # return 

        # Optimal Solution
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            

        