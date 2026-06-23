# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if head is None:
            return

        def find_middle(head):
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        middle = find_middle(head)
        latter = middle.next
        middle.next = None

        def reverse_list(head):
            node = None
            while head is not None:
                next_head = head.next
                head.next = node
                node = head
                head = next_head
            return node

        reversed_latter = reverse_list(latter)

        def merge_lists(former, latter):
            while former is not None and latter is not None:
                next_former = former.next
                next_latter = latter.next
                former.next = latter
                latter.next = next_former
                former = next_former
                latter = next_latter

        merge_lists(head, reversed_latter)
