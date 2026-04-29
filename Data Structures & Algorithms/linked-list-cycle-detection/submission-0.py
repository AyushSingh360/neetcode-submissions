# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # If list is empty or has just one node, it cannot have a cycle
        if not head or not head.next:
            return False

        slow = head
        fast = head.next  # can also start at head; logic just changes slightly

        # Move slow by 1 and fast by 2 until they meet or fast hits the end
        while fast and fast.next:
            if slow is fast:
                return True
            slow = slow.next
            fast = fast.next.next

        # If we exit the loop, fast hit null -> no cycle
        return False