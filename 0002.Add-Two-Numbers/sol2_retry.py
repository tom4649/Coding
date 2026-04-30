# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not (l1 and l2):
            return 0
        dummy = ListNode()
        target_node = dummy
        node1 = l1
        node2 = l2
        carry = 0
        while carry != 0 or node1 or node2:
            number = carry
            if node1:
                number += node1.val
                node1 = node1.next
            if node2:
                number += node2.val
                node2 = node2.next
            carry = number // 10
            target_node.next = ListNode(val=number % 10)
            target_node = target_node.next
        return dummy.next
