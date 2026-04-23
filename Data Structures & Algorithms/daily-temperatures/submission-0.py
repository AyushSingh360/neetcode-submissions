from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # will store indices, temperatures[stack] is monotonic decreasing

        for i, t in enumerate(temperatures):
            # While current temp is warmer than the temp at stack's top index,
            # this is the next warmer day for that earlier index.
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)

        return res