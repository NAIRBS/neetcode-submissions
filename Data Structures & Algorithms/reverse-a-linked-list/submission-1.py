# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head: return None
        # prev = head # Store prev as head
        # n3xt = 0
        # currentNode = head.next # Store node as after head
        # head.next = None # Set head as end of linked list by pointing to NULL
        # while currentNode: # While current node is not NULL (end of linked list)
        #     n3xt = currentNode.next # Store the next element
        #     currentNode.next = prev # Make current element point to previous element
        #     prev = currentNode # Store the current element as prev
        #     currentNode = n3xt # Move to next element
        # return prev # We break while loop when current node found empty, so return prev node!

        # The model answer
        prev, curr = None, head
        while curr:
            n3xt = curr.next
            curr.next = prev
            prev = curr
            curr = n3xt
        return prev