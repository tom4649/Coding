# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if head is None:
            return

        def find_middle(head: ListNode | None) -> ListNode | None:
            # when the number of nodes is odd, the middle node is the left half of the list
            # when the number of nodes is even, the middle node is the right half of the list
            slow = head
            fast = head
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            return slow

        middle = find_middle(head)
        latter = middle.next
        middle.next = None

        def reverse_list(head: ListNode | None) -> ListNode | None:
            node = None
            while head is not None:
                next_head = head.next
                head.next = node
                node = head
                head = next_head
            return node

        reversed_latter = reverse_list(latter)

        def interleave(former: ListNode | None, latter: ListNode | None) -> None:
            while former is not None and latter is not None:
                next_former = former.next
                next_latter = latter.next
                former.next = latter
                latter.next = next_former
                former = next_former
                latter = next_latter

        interleave(head, reversed_latter)
