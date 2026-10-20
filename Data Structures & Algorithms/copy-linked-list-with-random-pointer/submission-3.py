"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution: # 20th Oct Solution (this is two pass instead of one pass but more intuitive, so 2n not 1n)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {} # key: value == old_node_mem_addr: new_node_mem_addr << direct mapping for each element
        first, second = head, head
        while first: # Copy only values first
            old_to_new[first] = Node(first.val) # Create the node for each element
            first = first.next
        while second: # Connect next and random pointers
            old_to_new[second].next = old_to_new.get(second.next) # Search old_node_mem_addr, return new_node_mem_addr
            old_to_new[second].random = old_to_new.get(second.random) # same as above
            second = second.next
        return old_to_new.get(head) # same as above