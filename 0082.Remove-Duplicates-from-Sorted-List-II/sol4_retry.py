# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ast import List


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        tail = dummy
        node = tail.next
        while node and node.next:
            if node.val != node.next.val:
                tail = tail.next
                node = node.next
                continue
            while node.next and node.val == node.next.val:
                node = node.next
            tail.next = node.next
            node = node.next

        return dummy.next
