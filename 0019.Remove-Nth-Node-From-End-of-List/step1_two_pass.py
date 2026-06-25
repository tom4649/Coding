# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        node = head
        while node is not None:
            node = node.next
            count += 1

        index_from_start = count - n
        if index_from_start < 0:
            raise ValueError(f"n is too large: {n}")
        if index_from_start == 0:
            return head.next

        node = head
        for _ in range(index_from_start - 1):
            node = node.next

        temp = node.next.next
        node.next.next = None
        node.next = temp

        return head
