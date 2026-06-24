# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None

        def merge(head1, head2, length1, length2):
            dummy = ListNode()
            head = dummy
            index1 = 0
            index2 = 0
            node1 = head1
            node2 = head2
            while index1 < length1 or index2 < length2:
                if index2 >= length2 or (index1 < length1 and node1.val < node2.val):
                    head.next = node1
                    head = head.next
                    node1 = node1.next
                    index1 += 1
                else:
                    head.next = node2
                    head = head.next
                    node2 = node2.next
                    index2 += 1
            head.next = None

            return dummy.next

        def merge_sort(head, length):
            if length == 1:
                return head

            half_length = length // 2
            second_head = head
            for _ in range(half_length):
                second_head = second_head.next

            first_head_sorted = merge_sort(head, half_length)
            second_head_sorted = merge_sort(second_head, length - half_length)
            return merge(
                first_head_sorted, second_head_sorted, half_length, length - half_length
            )

        node = head
        length = 0
        while node is not None:
            length += 1
            node = node.next

        return merge_sort(head, length)
