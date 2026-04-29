class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        seen = set()
        cur = head
        if not cur:
            return head
        seen.add(cur.val)
        next = cur.next
        if not next:
            return cur
        while next:
            if next.val in seen:
                cur.next = next.next
                next = cur.next
            else:
                seen.add(next.val)
                next = next.next
                cur = cur.next
        return head
