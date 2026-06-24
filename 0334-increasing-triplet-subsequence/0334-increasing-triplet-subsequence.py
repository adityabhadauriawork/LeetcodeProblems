# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
        
#         n=len(nums)
#         first = float('inf')
#         second = float('inf')
#         for i in range(n):
#             if nums[i] <= first:
#                 first = nums[i]
#             if nums[i] > first and nums[i]  <= second:
#                 second = nums[i]
#             if nums[i] > first and nums[i] > second:
#                 return True
            
#         return False
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False