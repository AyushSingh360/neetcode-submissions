from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Search space for k
        left, right = 1, max(piles)
        ans = right

        def can_finish(speed: int) -> bool:
            hours = 0
            for p in piles:
                # ceil(p / speed)
                hours += (p + speed - 1) // speed
                # early stop if already exceed h
                if hours > h:
                    return False
            return hours <= h

        while left <= right:
            mid = (left + right) // 2
            if can_finish(mid):
                ans = mid
                right = mid - 1  # try smaller speed
            else:
                left = mid + 1   # need larger speed

        return ans