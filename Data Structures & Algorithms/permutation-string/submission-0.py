class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        # frequency arrays for 26 lowercase letters
        freq1 = [0] * 26
        freq2 = [0] * 26

        # build freq for s1 and first window of s2
        for i in range(n1):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1

        # if first window already matches
        if freq1 == freq2:
            return True

        # slide the window over s2
        for i in range(n1, n2):
            # add new char
            freq2[ord(s2[i]) - ord('a')] += 1
            # remove char going out of window
            freq2[ord(s2[i - n1]) - ord('a')] -= 1

            if freq1 == freq2:
                return True

        return False