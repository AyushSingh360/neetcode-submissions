from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        need = Counter(t)          # counts of chars we need from t
        missing = len(t)           # how many chars are still missing
        left = 0
        best_len = float("inf")
        best_l, best_r = 0, 0

        for right, ch in enumerate(s):
            # if this char is still needed, we reduce the missing count
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            # when we have a valid window (no missing chars)
            while missing == 0:
                # update best window
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_l, best_r = left, right

                # try to shrink from the left
                left_ch = s[left]
                need[left_ch] += 1
                if need[left_ch] > 0:
                    # this means we’re now missing one required char again
                    missing += 1
                left += 1

        return "" if best_len == float("inf") else s[best_l:best_r+1]