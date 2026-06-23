# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return

        ordered_list = []
        node = head
        while node is not None:
            ordered_list.append(node)
            node = node.next

        left = 0
        right = len(ordered_list) - 1
        while left < right:
            ordered_list[left].next = ordered_list[right]
            left += 1
            if left == right:
                break
            ordered_list[right].next = ordered_list[left]
            right -= 1

        ordered_list[left].next = None
