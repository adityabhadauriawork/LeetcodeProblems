class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        t1=[]
        for ch in list(s):
            if ch!='#':
                s1.append(ch)
            elif len(s1)>0:   #if hash is coming and the length should be something of the stack then ->
                s1.pop()


        for ch in list(t):
            if ch!='#':
                t1.append(ch)
            elif len(t1)>0:   #if hash is coming and the length should be something of the stack then ->
                t1.pop()

        return t1==s1