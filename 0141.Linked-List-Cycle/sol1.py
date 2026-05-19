class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = set()
        while head and head.next:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
