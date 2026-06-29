class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        freq = {
            'a' : True,
            'e' : True,
            'i' : True,
            'o' : True,
            'u' : True
        }
        count = 0
        for i in range(k):
            if s[i] in freq:
                count+=1
        count2=count
        for i in range(k, len(s)):            
            if s[i] in freq:
                count2+=1

            if s[i-k] in freq:
                count2-=1
            count = max(count, count2)

        return count
            


        