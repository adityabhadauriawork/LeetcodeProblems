class Solution:
    def maxArea(self, height: List[int]) -> int:
        # ans = 0
        # for r in range(len(height)):
        #     l = r+1
            
        #     while l <= len(height) - 1:
        #         brth = l - r
        #         leng = min(height[r] , height[l])
        #         area = leng * brth
        #         ans = max(ans, area)
        #         l+=1
                
        # return ans

        ###########
        l = 0
        n = len(height)
        r = n-1
        ans = 0
        while l<r:
            area = (r-l) * (min(height[l] , height[r]))
            ans = max(ans, area)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
            
        return ans



        

        