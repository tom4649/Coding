# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index_to_node = {}
        index = 0
        node = head
        while node is not None:
            index_to_node[index] = node
            node = node.next
            index += 1

        index_from_start = index - n
        if index_from_start < 0:
            raise ValueError(f"n is too large: {n}")
        if index_from_start == 0:
            return head.next

        index_to_node[index_from_start - 1].next = index_to_node[index_from_start].next
        index_to_node[index_from_start].next = None

        return head
