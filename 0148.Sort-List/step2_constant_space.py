# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head

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

        def skip_nodes(head, n):
            count = 0
            for _ in range(n):
                if head is None:
                    return None, count
                count += 1
                head = head.next
            return head, count

        node = head
        length = 0
        while node is not None:
            length += 1
            node = node.next

        sorted_length = 1
        dummy = ListNode()
        dummy.next = head
        prev_merged_tail = dummy
        while sorted_length < length:
            prev_merged_tail = dummy
            next_head = dummy.next
            while next_head is not None:
                first_head = next_head
                second_head, length1 = skip_nodes(first_head, sorted_length)
                next_head, length2 = skip_nodes(second_head, sorted_length)
                prev_merged_tail.next = merge(first_head, second_head, length1, length2)
                prev_merged_tail, _ = skip_nodes(prev_merged_tail, length1 + length2)
            sorted_length *= 2
        prev_merged_tail.next = None

        return dummy.next
