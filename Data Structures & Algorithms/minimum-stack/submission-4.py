class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)

        if (val <= min(self.minStack)):
            self.minStack.append(val)
        
    def pop(self) -> None:
        
        val = self.stack.pop()
        if (val == self.minStack[-1]):
            self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.minStack)


