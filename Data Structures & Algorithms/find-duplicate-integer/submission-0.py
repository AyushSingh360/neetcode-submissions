from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: find intersection in the cycle
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]          # move 1 step
            fast = nums[nums[fast]]    # move 2 steps
            if slow == fast:
                break

        # Phase 2: find the entrance to the cycle (duplicate number)
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow