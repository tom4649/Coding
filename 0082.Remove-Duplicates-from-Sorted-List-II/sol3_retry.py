# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ast import List


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        cur = prev.next
        while cur and cur.next:
            if cur.val != cur.next.val:
                prev = prev.next
                cur = cur.next
                continue
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            prev.next = cur.next
            cur = cur.next

        return dummy.next
