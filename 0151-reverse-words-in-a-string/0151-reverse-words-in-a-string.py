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
    def reverseWords(self, s: str) -> str:
        stack = Stack()
        words = s.split()
        for ch in words:
            stack.push(ch)
        ans = []
        while stack.size()>0:
            ans.append(stack.pop())

        return " ".join(ans)


        
        