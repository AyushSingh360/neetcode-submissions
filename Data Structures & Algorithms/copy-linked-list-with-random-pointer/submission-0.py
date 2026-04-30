# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Map from original node -> copied node
        old_to_new = {}

        # First pass: create all nodes (val, next) and fill map
        curr = head
        while curr:
            copy = Node(curr.val)
            old_to_new[curr] = copy
            curr = curr.next

        # Second pass: assign next and random pointers
        curr = head
        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new.get(curr.next)      # None if curr.next is None
            copy.random = old_to_new.get(curr.random)  # None if curr.random is None
            curr = curr.next

        return old_to_new[head]