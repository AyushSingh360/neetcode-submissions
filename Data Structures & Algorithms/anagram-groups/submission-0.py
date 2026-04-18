from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)   # key: char count signature, value: list of anagrams

        for s in strs:
            count = [0] * 26      # assuming lowercase 'a'–'z'
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)

        return list(res.values())