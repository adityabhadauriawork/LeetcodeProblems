class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        n = len(nums)
        l = 0
        max_zero = 0
        max_len = 0
        for r in range(n):
            if nums[r] == 0:
                max_zero+=1
            
            while max_zero > k:
                if nums[l] == 0:
                    max_zero -=1
                l+=1

            length = r - l + 1
            max_len = max(max_len, length)
        return max_len





        