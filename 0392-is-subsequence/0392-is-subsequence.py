class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a=0
        b=0
        if s == "":
            return True 
        count=0
        while b < len(t) and a < len(s) :
            if s[a]!=t[b]:
                b+=1
            elif s[a]==t[b]:
                a+=1
                b+=1
                count+=1
        if count == len(s):
            return True
        else:
            return False
        
        