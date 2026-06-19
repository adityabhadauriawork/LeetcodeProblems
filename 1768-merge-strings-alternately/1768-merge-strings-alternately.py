class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        n1=len(word1)
        n2=len(word2)
        word=word1+word2
        d=0
        length=min(n1,n2)
        for _ in range(length):
            ans=ans+word[d]
            ans+=word[d+n1]
            d+=1
        if n1>n2:
            ans+=word1[d:]
        else:
            ans+=word2[d:]
            
        return ans

        
        