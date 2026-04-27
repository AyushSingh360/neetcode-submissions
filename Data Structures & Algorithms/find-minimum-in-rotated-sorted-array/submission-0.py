from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = nums[0]

        while left <= right:
            # If current window is already sorted, nums[left] is the minimum in this window
            if nums[left] <= nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right) // 2
            res = min(res, nums[mid])

            # Left half is sorted, so minimum must be in right half
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                # Right half is unsorted; minimum is in left half including mid
                right = mid - 1

        return res