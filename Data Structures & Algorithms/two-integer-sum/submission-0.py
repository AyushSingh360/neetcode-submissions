from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}  # value -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in idx:
                return [idx[complement], i]
            idx[num] = i

        # per problem statement there is always exactly one solution
        return []