# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = {} # Use a hashmap to store visited node locations (in memory!)
        currentNode = head
        # if head.val: return False
        # hashmap[currentNode.val] = 1
        # currentNode = currentNode.next
        while currentNode:
            if currentNode.next not in hashmap: hashmap[currentNode.next] = 1
            else: return True
            currentNode = currentNode.next
        return False
        