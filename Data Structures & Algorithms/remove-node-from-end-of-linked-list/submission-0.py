# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node to handle removal of head cleanly
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both until fast is at the last node
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        # slow is just before node to delete
        slow.next = slow.next.next

        return dummy.next