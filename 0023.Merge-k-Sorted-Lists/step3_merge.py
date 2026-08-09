# Definition for singly-linked list.
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None

        def merge_two_lists(node1, node2):
            sentinel = ListNode()
            node = sentinel

            while node1 is not None and node2 is not None:
                if node1.val > node2.val:
                    node1, node2 = node2, node1
                node.next = node1
                node = node.next
                node1 = node1.next

            node.next = node1 if node1 is not None else node2
            return sentinel.next

        node_to_merge = collections.deque(lists)
        while 1:
            node1 = node_to_merge.popleft()

            if not node_to_merge:
                return node1

            node2 = node_to_merge.popleft()
            node_to_merge.append(merge_two_lists(node1, node2))
