# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        if curr is None:
            return None

        count = 1

        while curr.next:
            curr = curr.next
            count += 1

        if count == 1:
            return curr

        mid = 0

        if count % 2 == 0:
            mid = count // 2
        else:
            mid = (count // 2) + 1

        currTwo = head
        while currTwo.next:
            currTwo = currTwo.next
            count -= 1
            if count == mid:
                return currTwo
