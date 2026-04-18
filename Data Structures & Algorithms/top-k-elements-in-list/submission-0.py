from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        # 1) Count frequencies
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # 2) Bucket numbers by frequency
        for num, c in count.items():
            freq[c].append(num)

        # 3) Collect from highest frequency down
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res