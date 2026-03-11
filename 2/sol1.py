# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def listnode_to_num(l):
    n_pow = 0
    num = 0
    while l:
        num += l.val * (10 ** n_pow)
        l = l.next
        n_pow += 1
    return num

def num_to_list(num):
    dummy = ListNode(0, None)
    cur = dummy
    while num > 0:
        digit = num % 10
        cur.next = ListNode(digit, None)
        cur = cur.next
        num //= 10
    return dummy.next if dummy.next else dummy

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d1, d2 = listnode_to_num(l1), listnode_to_num(l2)
        d_sum = d1 + d2
        return num_to_list(d_sum)

