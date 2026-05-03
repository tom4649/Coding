class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = head
        while cur:
            next = cur.next
            while next and next.val == cur.val:
                cur.next = next.next
                next = cur.next
            cur = next
        return head
