# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from ast import List


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_head = None
        original_node = head
        while original_node:
            next_original_node = original_node.next
            original_node.next = reversed_head
            reversed_head = original_node
            original_node = next_original_node
        return reversed_head
