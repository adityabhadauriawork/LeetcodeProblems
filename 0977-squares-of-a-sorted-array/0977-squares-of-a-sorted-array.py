class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # ans = []
        # for num in nums:
        #     if num<0:
        #         num=-1*num
        #         ans.append(num**2)
        #     else:
        #         ans.append(num**2)
         
        # ans.sort()
        # return ans
########################################################
        n=len(nums)
        ans=[0]*n

        l = 0
        r = n - 1
        i = n - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                ans[i] = nums[l] * nums[l]
                l+=1
            else:
                ans[i] = nums[r] * nums[r]
                r-=1
            i-=1
        return ans

            
