import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # Include index i to avoid comparison collisions when node values are equal.
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node is not None]
        heapq.heapify(heap)

        dummy = ListNode()
        node = dummy
        while heap:
            val, i, head = heapq.heappop(heap)
            node.next = ListNode(val)
            node = node.next
            if head.next is not None:
                heapq.heappush(heap, (head.next.val, i, head.next))

        return dummy.next
