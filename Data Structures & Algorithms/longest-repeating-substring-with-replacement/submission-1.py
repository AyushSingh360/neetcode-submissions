class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}          # char -> frequency in current window
        left = 0
        max_freq = 0        # max frequency of a single char in current window
        res = 0

        for right, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            max_freq = max(max_freq, count[ch])

            # window size is (right - left + 1)
            # replacements needed = window size - max_freq
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res