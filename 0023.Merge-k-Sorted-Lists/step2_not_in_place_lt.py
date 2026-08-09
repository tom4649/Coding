import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        ListNode.__lt__ = lambda self, other: self.val < other.val

        heap = [node for node in lists if node is not None]
        heapq.heapify(heap)

        dummy = ListNode()
        node = dummy
        while heap:
            head = heapq.heappop(heap)
            node.next = ListNode(head.val)
            node = node.next
            if head.next is not None:
                heapq.heappush(heap, head.next)

        return dummy.next
