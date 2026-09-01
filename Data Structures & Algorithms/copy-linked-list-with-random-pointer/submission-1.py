"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution: # One pass with Hashmap
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = collections.defaultdict(lambda: Node(0)) # Create a dict when missing key, with value 0
        copy[None] = None
        cur = head
        while cur:
            copy[cur].val = cur.val
            copy[cur].next = copy[cur.next]
            copy[cur].random = copy[cur.random]
            cur = cur.next
        return copy[head]
