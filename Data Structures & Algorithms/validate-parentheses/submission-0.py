class Solution:
    def isValid(self, s: str) -> bool:
        # map closing bracket -> opening bracket
        match = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for ch in s:
            # if it's an opening bracket, push to stack
            if ch in '([{':
                stack.append(ch)
            else:
                # must be a closing bracket, stack cannot be empty
                if not stack:
                    return False
                # top of stack must match
                if stack[-1] != match[ch]:
                    return False
                stack.pop()

        # valid only if no unmatched openings remain
        return len(stack) == 0