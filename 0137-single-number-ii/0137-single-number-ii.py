class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {} 
        for a in nums:
            if a in freq:
                #hehhe
                freq[a]+=1
            else:
                freq[a]=1
        for key,value in freq.items():
            if value==1:
                return key
                     
        