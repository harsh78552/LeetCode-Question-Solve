class MinStack:

    def __init__(self):
        self.original_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.original_stack:
            self.original_stack.append(val)
            self.min_stack.append(val)
        else:
            self.original_stack.append(val)
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)

    def pop(self) -> None:
        x = self.original_stack.pop()
        if x == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.original_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


createStack = MinStack()
createStack.push(-2)
createStack.push(7)
createStack.push(4)
createStack.push(5)
createStack.push(3)
createStack.push(7)
createStack.push(2)
print(createStack.getMin())

# print(createStack.original_stack)
