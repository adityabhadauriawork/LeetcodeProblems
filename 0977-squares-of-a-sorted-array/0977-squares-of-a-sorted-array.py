class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num<0:
                num=-1*num
                ans.append(num**2)
            else:
                ans.append(num**2)
         
        ans.sort()
        return ans