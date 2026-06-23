# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        original_latter = slow.next
        slow.next = None
        node = None

        while original_latter is not None:
            temp = original_latter.next
            original_latter.next = node
            node = original_latter
            original_latter = temp

        original_former = head
        original_latter = node
        while original_former is not None and original_latter is not None:
            next_former = original_former.next
            next_latter = original_latter.next
            original_former.next = original_latter
            original_latter.next = next_former
            original_former = next_former
            original_latter = next_latter
