class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        for a in candies:
            b = max(candies)
            a = a + extraCandies
            if a>=b:
                ans.append(True)
                
            else:
                ans.append(False)
            
        return ans
        