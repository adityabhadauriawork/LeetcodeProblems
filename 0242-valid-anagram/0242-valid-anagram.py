class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #bruteforce
        # dict1={}
        # dict2={}
        # for a in s:
        #     if a in dict1:
        #         dict1[a]+=1
        #     else:
        #         dict1[a]=1
        # for b in t:
        #     if b in dict2:
        #         dict2[b]+=1
        #     else:
        #         dict2[b]=1
        # if dict1==dict2:
        #     return True
        # return False
        # 2nd approach
        s=list(s)
        t=list(t)
        print(s)
        print(t)
        s.sort()
        t.sort()

        if s==t:
            return True
        return False
        