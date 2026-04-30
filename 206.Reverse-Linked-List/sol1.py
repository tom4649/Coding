# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = deque()
        while head:
            stack.append(head)
            head = head.next
        if len(stack) == 0:
            return None
        head_new = stack.pop()
        cur_list = head_new
        while len(stack) > 0:
            cur_list.next = stack.pop()
            cur_list = cur_list.next
        cur_list.next = None
        return head_new


