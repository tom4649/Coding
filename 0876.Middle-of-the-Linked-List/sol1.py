# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        pos_to_node = {}
        pos = 0

        while head is not None:
            pos_to_node[pos] = head
            head = head.next
            pos += 1

        return pos_to_node[pos // 2]
