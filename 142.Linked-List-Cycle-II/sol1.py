class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        if not fast:
            return None
        while 1:
            if fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return None
            if fast == slow:
                break
        slow = head
        while 1:
            if fast == slow:
                return fast
            slow = slow.next
            fast = fast.next
