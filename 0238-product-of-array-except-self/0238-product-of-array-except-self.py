# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         no_of_zeros=0
#         n=len(nums)
#         product = 1
#         for a in nums:
#             if a == 0:
#                 no_of_zeros+=1
#             elif a!=0:    
#                 product = product*a
#         if no_of_zeros > 1:
#             return [0]*n
#         answer = []
#         for i in range(n):
            
#             if no_of_zeros == 0:
#                 answer.append(product//nums[i])
#             if no_of_zeros == 1:
#                 if nums[i] != 0:
#                     answer.append(0)
#                 elif nums[i]==0:
#                     answer.append(product)
#         return answer
                
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        no_of_zeros=0
        n=len(nums)
        product = 1
        for a in nums:
            if a == 0:
                no_of_zeros+=1
            elif a!=0:    
                product = product*a
        if no_of_zeros > 1:
            return [0]*n
        for i in range(n):
            
            if no_of_zeros == 0:
                nums[i] = product//nums[i]
            if no_of_zeros == 1:
                if nums[i] != 0:
                    nums[i]=0
                elif nums[i]==0:
                    nums[i]=product
        return nums
                
        