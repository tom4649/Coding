# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(next=head)
        slow = dummy
        fast = dummy
        for _ in range(n):
            fast = fast.next

        if fast is None:
            raise ValueError(f"n is too large: {n}")

        while fast.next:
            slow = slow.next
            fast = fast.next

        removed_node = slow.next
        slow.next = removed_node.next
        removed_node.next = None

        return dummy.next
