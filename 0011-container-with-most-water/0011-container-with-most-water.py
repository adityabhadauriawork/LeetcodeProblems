class Solution:
    def maxArea(self, height: List[int]) -> int:

        # BRUTE FORCE
        # ans = 0
        # for l in range(len(height)):
        #     for r in range(l+1, len(height)):
        #         area = (r - l) * min(height[l], height[r])
        #         ans = max(ans,area)
        # return ans

        # optimized soltuion two pointer -> to find the big l and breath instead of going on everyone

        left = 0
        res= 0 
        right = len(height) - 1
        while left < right:
            area = (right - left) * min(height[left] , height[right])

            if height[left] < height[right]:
                left+=1
            else:
                right -=1
            
            res = max(res, area)
        return res


        