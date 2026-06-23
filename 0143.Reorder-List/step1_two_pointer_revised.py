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

        latter = slow.next
        slow.next = None
        node = None

        while latter is not None:
            next_latter = latter.next
            latter.next = node
            node = latter
            latter = next_latter

        former = head
        latter = node
        while former is not None and latter is not None:
            next_former = former.next
            next_latter = latter.next
            former.next = latter
            latter.next = next_former
            former = next_former
            latter = next_latter
