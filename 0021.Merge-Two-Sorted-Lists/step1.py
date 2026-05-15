from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        dummy = ListNode()
        merged = dummy

        while node1 is not None or node2 is not None:
            if node1 is None:
                node1, node2 = node2, node1
            if node2 is None or node1.val < node2.val:
                merged.next = ListNode(val=node1.val)
                node1 = node1.next
            else:
                merged.next = ListNode(val=node2.val)
                node2 = node2.next
            merged = merged.next

        return dummy.next
