class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        count_zero = 0
        count_len = 0
        ans = 0
        for r in range(n):
            if nums[r] == 0:
                count_zero+=1
            
            while count_zero > 1:
                if nums[l]==0:    
                    
                    count_zero-=1
                l+=1
        
            ans = max(ans, r-l)
        return ans

            







        