from List import ListNode

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        p = dummy = ListNode(None)

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next

            p = p.next

        if l1 is not None:
            p.next = l1
        if l2 is not None:
            p.next = l2


        return dummy.next
