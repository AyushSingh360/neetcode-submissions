class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # will store indices of bars in increasing height
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            # Treat i == n as a bar of height 0 to flush remaining stack
            cur_height = heights[i] if i < n else 0

            # When current bar is smaller, finalize rectangles for taller bars
            while stack and cur_height < heights[stack[-1]]:
                h = heights[stack.pop()]
                # If stack is empty, width extends from 0 to i-1
                # Else, from stack[-1] + 1 to i - 1
                left_boundary = stack[-1] if stack else -1
                width = i - left_boundary - 1
                max_area = max(max_area, h * width)

            stack.append(i)

        return max_area