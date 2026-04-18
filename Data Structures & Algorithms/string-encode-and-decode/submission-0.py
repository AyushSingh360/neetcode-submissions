from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        # format: <len>#<string><len>#<string>...
        res_parts = []
        for s in strs:
            res_parts.append(str(len(s)))
            res_parts.append('#')
            res_parts.append(s)
        return ''.join(res_parts)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)

        while i < n:
            # read length up to '#'
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # substring of the given length after '#'
            j += 1                      # move past '#'
            word = s[j:j + length]
            res.append(word)
            # move i to the start of the next encoded block
            i = j + length

        return res