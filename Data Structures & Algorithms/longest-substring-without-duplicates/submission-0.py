class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}        # maps char -> last index seen
        left = 0               # left side of the sliding window
        max_len = 0

        for right, ch in enumerate(s):
            # If we have seen this character and it's inside the current window,
            # move the left pointer just past the previous occurrence.
            if ch in char_index and char_index[ch] >= left:
                left = char_index[ch] + 1

            # Update or record the current character's index
            char_index[ch] = right

            # Window length is right - left + 1
            max_len = max(max_len, right - left + 1)

        return max_len