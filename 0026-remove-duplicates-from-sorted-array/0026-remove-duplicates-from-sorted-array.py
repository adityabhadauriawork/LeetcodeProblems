class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # n = len(nums)
        # l = 1
        # for r in range(1,n):
        #     if nums[r] != nums[r-1]:
        #         nums[l]=nums[r]
        #         l+=1
        # return l



        n = len(nums)
        left = 1
        for right in range(1, n):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left+=1
        return left















            
        