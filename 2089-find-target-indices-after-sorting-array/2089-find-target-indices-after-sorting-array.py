class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            if target == nums[i]:
                ans.append(i)
        return ans
        