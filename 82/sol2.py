class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(-1, head)
        cur = dummy
        while cur:
            is_duplicated = False
            while cur.next and cur.next.next and cur.next.val == cur.next.next.val:
                is_duplicated = True
                cur.next = cur.next.next
            if is_duplicated:
                duplicated_val = cur.next.val
                while cur.next and cur.next.val == duplicated_val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
