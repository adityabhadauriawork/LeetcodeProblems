class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == k:
                count+=1
                l+=1
                r-=1
            elif nums[l] + nums[r] < k:
                l+=1
            else:
                r-=1
        return count
        freq = {}

        # o(n) time comlexity code using map / dict
        freq = {}
        count = 0
        for a in nums:
            if k-a  in freq:
                count+=1
                freq[a]-=1
            else:
                freq[a] = 1
        return count

        













        