class Stack:
  def __init__(self):
    self.st=[]

  def push(self,x):
    self.st.append(x)

  def pop(self):
    if len(self.st)==0:
      return -1
    x=self.st[-1]
    self.st.pop()
    return x

  def top(self):
    if len(self.st)==0:
      return -1
    return self.st[-1]

  def size(self):
    return len(self.st)

class Solution:
    def removeStars(self, s: str) -> str:
        stack = Stack()
        for i in range(len(s)):
            if s[i] != '*':
                stack.push(s[i])
            else:
                stack.pop()
        ans = "".join(stack.st)
        return str(ans)
        