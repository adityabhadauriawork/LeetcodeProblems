class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        freq={}
        for i, a in enumerate(nums):
           
            
            if target-a in freq:
                return [freq[target-a], i]
            if a not in freq:
                freq[a]=i

        

            


        