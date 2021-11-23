class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for i in range(0,n):
            fast = fast.next

        if fast is None:
            head = head.next
            return head
        else:
            while fast.next is not None:
                slow = slow.next
                fast = fast.next
            slow.next = slow.next.next

        return head
