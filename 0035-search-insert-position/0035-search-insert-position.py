class Solution:
    def lowerBound(self,nums,target):
        n = len(nums)
        l = 0
        r = n-1
        ans = n
        while l<=r:
            mid = (l+r) // 2
            if nums[mid]>=target:
                ans = mid
                r = mid-1 # first greater number milte hi rukna nhi hai , aur check krna hai that's why used
            else:
                l = mid+1
        return ans




    def searchInsert(self, nums , target):
        return self.lowerBound( nums ,target)
        
            
        

        
        