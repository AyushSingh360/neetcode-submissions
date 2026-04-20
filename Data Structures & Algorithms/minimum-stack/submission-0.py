class MinStack:

    def __init__(self):
        # stack for all values
        self.stack = []
        # stack for current mins
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if min_stack empty or new val <= current min, push it to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # pop from main stack
        val = self.stack.pop()
        # if popped value is current min, pop from min_stack as well
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]