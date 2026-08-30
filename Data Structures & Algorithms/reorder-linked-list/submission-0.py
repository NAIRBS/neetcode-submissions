# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1 > 2 > 3 > 4 > 5 > 6 > 7 > 8
        # 1 > 8 > 2 > 7 > 3 > 6 > 4 > 5
        # 1 > 3 > 5 > 7
        # 2 > 4 > 6 > 8
        stack = []
        currentNode = head
        count = 0
        while currentNode:
            stack.append(currentNode)
            count += 1
            currentNode = currentNode.next
        currentNode = head
        for i in range(count//2): # Move x between 1 > x > 2, 1.next = x, x.next = 2
            ne3t = currentNode.next
            currentNode.next = stack.pop() # 1.next = x
            currentNode = currentNode.next # move to x
            currentNode.next = ne3t # x.next set to 2
            currentNode = currentNode.next # Move to the next node
        currentNode.next = None
        return 
            

        