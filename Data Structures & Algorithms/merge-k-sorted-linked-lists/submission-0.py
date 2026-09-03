# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None

        res = ListNode(0)
        cur = res
        minHeap = []

        for lst in lists: # Throw alla dat into the heap
            if lst is not None:
                heapq.heappush(minHeap, NodeWrapper(lst))

        while minHeap: # While the heap aint empty, keep making the linked list
            node_wrapper = heapq.heappop(minHeap) # Since smallest element will keep surfacing...
            cur.next = node_wrapper.node
            cur = cur.next

            if node_wrapper.node.next:
                heapq.heappush(minHeap, NodeWrapper(node_wrapper.node.next))

        return res.next