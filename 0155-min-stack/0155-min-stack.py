
class MinStack:

    def __init__(self):
        self.stack = []
        self.MinStack = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.MinStack:
            self.MinStack.append(value)
        elif value <= self.MinStack[-1]:
            self.MinStack.append(value)
        

    def pop(self) -> None:
        if self.stack[-1] == self.MinStack[-1]:
            self.MinStack.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.MinStack[-1]        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()