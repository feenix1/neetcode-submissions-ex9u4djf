class MinStack:
    stack = []
    prefix_min = []

    def __init__(self):
        self.stack.clear()
        self.prefix_min.clear()
        pass

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.prefix_min) == 0:
            self.prefix_min.append(val)
            return
        if val < self.prefix_min[-1]:
            self.prefix_min.append(val)
        else:
            self.prefix_min.append(self.prefix_min[-1])

    def pop(self) -> None:
        self.stack.pop(-1)
        self.prefix_min.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix_min[-1]