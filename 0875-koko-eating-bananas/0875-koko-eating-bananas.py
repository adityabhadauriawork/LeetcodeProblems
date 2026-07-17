class Solution:
    def Hours(self , piles, mid):
        ans = 0
        for pile in piles:
            ans+=(pile+mid-1) // mid
        return ans
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        n = max(piles)
        r = n
        k = 0
        while l<=r:
            mid = (l+r) // 2
            if self.Hours(piles,mid)>h:
                l = mid+1        # banana khane ki speed bhada rahe isiliye here +1
            else:
                k = mid
                r = mid-1
        return k
        