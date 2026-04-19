from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()   # will store indices, values in decreasing order in nums[dq]
        res = []

        for i, val in enumerate(nums):
            # 1) Pop from back while current value is greater,
            #    to keep dq values in decreasing order
            while dq and nums[dq[-1]] <= val:
                dq.pop()

            # 2) Push current index
            dq.append(i)

            # 3) Remove indices that are out of this window (i - k + 1 is window start)
            if dq[0] <= i - k:
                dq.popleft()

            # 4) If window has size k, record the max (front of deque)
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res