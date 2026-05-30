import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap_indices = [
            (node.val, i) for i, node in enumerate(lists) if node is not None
        ]
        heapq.heapify(heap_indices)
        dummy = ListNode()

        node = dummy
        while heap_indices:
            _, i = heapq.heappop(heap_indices)
            next_node = lists[i]
            node.next = next_node
            lists[i] = next_node.next
            if next_node.next is not None:
                heapq.heappush(heap_indices, (next_node.next.val, i))
            node = node.next

        return dummy.next
