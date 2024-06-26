
class Solution(object):
def reverseKGroup(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if not head or not head.next:
        return head

    tail = head
    for i in range(k):
        if not tail:
            return head

        tail = tail.next

    tail = self.reverseKGroup(tail, k)

    for i in range(k):
        next = head.next
        head.next = tail
        tail = head
        head = next

    return tail
