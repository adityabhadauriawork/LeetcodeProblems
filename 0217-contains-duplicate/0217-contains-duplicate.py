class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq ={}
        for a in nums:
            if a in freq:
                freq[a]+=1
            else:
                freq[a]=1
        # dictionary mein sab freq. store hogyi ab kya beta kallu
        for b in freq:
            if freq[b]>1:
                return True
        return False
        