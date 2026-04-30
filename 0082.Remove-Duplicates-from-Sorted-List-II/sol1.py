class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return head
        while head and head.next and head.val == head.next.val:
            cur = head.next
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            head = cur.next


        pre = head
        while pre and pre.next:
            cur = pre.next
            while cur and cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next
                cur = pre.next
            pre = cur

        return head



