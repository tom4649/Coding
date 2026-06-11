class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None

        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        return slow
