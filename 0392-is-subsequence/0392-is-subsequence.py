class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # a=0
        # b=0
        # if s == "":
        #     return True 
        # count=0
        # while b < len(t) and a < len(s) :
        #     if s[a]!=t[b]:
        #         b+=1
        #     elif s[a]==t[b]:
        #         a+=1
        #         b+=1
        #         count+=1
        # if count == len(s):
        #     return True
        # else:
        #     return False
        ##########################
        l = 0
        r = 0
        while r<len(t) and l<len(s):
            if s[l] == t[r]:
                l+=1
                r+=1
            else:
                r+=1
        return l == len(s)













        